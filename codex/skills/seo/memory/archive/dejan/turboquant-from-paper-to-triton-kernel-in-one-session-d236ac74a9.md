---
source: https://dejan.ai/blog/turboquant/
title: TurboQuant: From Paper to Triton Kernel in One Session
scraped: 2026-03-25
published_on: 2026-03-25
tags: live_feed, phase1_ingest, dejan, practitioner, reverse-engineering, grounding, archive_backfill, historical_source
topic: ai_reverse_engineering
intent: research, monitoring, source_selection, ai_selection
role: researcher, seo, pinchy
confidence: high
canonical: false
canonical_group: Archive backfill - DEJAN / Dan Petrovic
use_for: historical_patterns, archive_research, source_examples
avoid_for: final_strategy_without_canonical_review
---

# TurboQuant: From Paper to Triton Kernel in One Session

Source: DEJAN / Dan Petrovic
Homepage: https://dejan.ai/blog/
Original URL: https://dejan.ai/blog/turboquant/
Published: 2026-03-25
Strength: AI-search reverse engineering, grounding, AI Mode, machine readability

## Summary
Implementing Google’s KV cache compression algorithm on Gemma 3 4B and everything that went wrong along the way. On March 24, 2026, Google Research published a blog post introducing TurboQuant, a compression algorithm for large language model inference. The paper behind it, “Online Vector Quantization with Near-optimal Distortion Rate” had been on arXiv since April […]

## Extracted Body
DEJAN AI is an AI SEO agency widely regarded as the leading authority in AI search visibility innovation.

Implementing Google’s KV cache compression algorithm on Gemma 3 4B and everything that went wrong along the way.

On March 24, 2026, Google Research published a blog post introducing TurboQuant , a compression algorithm for large language model inference. The paper behind it, “ Online Vector Quantization with Near-optimal Distortion Rate ” had been on arXiv since April 2025 and was accepted at ICLR 2026 . The claims were striking: compress the key-value cache to 3 bits per coordinate with zero accuracy loss, no training required, and up to 8x speedup on H100 GPUs.

I decided to implement it from scratch and see if the claims held up. They did, and then some.

Every time a transformer generates a token, it computes attention over all previous tokens. The key-value (KV) cache stores those previously computed states to avoid redundant work. As sequences get longer, this cache becomes a serious memory bottleneck, it grows linearly with sequence length and consumes precious GPU memory that could otherwise be used for larger batches or longer contexts.

Vector quantization is the obvious solution: compress the KV cache to fewer bits. But traditional quantization methods carry hidden overhead. They need to store normalization constants (zero points, scales) for every small block of data, typically adding 1-2 extra bits per number. At low bit-widths, this overhead can eat a significant chunk of the compression gains.

TurboQuant eliminates this overhead through a two-stage approach built on a clean mathematical insight.

Stage 1 — Random rotation + Lloyd-Max quantization. The algorithm applies a random orthogonal rotation to each KV vector. This is the key trick: after rotation, each coordinate’s distribution becomes a known Beta distribution, concentrated near zero with a predictable shape that depends only on the vector dimension. Because the distribution is known analytically, you can precompute the optimal scalar quantizer (a Lloyd-Max quantizer) once and reuse it for every vector. No per-block normalization constants, no data-dependent calibration, no training. Just rotate and quantize.

Stage 2 — QJL residual correction. The paper’s inner-product-optimized variant (TurboQuant_prod) applies a 1-bit Quantized Johnson-Lindenstrauss transform to the quantization residual. This gives an unbiased inner product estimator, which matters because attention scores are inner products. This stage requires a custom attention kernel to realize its benefits, you can’t just add the QJL correction back to the reconstructed vector (more on that later).

The theoretical backing is strong: TurboQuant’s MSE distortion is provably within a factor of ~2.7 of the information-theoretic lower bound. For a data-oblivious algorithm (one that doesn’t look at the data distribution), that’s essentially optimal.

We implemented TurboQuant from scratch in PyTorch and tested it on Gemma 3 4B IT running on an RTX 4090. The implementation has three layers, each building on the last:

Layer 1: Core algorithm ( turboquant_core.py ). The random rotation, Lloyd-Max codebook computation, and quantize/dequantize operations. The codebook is built once for a given (dimension, bit-width) pair by running 300 iterations of Lloyd-Max optimization over a dense numerical grid of the Beta distribution. This takes a few seconds on CPU and the result is cached.

Layer 2: Python KV cache integration ( turboquant_kv_cache.py ). A patched DynamicCache that quantizes key and value tensors on every cache.update() call. This is the simplest integration path, it works with any HuggingFace model and requires no model-specific code. The tradeoff is that it stores the dequantized fp16 tensors back in the cache, so you don’t save memory; you only simulate the accuracy impact of quantization.

Layer 3: Triton fused kernel ( triton_attention.py + turboquant_fused.py ). A custom Triton kernel that computes attention scores directly from compressed uint8 key indices, never materializing fp16 keys. This is where the real memory and speed gains come from.

The fused kernel exploits a simple algebraic identity. Since the rotation matrix R is orthogonal:

$$\langle q, R^T \cdot \text{centroids}[\text{idx}] \rangle = \langle R \cdot q, \text{centroids}[\text{idx}] \rangle$$

Pre-rotate the query once with a single matmul, then the per-KV-position work reduces to a centroid table lookup and dot product. The Triton kernel does this across all sequence positions in parallel, loading uint8 indices instead of fp16 values, roughly 4x less data from GPU memory.

On synthetic vectors (d=256), the quantize-dequantize roundtrip quality:

The fused kernel vs standard dequantize-then-matmul, measuring just the Q@K^T operation:

Cosine similarity between the kernel output and PyTorch reference: 1.000000. The kernel is numerically exact.

Three prompts: explain compilers vs interpreters, write a palindrome function, causes of the French Revolution. Each generated up to 200 tokens with greedy decoding.

The 2-bit fused path produces character-for-character identical output to the fp16 baseline on all three prompts, at the same speed, with 3-6x less VRAM for the KV cache.

After random rotation on the unit sphere S^{d-1}, each coordinate follows a Beta((d-1)/2, (d-1)/2) distribution on [-1, 1]. For large d (Gemma 3 uses d=256), this concentrates tightly around zero with standard deviation approximately 1/sqrt(d) ≈ 0.0625.

The codebook construction solves the continuous k-means problem for this distribution: partition [-1, 1] into 2^b intervals and find the centroid of each interval that minimizes weighted MSE under the Beta PDF. We use a dense grid (50,000 points) focused on the ±6σ range where the distribution has mass, then run standard Lloyd-Max iteration: assign grid points to nearest centroid, update centroids as weighted means, repeat.

The resulting codebook has an interesting structure — the centroids cluster densely near zero where the distribution is concentrated, with wider spacing in the tails. At 4 bits (16 levels), the centroid spacing near zero is approximately 0.008, providing very fine-grained reconstruction in the region where most values live.

The paper uses a randomized Hadamard transform (H · diag(signs)) for the rotation. We initially implemented this faithfully — and it was catastrophically slow. The Fast Walsh-Hadamard Transform is a series of butterfly operations, and our Python implementation executed each butterfly as a tensor slice operation. On GPU, this meant thousands of tiny CUDA kernel launches per rotation, with Python-level loop overhead between each one.

We replaced it with a precomputed random orthogonal matrix via QR decomposition. Mathematically equivalent — any orthogonal rotation on S^{d-1} produces the same Beta distribution on coordinates. The QR matrix is d×d (256×256 = 256KB, negligible), computed once from a seeded random Gaussian matrix, and the rotation becomes a single torch.matmul . Problem solved.

A production implementation would use a structured rotation (Hadamard + random signs) with a fused CUDA kernel for the butterfly operations. The structured form is more memory-efficient (you only store the d random signs, not a d×d matrix) and the butterfly operations parallelize beautifully on GPU. But for a reference implementation, the dense matrix works fine.

The kernel parallelizes over (query_head × batch, sequence_position_block). Each program instance:

The autotuner searches over 5 configurations of (BLOCK_S, BLOCK_D) and warp count. On the RTX 4090, it typically selects BLOCK_S=64, BLOCK_D=64 with 4 warps.

The key efficiency win is memory bandwidth. Loading uint8 indices requires 1 byte per element; loading fp16 keys requires 2 bytes. The centroid table (16 float32 values at 4-bit, or 4 values at 2-bit) fits comfortably in L1/L2 cache and is reused across all sequence positions. The net effect is roughly 2x less data movement from HBM, which translates to the observed ~1.2x speedup on the Q@K^T operation.

Gemma 3 4B uses Grouped Query Attention with 8 query heads and 4 KV heads (ratio 2:1). The kernel handles this by mapping each query head to its corresponding KV head: kv_head = q_head // gqa_ratio . The key indices and norms are loaded from the KV head, while queries come from the query head. This means each KV head’s compressed data is read twice (once per query head in its group), but since it’s small (uint8), the redundant reads are cheap.

The fused integration stores keys in compressed form (uint8 indices + fp16 norms per vector) and values in standard fp16. We only compress keys because the attention score computation (Q@K^T) is where the memory bandwidth bottleneck lives during decoding. The softmax@V multiplication is less critical because it’s compute-bound rather than memory-bound at typical sequence lengths.

A fully optimized implementation would also compress values, but the gains are smaller and the integration is more complex (you’d need a second Triton kernel for the softmax@V step with compressed values).

The paper describes two variants: TurboQuant_mse (pure Lloyd-Max, best for reconstruction) and TurboQuant_prod (Lloyd-Max + 1-bit QJL, best for inner products). Our first implementation used TurboQuant_prod for the KV cache: (bits-1) bits of Lloyd-Max plus 1 bit of QJL on the residual.

The QJL stage produces a correction term that makes the inner product estimator unbiased. But when you add this correction back to the reconstructed vector and store it in the KV cache, you’re injecting noise into the vector itself. The result: cosine similarity dropped to 0.69 (terrible) and the model produced garbage.

The fix was simple: use TurboQuant_mse (all bits to Lloyd-Max) for the drop-in cache, and reserve TurboQuant_prod for a custom attention kernel that can use the two-part representation directly. The fused Triton kernel implements the MSE variant.

We initially loaded the model with AutoModelForCausalLM and AutoTokenizer . This loaded the model fine, tokenized fine, and even generated — but every output token was <pad> (token ID 0). The baseline and quantized paths both produced identical pad sequences.

Gemma 3 4B+ is a multimodal model. It requires Gemma3ForConditionalGeneration and AutoProcessor , not the causal LM variants. The AutoProcessor handles the chat template correctly and returns the right token format. This wasn’t a quantization bug at all — the model simply wasn’t being invoked correctly.

The Fast Walsh-Hadamard Transform is O(d log d) butterfly operations. Our initial implementation ran each butterfly as a Python loop iteration with tensor slicing:

For d=256, this is 8 outer iterations × 128 inner iterations = 1,024 tiny CUDA operations per vector, with Python interpreter overhead between each one. On a KV cache update touching 26 layers × 4 KV heads × 256-dim vectors, the GPU was spending more time waiting for Python than doing math. Generation hung completely — even a 20-token completion with a trivial prompt didn’t return.

Replacing this with a single x @ Q_T matmul using a precomputed orthogonal matrix made it instant.

Our first KV cache integration subclassed HuggingFace’s DynamicCache . This broke immediately because Gemma 3’s model code calls past_key_values.is_initialized , past_key_values.key_cache , and other attributes whose names and semantics change across transformers versions. Our subclass was missing several of these.

The final approach is the cleanest: create a normal DynamicCache , save a reference to its update method, and replace it with a wrapper that quantizes inputs before calling the original. All the cache’s internal bookkeeping (sequence length tracking, layer indexing) works unchanged.

The FusedTurboQuantRunner returns decoded text directly (not output IDs), so we tried processor.encode(text) to count tokens for the timing report. But Gemma3Processor is a multimodal processor — it has decode but not encode . The tokenizer lives at processor.tokenizer.encode() . A one-line fix, but it crashed the first successful fused generation and hid the results until the next run.

Prince Canuma independently implemented TurboQuant in MLX and tested on Qwen 3.5 35B with context lengths up to 64K tokens. Their results: 6/6 exact match on needle-in-haystack at every quantization level, 4.9x smaller KV cache at 2.5-bit, 3.8x at 3.5-bit.

Two implementations, different frameworks (PyTorch+Triton vs MLX), different models (Gemma 3 4B vs Qwen 3.5 35B), different hardware (NVIDIA RTX 4090 vs Apple Silicon) — same conclusion. TurboQuant’s theoretical guarantees translate directly to practice across the board.

This implementation leaves several optimizations on the table:
