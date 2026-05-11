const refreshButton = document.getElementById("refreshNow");
const updatedAt = document.getElementById("updatedAt");
const liveBadge = document.getElementById("liveBadge");
const datasetBanner = document.getElementById("datasetBanner");
const streamMeta = document.getElementById("streamMeta");
const heroMetrics = document.getElementById("heroMetrics");
const goalMeta = document.getElementById("goalMeta");
const chunkChart = document.getElementById("chunkChart");
const pulseChart = document.getElementById("pulseChart");
const activeJobs = document.getElementById("activeJobs");
const pendingSummary = document.getElementById("pendingSummary");
const pendingSources = document.getElementById("pendingSources");
const coverageChart = document.getElementById("coverageChart");
const openclawBrain = document.getElementById("openclawBrain");
const sourceHealth = document.getElementById("sourceHealth");
const primaryBreakdown = document.getElementById("primaryBreakdown");
const squadBridge = document.getElementById("squadBridge");
const articleSources = document.getElementById("articleSources");
const recentKnowledge = document.getElementById("recentKnowledge");
const sourceSnapshots = document.getElementById("sourceSnapshots");
const logsGrid = document.getElementById("logsGrid");
const bulkProgressCard = document.getElementById("bulkProgressCard");
const fetchSourcesCard = document.getElementById("fetchSourcesCard");
const errorSourcesCard = document.getElementById("errorSourcesCard");
const activityTickerCard = document.getElementById("activityTickerCard");
const manualIngestForm = document.getElementById("manualIngestForm");
const manualIngestUrl = document.getElementById("manualIngestUrl");
const manualIngestSubmit = document.getElementById("manualIngestSubmit");
const manualIngestStatus = document.getElementById("manualIngestStatus");

const HISTORY_LIMIT = 420;
const HISTORY_REFRESH_MS = 45000;
const FALLBACK_POLL_MS = 12000;
const STREAM_RECONNECT_MS = 4000;

let historyItems = [];
let overviewState = null;
let stream = null;
let streamConnected = false;
let streamHeartbeatTimer = null;
let fallbackPollTimer = null;
let historyTimer = null;
let manualIngestFlashError = "";

function formatNumber(value) {
  return Number(value || 0).toLocaleString();
}

function formatMaybeNumber(value) {
  return value == null ? "Updating…" : formatNumber(value);
}

function formatBytes(bytes) {
  const value = Number(bytes || 0);
  if (value < 1024) return `${value} B`;
  const units = ["KB", "MB", "GB", "TB"];
  let size = value / 1024;
  let unit = units[0];
  for (let index = 0; index < units.length; index += 1) {
    unit = units[index];
    if (size < 1024 || index === units.length - 1) break;
    size /= 1024;
  }
  return `${size.toFixed(size >= 100 ? 0 : 1)} ${unit}`;
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function shortPath(value) {
  const text = String(value ?? "").trim();
  if (!text) return "";
  const parts = text.split("/");
  return parts.length <= 4 ? text : `.../${parts.slice(-4).join("/")}`;
}

function timeAgo(updatedAtIso) {
  if (!updatedAtIso) return "unknown";
  const diffMs = Date.now() - new Date(updatedAtIso).getTime();
  const seconds = Math.max(Math.round(diffMs / 1000), 0);
  if (seconds < 60) return `${seconds}s ago`;
  const minutes = Math.round(seconds / 60);
  if (minutes < 60) return `${minutes}m ago`;
  const hours = Math.round(minutes / 60);
  return `${hours}h ago`;
}

function clamp(value, min, max) {
  return Math.min(Math.max(value, min), max);
}

function mergeHistoryPoint(overview) {
  const point = {
    updated_at: overview.updated_at,
    updated_at_iso: overview.updated_at_iso,
    chunks: overview.db.chunks,
    paths: overview.db.paths,
    primary_chunks: overview.db.primary_chunks,
    live_article_chunks: overview.db.live_article_chunks,
    archive_article_chunks: overview.db.archive_article_chunks,
    live_article_notes: overview.articles.live_article_notes,
    archive_article_notes: overview.articles.archive_article_notes,
    primary_source_notes: overview.coverage.primary_source_notes,
    pending_total: overview.pending.pending_total,
    recent_fetch_total: overview.activity.recent_fetch_total,
    recent_fetch_ok: overview.activity.recent_fetch_ok,
    recent_fetch_error: overview.activity.recent_fetch_error,
  };
  const existingIndex = historyItems.findIndex((item) => item.updated_at_iso === point.updated_at_iso);
  if (existingIndex >= 0) {
    historyItems[existingIndex] = point;
  } else {
    historyItems.push(point);
    if (historyItems.length > HISTORY_LIMIT) {
      historyItems = historyItems.slice(-HISTORY_LIMIT);
    }
  }
}

function setLiveState(isLive, label) {
  streamConnected = isLive;
  liveBadge.classList.toggle("is-live", isLive);
  liveBadge.classList.toggle("is-stale", !isLive);
  liveBadge.innerHTML = `<span class="live-dot"></span>${escapeHtml(label || (isLive ? "Realtime feed" : "Polling fallback"))}`;
}

function scheduleHeartbeat() {
  window.clearTimeout(streamHeartbeatTimer);
  streamHeartbeatTimer = window.setTimeout(() => {
    setLiveState(false, "Feed cooling");
    if (overviewState?.updated_at_iso) {
      streamMeta.textContent = `No packet for ${timeAgo(overviewState.updated_at_iso)} • fallback polling active`;
    }
  }, STREAM_RECONNECT_MS * 2);
}

function buildLineChart(items, fields, colors, labels) {
  const width = 900;
  const height = 260;
  const left = 48;
  const right = 20;
  const top = 18;
  const bottom = 34;
  const chartWidth = width - left - right;
  const chartHeight = height - top - bottom;

  const cleaned = items.slice(-80);
  const allValues = cleaned.flatMap((item) => fields.map((field) => Number(item[field] || 0)));
  const maxValue = Math.max(...allValues, 1);
  const yTicks = 4;

  function pointFor(item, field, index) {
    const x = left + (chartWidth * index) / Math.max(cleaned.length - 1, 1);
    const y = top + chartHeight - (chartHeight * Number(item[field] || 0)) / maxValue;
    return { x, y };
  }

  function makePoints(field) {
    return cleaned.map((item, index) => pointFor(item, field, index));
  }

  function makePath(points) {
    return points.map((point, index) => `${index === 0 ? "M" : "L"} ${point.x.toFixed(2)} ${point.y.toFixed(2)}`).join(" ");
  }

  const primaryPoints = makePoints(fields[0]);
  const secondaryPoints = fields[1] ? makePoints(fields[1]) : [];
  const primaryPath = makePath(primaryPoints);
  const secondaryPath = secondaryPoints.length ? makePath(secondaryPoints) : "";
  const lastPrimary = primaryPoints.at(-1) || { x: left, y: top + chartHeight };
  const areaPath = `${primaryPath} L ${left + chartWidth} ${top + chartHeight} L ${left} ${top + chartHeight} Z`;

  const lines = Array.from({ length: yTicks + 1 }, (_value, index) => {
    const y = top + (chartHeight * index) / yTicks;
    const label = Math.round(maxValue - (maxValue * index) / yTicks);
    return `
      <line class="grid-line" x1="${left}" y1="${y}" x2="${left + chartWidth}" y2="${y}" />
      <text class="axis-label" x="6" y="${y + 4}">${formatNumber(label)}</text>
    `;
  }).join("");

  const xLabels = cleaned.length
    ? [cleaned[0], cleaned[Math.floor(cleaned.length / 2)], cleaned[cleaned.length - 1]]
        .map((item, index) => {
          const x = index === 0 ? left : index === 1 ? left + chartWidth / 2 : left + chartWidth;
          const stamp = String(item.updated_at || item.updated_at_iso || "").slice(5, 16).replace("T", " ");
          return `<text class="axis-label" x="${x}" y="${height - 8}" text-anchor="${index === 0 ? "start" : index === 1 ? "middle" : "end"}">${escapeHtml(stamp)}</text>`;
        })
        .join("")
    : "";

  const legend = fields
    .map(
      (_field, index) => `
        <g transform="translate(${left + index * 180}, ${height - 24})">
          <rect x="0" y="-10" width="12" height="12" rx="4" fill="${colors[index]}" />
          <text class="axis-label" x="18" y="0">${escapeHtml(labels[index])}</text>
        </g>
      `
    )
    .join("");

  return `
    <svg class="chart-svg" viewBox="0 0 ${width} ${height}" preserveAspectRatio="none">
      ${lines}
      <path class="area-fill" d="${areaPath}" />
      <path class="line-glow" d="${primaryPath}" />
      <path class="line-primary" stroke="${colors[0]}" d="${primaryPath}" />
      ${
        secondaryPath
          ? `<path class="line-glow-secondary" d="${secondaryPath}" />
             <path class="line-secondary" stroke="${colors[1]}" d="${secondaryPath}" />`
          : ""
      }
      <line class="scan-line" x1="${lastPrimary.x}" y1="${top}" x2="${lastPrimary.x}" y2="${top + chartHeight}" />
      <circle class="point-pulse" cx="${lastPrimary.x}" cy="${lastPrimary.y}" r="5" />
      ${xLabels}
      ${legend}
    </svg>
  `;
}

function renderManualIngest(overview) {
  if (!manualIngestStatus) return;
  const ingest = overview.manual_ingest || {};
  const current = ingest.current || null;
  const history = ingest.history || [];
  const active = Boolean(ingest.active);
  const result = current?.result || {};
  const status = current?.status || "idle";
  if (current && status !== "error" && manualIngestFlashError) {
    manualIngestFlashError = "";
  }
  const tone =
    active ? "running"
    : status === "completed" ? "success"
    : status === "error" ? "error"
    : "idle";
  const badge =
    active ? "Running"
    : status === "completed" ? "Latest Success"
    : status === "error" ? "Last Run Failed"
    : "Ready";
  const progress = clamp(Number(current?.progress_percent || 0), 0, 100);
  const sourceHost = current?.source_host || result.source_host || "waiting";
  const targetDb = current?.target_db_path || ingest.target_db_path || "";
  const notePath = current?.note_path || result.note_path || "";
  const manifestPath = current?.manifest_path || result.manifest_path || "";
  const articleTitle = current?.article_title || result.article?.title || "";
  const chunkDeltaValue = current?.chunk_delta ?? result.chunk_delta;
  const pathDeltaValue = current?.path_delta ?? result.path_delta;
  const chunkDelta =
    typeof chunkDeltaValue === "number"
      ? `${chunkDeltaValue >= 0 ? "+" : ""}${formatNumber(chunkDeltaValue)} chunks`
      : "delta pending";
  const pathDelta =
    typeof pathDeltaValue === "number"
      ? `${pathDeltaValue >= 0 ? "+" : ""}${formatNumber(pathDeltaValue)} paths`
      : "paths pending";
  const flashError = manualIngestFlashError
    ? `<div class="manual-ingest-flash">${escapeHtml(manualIngestFlashError)}</div>`
    : "";

  manualIngestStatus.innerHTML = `
    ${flashError}
    <div class="manual-ingest-card tone-${tone}">
      <div class="manual-ingest-head">
        <div>
          <div class="manual-ingest-topline">
            <span class="manual-status-chip ${tone}">${escapeHtml(badge)}</span>
            <span class="manual-ingest-phase">${escapeHtml(current?.phase || "idle")}</span>
          </div>
          <h3>${escapeHtml(current?.message || "Paste a URL and push it straight into memory.")}</h3>
          <p class="manual-ingest-copy">
            Target dataset: <strong>Squad Memory DB</strong> • ${escapeHtml(shortPath(targetDb) || "db not configured")}
          </p>
        </div>
        <div class="manual-ingest-progress-number">${progress.toFixed(0)}%</div>
      </div>
      <div class="progress-track manual-progress-track">
        <div class="progress-fill" style="width:${progress}%"></div>
      </div>
      <div class="manual-ingest-meta">
        <div class="manual-meta-card">
          <span>Source Host</span>
          <strong>${escapeHtml(sourceHost)}</strong>
        </div>
        <div class="manual-meta-card">
          <span>Chunk Delta</span>
          <strong>${escapeHtml(chunkDelta)}</strong>
        </div>
        <div class="manual-meta-card">
          <span>Path Delta</span>
          <strong>${escapeHtml(pathDelta)}</strong>
        </div>
        <div class="manual-meta-card">
          <span>Started</span>
          <strong>${escapeHtml(current?.started_at_iso ? timeAgo(current.started_at_iso) : "not started")}</strong>
        </div>
      </div>
      <div class="manual-ingest-detail-grid">
        <div class="manual-detail-block">
          <span>URL</span>
          <code>${escapeHtml(current?.url || "No URL queued yet.")}</code>
        </div>
        <div class="manual-detail-block">
          <span>Article</span>
          <strong>${escapeHtml(articleTitle || "Waiting for extraction…")}</strong>
        </div>
        <div class="manual-detail-block">
          <span>Note Path</span>
          <code>${escapeHtml(notePath || "Will appear after note creation.")}</code>
        </div>
        <div class="manual-detail-block">
          <span>Manifest</span>
          <code>${escapeHtml(manifestPath || "Will appear after rebuild.")}</code>
        </div>
      </div>
      <div class="manual-history">
        <div class="manual-history-head">
          <span>Recent Manual Runs</span>
          <strong>${formatNumber(history.length)}</strong>
        </div>
        ${
          history.length
            ? history
                .slice(0, 4)
                .map(
                  (item) => `
                    <div class="manual-history-item">
                      <div>
                        <div class="feed-item-title">${escapeHtml(item.url || "manual run")}</div>
                        <div class="feed-meta">${escapeHtml(item.message || item.status || "unknown")} • ${escapeHtml(item.updated_at_iso || "")}</div>
                      </div>
                      <span class="manual-history-pill ${escapeHtml(item.status || "idle")}">${escapeHtml(item.status || "idle")}</span>
                    </div>
                  `
                )
                .join("")
            : `<div class="manual-history-empty">No earlier dashboard ingests yet.</div>`
        }
      </div>
    </div>
  `;

  if (manualIngestForm && manualIngestSubmit && manualIngestUrl) {
    manualIngestSubmit.disabled = active;
    manualIngestUrl.disabled = active;
    manualIngestSubmit.textContent = active ? "Chunking…" : "Scrape + Chunk";
    if (current?.url && (active || !manualIngestUrl.value.trim())) {
      manualIngestUrl.value = current.url;
    }
  }
}

function renderGoalMeta(overview) {
  const label = overview.goal.over_target ? "Target crushed" : "Target climb";
  const progress = overview.goal.progress_percent.toFixed(1);
  const feedState = streamConnected ? "streaming live" : "polling fallback";
  goalMeta.textContent = `${label} • ${progress}% of target • ${feedState}`;
}

function renderDatasetBanner(overview) {
  if (!datasetBanner) return;
  const dataset = overview.dataset;
  if (!dataset) {
    datasetBanner.innerHTML = "";
    return;
  }

  const relatedRows = (dataset.related_datasets || []).slice(0, 4);
  const relatedHtml = relatedRows.length
    ? relatedRows
        .map(
          (item) => `
            <div class="dataset-related-card">
              <span>${escapeHtml(String(item.type || "related_to").replaceAll("_", " "))}</span>
              <strong>${escapeHtml(item.label || item.id || "Linked dataset")}</strong>
              <small>${formatMaybeNumber(item.chunks)} chunks</small>
            </div>
          `
        )
        .join("")
    : `<div class="dataset-related-empty">No linked datasets registered yet.</div>`;

  datasetBanner.innerHTML = `
    <div class="dataset-banner-head">
      <div>
        <p class="dataset-kicker">Dataset Truth Layer</p>
        <h3>${escapeHtml(dataset.label || "Unknown dataset")}</h3>
      </div>
      <span class="dataset-status ${dataset.status === "ready" ? "is-ready" : "is-missing"}">
        ${escapeHtml(dataset.status === "ready" ? "Live DB" : "Missing DB")}
      </span>
    </div>
    <p class="dataset-copy">${escapeHtml(dataset.purpose || "No dataset description available.")}</p>
    <div class="dataset-stats">
      <div class="dataset-stat">
        <span>File</span>
        <strong>${escapeHtml(dataset.path_name || "unknown")}</strong>
      </div>
      <div class="dataset-stat">
        <span>Chunks</span>
        <strong>${formatMaybeNumber(dataset.chunks)}</strong>
      </div>
      <div class="dataset-stat">
        <span>Paths</span>
        <strong>${formatMaybeNumber(dataset.paths)}</strong>
      </div>
      <div class="dataset-stat">
        <span>Count Band</span>
        <strong>${escapeHtml(dataset.expected_count_band || "n/a")}</strong>
      </div>
    </div>
    <div class="dataset-meta-row">
      <span>Owner: ${escapeHtml(dataset.owner || "unassigned")}</span>
      <span>Updated: ${escapeHtml(dataset.updated_at || "unknown")}</span>
      <span>Size: ${formatBytes(dataset.db_size_bytes || 0)}</span>
    </div>
    <div class="dataset-related">
      ${relatedHtml}
    </div>
  `;
}

function renderPulseChart() {
  if (!pulseChart) return;
  const recent = historyItems.slice(-60);
  if (!recent.length) {
    pulseChart.innerHTML = "";
    return;
  }
  pulseChart.innerHTML = buildLineChart(
    recent,
    ["recent_fetch_total", "pending_total"],
    ["#ffd166", "#82a7ff"],
    ["Fetches / 2m", "Pending queue"]
  );
}

function renderHeroMetrics(overview) {
  const previous = overviewState;
  const metrics = [
    {
      key: "elite-chunks",
      label: "Elite Chunks",
      value: Number(overview.db.chunks),
      formatted: formatNumber(overview.db.chunks),
      sub: `${formatNumber(overview.db.paths)} unique paths`,
    },
    {
      key: "openclaw-main",
      label: "OpenClaw Main",
      value: overview.openclaw.main.chunks,
      formatted: formatMaybeNumber(overview.openclaw.main.chunks),
      sub: overview.openclaw.main.paths == null ? "sqlite refresh in progress" : `${formatNumber(overview.openclaw.main.paths)} indexed paths`,
    },
    {
      key: "openclaw-seo",
      label: "OpenClaw SEO",
      value: overview.openclaw.seo.chunks,
      formatted: formatMaybeNumber(overview.openclaw.seo.chunks),
      sub:
        overview.openclaw.seo.chunks == null ? "sqlite refresh in progress"
        : overview.openclaw.seo.chunks === 0 && overview.openclaw.imports.skill_docs > 0 ? "index needs rebuild"
        : `${formatNumber(overview.openclaw.seo.paths || 0)} indexed paths`,
    },
    {
      key: "skill-docs",
      label: "Skill Docs",
      value: Number(overview.openclaw.imports.skill_docs),
      formatted: formatNumber(overview.openclaw.imports.skill_docs),
      sub: `${formatNumber(overview.openclaw.imports.skill_packs)} skill packs mirrored`,
    },
    {
      key: "live-articles",
      label: "Live Articles",
      value: Number(overview.articles.live_article_notes),
      formatted: formatNumber(overview.articles.live_article_notes),
      sub: `${formatNumber(overview.db.live_article_chunks)} elite chunks`,
    },
    {
      key: "hq-queue",
      label: "HQ Queue",
      value: Number(overview.openclaw.queue.total),
      formatted: formatNumber(overview.openclaw.queue.total),
      sub: `${formatNumber(overview.openclaw.queue.ready)} ready • ${formatNumber(overview.openclaw.queue.done)} done`,
    },
    {
      key: "pending",
      label: "Harvest Queue",
      value: Number(overview.pending.pending_total),
      formatted: formatNumber(overview.pending.pending_total),
      sub: overview.pending.pending_total ? "ready to harvest" : "discovery-limited",
    },
    {
      key: "squad-bridge",
      label: "Squad Bridge",
      value: Number(overview.bridge?.import_corpus?.chunks || 0),
      formatted: formatNumber(overview.bridge?.import_corpus?.chunks || 0),
      sub: `${formatNumber(overview.bridge?.recent_article_files || 0)} recent article files mirrored`,
    },
  ];

  heroMetrics.innerHTML = metrics
    .map((item) => {
      const previousValue = previous
        ? item.key === "elite-chunks"
          ? previous.db.chunks
          : item.key === "openclaw-main"
            ? previous.openclaw.main.chunks
            : item.key === "openclaw-seo"
              ? previous.openclaw.seo.chunks
              : item.key === "skill-docs"
                ? previous.openclaw.imports.skill_docs
            : item.key === "live-articles"
              ? previous.articles.live_article_notes
              : item.key === "hq-queue"
                ? previous.openclaw.queue.total
              : item.key === "squad-bridge"
                ? previous.bridge?.import_corpus?.chunks
              : previous.pending.pending_total
        : item.value;
      const changed = Number(previousValue || 0) !== Number(item.value || 0);
      return `
        <article class="metric-card">
          <div class="metric-label">${escapeHtml(item.label)}</div>
          <div class="metric-value counting ${changed ? "bump" : ""}">${escapeHtml(item.formatted)}</div>
          <div class="metric-sub">${escapeHtml(item.sub)}</div>
        </article>
      `;
    })
    .join("");
}

function renderChunkChart() {
  chunkChart.innerHTML = buildLineChart(
    historyItems,
    ["chunks", "live_article_notes"],
    ["#7cf2c7", "#82a7ff"],
    ["Chunks", "Live article notes"]
  );
}

function renderCoverageChart(overview) {
  const items = [
    { label: "Primary", value: overview.coverage.primary_source_notes },
    { label: "Live", value: overview.articles.live_article_notes },
    { label: "Archive", value: overview.articles.archive_article_notes },
  ];
  const max = Math.max(...items.map((item) => item.value), 1);
  coverageChart.innerHTML = `
    <div class="source-bars">
      ${items
        .map(
          (item, index) => `
            <div class="source-bar">
              <div class="source-bar-head">
                <span>${escapeHtml(item.label)}</span>
                <strong>${formatNumber(item.value)}</strong>
              </div>
              <div class="source-track">
                <div class="source-fill" style="width: ${(item.value / max) * 100}%; background: ${
                  ["linear-gradient(90deg,#ffd166,#ffefb3)", "linear-gradient(90deg,#82a7ff,#7cf2c7)", "linear-gradient(90deg,#9a82ff,#82a7ff)"][index]
                }"></div>
              </div>
            </div>
          `
        )
        .join("")}
    </div>
  `;
}

function renderOpenclawBrain(overview) {
  if (!openclawBrain) return;
  const rows = [
    ["Main FTS", `${formatMaybeNumber(overview.openclaw.main.chunks)} chunks`, overview.openclaw.main.paths == null ? "sqlite refresh in progress" : `${formatNumber(overview.openclaw.main.paths)} paths`],
    ["SEO FTS", `${formatMaybeNumber(overview.openclaw.seo.chunks)} chunks`, overview.openclaw.seo.chunks === 0 && overview.openclaw.imports.skill_docs > 0 ? "imported docs waiting for SEO index" : `${formatMaybeNumber(overview.openclaw.seo.paths)} paths`],
    ["Skill Packs", `${formatNumber(overview.openclaw.imports.skill_packs)} packs`, `${formatNumber(overview.openclaw.imports.skill_docs)} docs`],
    ["Graph + HQ", `${formatNumber(overview.openclaw.imports.graph_hq_assets)} assets`, `${formatNumber(overview.openclaw.imports.graph_hq_docs)} docs`],
    ["Managed Jobs", `${formatNumber(overview.openclaw.jobs.seo_jobs)} SEO jobs`, `${formatNumber(overview.openclaw.jobs.ok_jobs)} ok • ${formatNumber(overview.openclaw.jobs.error_jobs)} error`],
    ["Current Mission", overview.openclaw.queue.mission, `${overview.openclaw.queue.current_focus} • ${formatNumber(overview.openclaw.queue.ready)} ready`],
  ];
  openclawBrain.innerHTML = rows
    .map(
      ([label, value, meta]) => `
        <div class="metric-row">
          <div>
            <div class="feed-item-title">${escapeHtml(String(label))}</div>
            <div class="feed-meta">${escapeHtml(String(meta))}</div>
          </div>
          <strong>${escapeHtml(String(value))}</strong>
        </div>
      `
    )
    .join("");
}

function renderActiveJobs(overview) {
  activeJobs.innerHTML = overview.active_jobs
    .map(
      (job) => `
        <div class="status-item ${escapeHtml(job.status)}">
          <div>
            <div class="status-name">${escapeHtml(job.job)}</div>
            <div class="status-meta">${escapeHtml(job.updated_at)}${job.age_seconds != null ? ` • ${job.age_seconds}s ago` : ""}</div>
          </div>
          <span class="status-pill ${escapeHtml(job.status)}">${escapeHtml(job.status)}</span>
        </div>
      `
    )
    .join("");
}

function renderPending(overview) {
  pendingSummary.innerHTML = `
    <div class="queue-box"><span class="metric-label">Pending</span><strong>${formatNumber(overview.pending.pending_total)}</strong></div>
    <div class="queue-box"><span class="metric-label">Fetched</span><strong>${formatNumber(overview.pending.fetched_total)}</strong></div>
    <div class="queue-box"><span class="metric-label">Failed</span><strong>${formatNumber(overview.pending.failed_total)}</strong></div>
  `;
  const topSources = overview.pending.top_sources || [];
  if (!topSources.length) {
    pendingSources.innerHTML = `<div class="feed-item"><div class="feed-item-title">Queue is currently drained.</div><div class="feed-meta">The next gains come from discovery, not rerunning harvest.</div></div>`;
    return;
  }
  const max = Math.max(...topSources.map((item) => item.count), 1);
  pendingSources.innerHTML = topSources
    .map(
      (item) => `
        <div class="source-bar">
          <div class="source-bar-head">
            <span>${escapeHtml(item.source)}</span>
            <strong>${formatNumber(item.count)}</strong>
          </div>
          <div class="source-track"><div class="source-fill" style="width:${(item.count / max) * 100}%"></div></div>
        </div>
      `
    )
    .join("");
}

function renderPrimaryBreakdown(overview) {
  const rows = [
    ["Primary notes", overview.coverage.primary_source_notes],
    ["Primary chunks", overview.db.primary_chunks],
    ["Patent chunks", overview.db.google_patent_chunks],
    ["Search Central chunks", overview.db.google_search_central_chunks],
    ["Crawling infra chunks", overview.db.google_crawling_chunks],
  ];
  primaryBreakdown.innerHTML = rows
    .map(
      ([label, value]) => `
        <div class="metric-row">
          <span>${escapeHtml(String(label))}</span>
          <strong>${formatNumber(value)}</strong>
        </div>
      `
    )
    .join("");
}

function renderSquadBridge(overview) {
  if (!squadBridge) return;
  const bridge = overview.bridge || {};
  const rows = [
    ["Imported chunks", bridge.import_corpus?.chunks, `${formatMaybeNumber(bridge.import_corpus?.paths)} paths in squad db`],
    ["Selected files", bridge.selected_files, `${formatNumber(bridge.recent_article_files || 0)} recent article files`],
    ["Last sync delta", bridge.copied_last_run, `${formatNumber(bridge.removed_last_run || 0)} removed in latest run`],
    ["Squad DB", bridge.squad_db?.chunks, `${formatMaybeNumber(bridge.squad_db?.paths)} paths`],
    ["Manifest", bridge.manifest_updated_at || "missing", bridge.generated_at || "no generated_at"],
    ["Target root", "imports/seo-elite", bridge.index_updated_at || "index missing"],
  ];
  squadBridge.innerHTML = rows
    .map(
      ([label, value, meta]) => `
        <div class="metric-row">
          <div>
            <div class="feed-item-title">${escapeHtml(String(label))}</div>
            <div class="feed-meta">${escapeHtml(String(meta))}</div>
          </div>
          <strong>${typeof value === "number" ? escapeHtml(formatNumber(value)) : escapeHtml(String(value))}</strong>
        </div>
      `
    )
    .join("");
}

function renderSourceHealth(overview) {
  if (!sourceHealth) return;
  const recentFetch = overview.activity?.recent_fetch_sources || [];
  const recentErrors = overview.activity?.recent_error_sources || [];
  const liveSources = overview.sources?.snapshots || [];
  const recentErrorMap = new Map(recentErrors.map((item) => [item.source, Number(item.count || 0)]));
  const freshMap = new Map(
    liveSources.map((item) => {
      const host = String(item.slug || "").toLowerCase();
      return [host, item];
    })
  );

  const rows = recentFetch.slice(0, 6).map((item) => {
    const source = String(item.source || "");
    const slug = source.replace(/^www\./, "").replace(/\.com$|\.co\.uk$|\.ai$|\.co$|\.net$|\.org$/g, "");
    const freshness = freshMap.get(slug)?.updated_at || "recent";
    const errors = recentErrorMap.get(source) || 0;
    const status =
      errors >= 10 ? "Hot"
      : errors > 0 ? "Watch"
      : "Clean";
    return { source, fetches: Number(item.count || 0), errors, freshness, status };
  });

  sourceHealth.innerHTML = rows.length
    ? rows
        .map(
          (row) => `
            <div class="metric-row health-row">
              <div>
                <div class="feed-item-title">${escapeHtml(row.source)}</div>
                <div class="feed-meta">${escapeHtml(row.freshness)} • ${formatNumber(row.fetches)} fetches • ${formatNumber(row.errors)} errors</div>
              </div>
              <span class="health-pill ${row.status.toLowerCase()}">${escapeHtml(row.status)}</span>
            </div>
          `
        )
        .join("")
    : `<div class="feed-meta">No recent source-pressure sample yet.</div>`;
}

function renderArticleSources(overview) {
  const rows = [...(overview.sources.live_article_sources || []), ...(overview.sources.archive_article_sources || [])]
    .sort((a, b) => b.article_count - a.article_count)
    .slice(0, 16);
  const max = Math.max(...rows.map((item) => item.article_count), 1);
  articleSources.innerHTML = rows
    .map(
      (item) => `
        <div class="source-bar">
          <div class="source-bar-head">
            <span>${escapeHtml(item.source)} <span class="panel-meta">(${escapeHtml(item.layer)})</span></span>
            <strong>${formatNumber(item.article_count)}</strong>
          </div>
          <div class="source-track">
            <div class="source-fill" style="width:${(item.article_count / max) * 100}%"></div>
          </div>
        </div>
      `
    )
    .join("");
}

function renderRecentKnowledge(overview) {
  const items = [
    ...(overview.recent_knowledge.live_articles || []).map((item) => ({ ...item, type: "Live" })),
    ...(overview.recent_knowledge.primary_notes || []).map((item) => ({ ...item, type: "Primary" })),
    ...(overview.recent_knowledge.archive_articles || []).map((item) => ({ ...item, type: "Archive" })),
  ].slice(0, 12);
  recentKnowledge.innerHTML = items
    .map(
      (item) => `
        <article class="feed-item">
          <div class="feed-item-title">${escapeHtml(item.type)}</div>
          <div class="feed-item-path">${escapeHtml(item.path)}</div>
          <div class="feed-meta">${escapeHtml(item.updated)}</div>
        </article>
      `
    )
    .join("");
}

function renderSourceSnapshots(overview) {
  sourceSnapshots.innerHTML = (overview.sources.snapshots || [])
    .slice(0, 18)
    .map(
      (item) => `
        <div class="table-row">
          <div class="table-title">${escapeHtml(item.slug)}</div>
          <div class="table-meta">
            <span>${escapeHtml(item.layer)}</span>
            <span>${formatNumber(item.item_count)} items</span>
          </div>
          <div class="feed-meta">latest: ${escapeHtml(item.latest_published)} • ${escapeHtml(item.updated_at)}</div>
        </div>
      `
    )
    .join("");
}

function renderLogs(overview) {
  const groups = [
    ["Bulk Backfill", overview.logs.bulk_backfill],
    ["Article Harvest", overview.logs.article_harvest],
    ["Primary Refresh", overview.logs.primary_refresh],
    ["Bridge Sync", overview.logs.bridge_sync],
  ];
  logsGrid.innerHTML = groups
    .map(
      ([title, lines]) => `
        <div class="log-card">
          <div class="log-title">${escapeHtml(title)}</div>
          <ul>${(lines || []).map((line) => `<li>${escapeHtml(line)}</li>`).join("")}</ul>
        </div>
      `
    )
    .join("");
}

function renderActivity(overview) {
  const activity = overview.activity || {};
  const progress = activity.bulk_progress || { current: 0, total: 0, percent: 0 };
  const progressPercent = clamp(Number(progress.percent || 0), 0, 100);
  const currentPhase = activity.current_phase || "idle";
  const recentFetchTotal = Number(activity.recent_fetch_total || 0);
  const recentFetchOk = Number(activity.recent_fetch_ok || 0);
  const recentFetchError = Number(activity.recent_fetch_error || 0);
  const recentFetchWindowSeconds = Number(activity.recent_fetch_window_seconds || 120);
  const latestFetchSource = activity.latest_fetch_source || "";
  const latestFetchAt = activity.latest_fetch_at || "";
  const harvested = Number(activity.latest_harvested_notes || 0);
  const totalUrls = Number(activity.latest_total_urls || 0);
  const topFetch = activity.top_fetch_sources || [];
  const recentFetch = activity.recent_fetch_sources || [];
  const topErrors = activity.top_error_sources || [];
  const recentErrors = activity.recent_error_sources || [];
  const tickerItems = [
    ...(activity.ticker || []).slice(-8).map((line) => ({ type: "log", text: line })),
    ...(overview.pending.sample_urls || []).slice(0, 6).map((item) => ({
      type: "url",
      text: `${item.source}: ${item.title || item.url}`,
    })),
  ].slice(0, 12);

  const discoveryLive = currentPhase === "discovering" && recentFetchTotal > 0;
  const bulkLive = currentPhase === "harvesting" && progress.total > 0;
  const bulkCardLabel = bulkLive ? "Harvest Throughput" : discoveryLive ? "Discovery Live" : "Bulk Throughput";
  const bulkCardValue = bulkLive ? `${progressPercent.toFixed(1)}%` : discoveryLive ? `${formatNumber(recentFetchTotal)}` : "Idle";
  const bulkCardSub = bulkLive
    ? `${formatNumber(progress.current)} / ${formatNumber(progress.total)} items in current run`
    : discoveryLive
      ? `${formatNumber(recentFetchOk)} ok • ${formatNumber(recentFetchError)} errors in last ${Math.round(recentFetchWindowSeconds / 60)}m`
      : "Waiting for the next bulk cycle.";
  const bulkFillWidth = bulkLive
    ? progressPercent
    : discoveryLive
      ? clamp((recentFetchOk / Math.max(recentFetchTotal, 1)) * 100, 18, 100)
      : 6;
  const discoveryMetaRow = discoveryLive
    ? `
        <div class="activity-mini-row"><span>Latest source</span><strong>${escapeHtml(latestFetchSource || "unknown")}</strong></div>
        <div class="activity-mini-row"><span>Latest packet</span><strong>${escapeHtml(latestFetchAt || "live")}</strong></div>
      `
    : `
        <div class="activity-mini-row"><span>Latest harvested notes</span><strong>${formatNumber(harvested)}</strong></div>
        <div class="activity-mini-row"><span>Total harvested URLs</span><strong>${formatNumber(totalUrls)}</strong></div>
      `;

  bulkProgressCard.innerHTML = `
    <div class="activity-title">${escapeHtml(bulkCardLabel)}</div>
    <div class="activity-value">${escapeHtml(bulkCardValue)}</div>
    <div class="activity-sub">
      ${escapeHtml(bulkCardSub)}
    </div>
    <div class="progress-shell">
      <div class="progress-track"><div class="progress-fill" style="width:${bulkFillWidth}%"></div></div>
      <div class="activity-mini-list">
        ${discoveryMetaRow}
        <div class="activity-mini-row"><span>Pending queue</span><strong>${formatNumber(overview.pending.pending_total)}</strong></div>
      </div>
    </div>
  `;

  const fetchRows = discoveryLive && recentFetch.length ? recentFetch : topFetch;
  const maxFetch = Math.max(...fetchRows.map((item) => item.count), 1);
  fetchSourcesCard.innerHTML = `
    <div class="activity-title">Fastest Fetch Sources</div>
    <div class="activity-sub">${discoveryLive ? "Last 2 minutes of discovery activity." : "Live winners from the current scrape wave."}</div>
    <div class="activity-mini-list">
      ${
        fetchRows.length
          ? fetchRows
              .slice(0, 6)
              .map(
                (item) => `
                  <div class="source-bar">
                    <div class="source-bar-head">
                      <span>${escapeHtml(item.source)}</span>
                      <strong>${formatNumber(item.count)}</strong>
                    </div>
                    <div class="source-track"><div class="source-fill" style="width:${(item.count / maxFetch) * 100}%"></div></div>
                  </div>
                `
              )
              .join("")
          : `<div class="feed-meta">No fresh fetch events in the latest log window.</div>`
      }
    </div>
  `;

  const errorRows = discoveryLive && recentErrors.length ? recentErrors : topErrors;
  const maxErrors = Math.max(...errorRows.map((item) => item.count), 1);
  errorSourcesCard.innerHTML = `
    <div class="activity-title">Pressure / Blocks</div>
    <div class="activity-sub">${discoveryLive ? "Error pressure in the current discovery window." : "Sources generating the most fetch errors right now."}</div>
    <div class="activity-mini-list">
      ${
        errorRows.length
          ? errorRows
              .slice(0, 6)
              .map(
                (item) => `
                  <div class="source-bar">
                    <div class="source-bar-head">
                      <span>${escapeHtml(item.source)}</span>
                      <strong>${formatNumber(item.count)}</strong>
                    </div>
                    <div class="source-track"><div class="source-fill" style="width:${(item.count / maxErrors) * 100}%; background:linear-gradient(90deg,#ff7f96,#ffd166)"></div></div>
                  </div>
                `
              )
              .join("")
          : `<div class="feed-meta">No heavy error pressure in the latest log window.</div>`
      }
    </div>
  `;

  activityTickerCard.innerHTML = `
    <div class="activity-title">Live Ops Ticker</div>
    <div class="activity-sub">Latest log lines and queue candidates entering the brain.</div>
    <div class="ticker-shell">
      <div class="ticker-track">
        ${tickerItems
          .concat(tickerItems)
          .map(
            (item) => `
              <div class="ticker-item">
                <strong>${item.type === "url" ? "Queue" : "Log"}</strong>
                <div>${escapeHtml(item.text)}</div>
              </div>
            `
          )
          .join("")}
      </div>
    </div>
  `;

  const liveState = streamConnected
    ? "SSE live"
    : discoveryLive || bulkLive
      ? "Auto-refresh live"
      : stream
        ? "Connecting stream"
        : "Polling fallback";
  const phaseLabel =
    currentPhase === "discovering" ? `discovering • ${formatNumber(recentFetchTotal)} fetches / 2m`
      : currentPhase === "harvesting" ? `harvesting • ${formatNumber(progress.current)}/${formatNumber(progress.total)}`
      : currentPhase === "building" ? "building index"
      : `pending ${formatNumber(overview.pending.pending_total)}`;
  const suffix = progress.total
    ? `• ${phaseLabel}`
    : `• ${phaseLabel}`;
  streamMeta.textContent = `${liveState} • packet ${timeAgo(overview.updated_at_iso)} ${suffix}`;
}

function renderOverview(overview) {
  mergeHistoryPoint(overview);
  updatedAt.textContent = `Updated ${overview.updated_at}`;
  renderDatasetBanner(overview);
  renderManualIngest(overview);
  renderGoalMeta(overview);
  renderHeroMetrics(overview);
  renderCoverageChart(overview);
  renderOpenclawBrain(overview);
  renderActiveJobs(overview);
  renderPending(overview);
  renderPrimaryBreakdown(overview);
  renderSquadBridge(overview);
  renderSourceHealth(overview);
  renderArticleSources(overview);
  renderRecentKnowledge(overview);
  renderSourceSnapshots(overview);
  renderLogs(overview);
  renderActivity(overview);
  renderChunkChart();
  renderPulseChart();
  overviewState = overview;
}

async function loadHistory() {
  const response = await fetch(`/api/history?limit=400&ts=${Date.now()}`, { cache: "no-store" });
  const payload = await response.json();
  historyItems = payload.items || [];
  if (overviewState) {
    mergeHistoryPoint(overviewState);
  }
  renderChunkChart();
  renderPulseChart();
}

async function loadOverview(refresh = false) {
  const response = await fetch(`/api/overview?refresh=${refresh ? "1" : "0"}&ts=${Date.now()}`, { cache: "no-store" });
  const overview = await response.json();
  renderOverview(overview);
}

function stopFallbackPolling() {
  window.clearInterval(fallbackPollTimer);
  fallbackPollTimer = null;
}

function startFallbackPolling() {
  stopFallbackPolling();
  fallbackPollTimer = window.setInterval(() => {
    loadOverview(false).catch(console.error);
  }, FALLBACK_POLL_MS);
}

function connectStream() {
  if (!window.EventSource) {
    setLiveState(false, "Polling fallback");
    startFallbackPolling();
    return;
  }
  if (stream) {
    stream.close();
  }
  setLiveState(false, "Connecting");
  stream = new EventSource(`/api/stream?ts=${Date.now()}`);
  stream.addEventListener("open", () => {
    stopFallbackPolling();
    setLiveState(true, "Realtime feed");
    scheduleHeartbeat();
  });
  stream.addEventListener("overview", (event) => {
    scheduleHeartbeat();
    setLiveState(true, "Realtime feed");
    try {
      const overview = JSON.parse(event.data);
      renderOverview(overview);
    } catch (error) {
      console.error(error);
    }
  });
  stream.addEventListener("error", () => {
    setLiveState(false, "Reconnecting");
    window.clearTimeout(streamHeartbeatTimer);
    if (stream) {
      stream.close();
      stream = null;
    }
    startFallbackPolling();
    window.setTimeout(connectStream, STREAM_RECONNECT_MS);
  });
}

async function boot(refresh = false) {
  await Promise.all([loadHistory(), loadOverview(refresh)]);
}

if (manualIngestForm && manualIngestUrl && manualIngestSubmit) {
  manualIngestForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const url = manualIngestUrl.value.trim();
    if (!url) {
      manualIngestFlashError = "Paste a URL before starting the ingest.";
      if (overviewState) renderManualIngest(overviewState);
      return;
    }
    manualIngestFlashError = "";
    manualIngestSubmit.disabled = true;
    manualIngestSubmit.textContent = "Starting…";
    try {
      const response = await fetch(`/api/manual-ingest?ts=${Date.now()}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url }),
      });
      const payload = await response.json();
      if (!response.ok) {
        throw new Error(payload.error || "Could not start manual URL ingest.");
      }
      await loadOverview(false);
    } catch (error) {
      manualIngestFlashError = error instanceof Error ? error.message : "Could not start manual URL ingest.";
      if (overviewState) renderManualIngest(overviewState);
    } finally {
      if (!overviewState?.manual_ingest?.active) {
        manualIngestSubmit.disabled = false;
        manualIngestSubmit.textContent = "Scrape + Chunk";
      }
    }
  });
}

refreshButton.addEventListener("click", () => {
  boot(true).catch(console.error);
});

boot(true)
  .then(() => {
    connectStream();
    historyTimer = window.setInterval(() => {
      loadHistory().catch(console.error);
    }, HISTORY_REFRESH_MS);
  })
  .catch(console.error);
