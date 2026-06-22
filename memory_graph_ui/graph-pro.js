const graphProLayer = document.getElementById("graphProLayer");
const graphProFilters = document.getElementById("graphProFilters");

const CORE_KINDS = new Set([
  "brain",
  "domain",
  "memory_bank",
  "skill",
  "pack",
  "topic",
  "note",
  "publication",
  "outcome",
  "alert",
  "queue",
  "source",
  "stale_source",
]);

const OVERVIEW_KINDS = new Set([
  "brain",
  "domain",
  "memory_bank",
  "timeline",
  "publication",
  "queue",
  "alert",
  "outcome",
]);

const TIMELINE_LINK_KINDS = new Set(["timeline", "timeline_chunk", "timeline_outcome", "timeline_episode", "timeline_run"]);

const CAUSAL_LINK_PREFIXES = [
  "publication_",
  "evidence_",
  "topic_",
  "primary_",
  "used_",
  "episode_",
  "run_",
];

const graphProState = {
  ready: false,
  view: "hq",
  payload: null,
  filteredPayload: { nodes: [], links: [] },
  filters: {
    domains: new Set(),
    kinds: new Set(),
    source: "all",
    detail: "overview",
    viewMode: "topology",
    drillLevel: "overview",
    timelineBucket: "all",
    focusNodeId: null,
    playbackPercent: 100,
  },
  canvas: null,
  ctx: null,
  projectedNodes: [],
  selectedNodeId: null,
  hoveredNodeId: null,
  dragging: false,
  lastPointer: null,
  rotationY: 0.42,
  rotationX: -0.18,
  targetRotationY: 0.42,
  targetRotationX: -0.18,
  zoom: 1.04,
  targetZoom: 1.04,
  resizeObserver: null,
  animationFrame: null,
  playbackTimer: null,
  status: "Graph Pro is ready. Switch views to load the node-level map.",
  stars: Array.from({ length: 220 }, (_, index) => {
    const seed = index + 1;
    return {
      x: ((seed * 71) % 2400) - 1200,
      y: ((seed * 43) % 1800) - 900,
      z: ((seed * 97) % 2200) - 1100,
      size: 0.7 + ((seed * 17) % 7) * 0.12,
      alpha: 0.14 + ((seed * 29) % 10) * 0.03,
    };
  }),
};

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value));
}

function lerp(start, end, alpha) {
  return start + (end - start) * alpha;
}

function sanitizeMetric(value) {
  return Number.isFinite(Number(value)) ? Number(value) : 0;
}

function escapeHtml(value) {
  return String(value || "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;");
}

function titleCase(value) {
  return String(value || "")
    .replace(/[_-]+/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .replace(/\b\w/g, (match) => match.toUpperCase());
}

function rgba(hex, alpha) {
  const cleaned = String(hex || "#9fb3ff").replace("#", "");
  const fallback = { r: 159, g: 179, b: 255 };
  if (cleaned.length !== 6) return `rgba(${fallback.r}, ${fallback.g}, ${fallback.b}, ${alpha})`;
  const r = Number.parseInt(cleaned.slice(0, 2), 16);
  const g = Number.parseInt(cleaned.slice(2, 4), 16);
  const b = Number.parseInt(cleaned.slice(4, 6), 16);
  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
}

function parseTimestamp(value) {
  const raw = String(value || "").trim();
  if (!raw) return null;
  const parsed = Date.parse(raw);
  return Number.isNaN(parsed) ? null : parsed;
}

function normalizeNode(node) {
  return {
    ...node,
    x: sanitizeMetric(node.x),
    y: sanitizeMetric(node.y),
    z: sanitizeMetric(node.z),
    size: sanitizeMetric(node.size) || 4,
    label: node.label || titleCase(node.id || "Node"),
    domain: node.domain || "core",
    kind: node.kind || "node",
    color: node.color || "#9fb3ff",
  };
}

function buildNodeMap(nodes) {
  return new Map(nodes.map((node) => [String(node.id), node]));
}

function buildAdjacency(links) {
  const adjacency = new Map();
  links.forEach((link) => {
    const source = String(link.source);
    const target = String(link.target);
    if (!adjacency.has(source)) adjacency.set(source, new Set());
    if (!adjacency.has(target)) adjacency.set(target, new Set());
    adjacency.get(source).add(target);
    adjacency.get(target).add(source);
  });
  return adjacency;
}

function setIntersection(left, right) {
  return new Set([...left].filter((item) => right.has(item)));
}

function isCausalKind(kind) {
  const normalized = String(kind || "");
  return CAUSAL_LINK_PREFIXES.some((prefix) => normalized.startsWith(prefix));
}

function isDetailVisible(node, detailMode) {
  if (detailMode === "overview") return OVERVIEW_KINDS.has(node.kind);
  if (detailMode === "no_chunks") return node.kind !== "chunk";
  if (detailMode === "core_only") return CORE_KINDS.has(node.kind);
  return true;
}

function drillDepth(level, viewMode) {
  if (viewMode === "timeline") {
    if (level === "chunk") return 1;
    if (level === "note") return 2;
    return 3;
  }
  if (level === "domain") return 2;
  if (level === "topic") return 2;
  if (level === "note") return 2;
  if (level === "chunk") return 1;
  return 3;
}

function deriveDrillSeeds(filters, nodeMap, nodes) {
  const selectedId = filters.focusNodeId && nodeMap.has(filters.focusNodeId) ? filters.focusNodeId : null;
  const selectedNode = selectedId ? nodeMap.get(selectedId) : null;
  const seeds = new Set();
  if (selectedNode) {
    if (filters.drillLevel === "domain") {
      seeds.add(selectedNode.kind === "domain" ? selectedId : `domain:${selectedNode.domain}`);
    } else {
      seeds.add(selectedId);
    }
  } else if (filters.domains.size > 0 && filters.drillLevel !== "overview") {
    filters.domains.forEach((domain) => {
      const domainId = `domain:${domain}`;
      if (nodeMap.has(domainId)) seeds.add(domainId);
    });
  }
  if (!seeds.size && filters.viewMode === "causal") {
    nodes.forEach((node) => {
      if (node.kind === "topic" || node.kind === "pack") seeds.add(String(node.id));
    });
  }
  return seeds;
}

function neighborsOf(nodeId, payload, nodeMap) {
  const neighbors = [];
  (payload?.links || []).forEach((link) => {
    const source = String(link.source);
    const target = String(link.target);
    if (source === nodeId && nodeMap.has(target)) neighbors.push(nodeMap.get(target));
    if (target === nodeId && nodeMap.has(source)) neighbors.push(nodeMap.get(source));
  });
  return neighbors;
}

function firstNeighborByKind(nodeId, kinds, payload, nodeMap) {
  const kindSet = new Set(kinds);
  return neighborsOf(nodeId, payload, nodeMap).find((neighbor) => kindSet.has(neighbor.kind)) || null;
}

function deriveDrillLevelForNode(node) {
  if (!node) return "overview";
  if (node.kind === "domain") return "domain";
  if (node.kind === "topic") return "topic";
  if (node.kind === "note") return "note";
  if (node.kind === "chunk") return "chunk";
  return "overview";
}

function deriveSelectionTrail(payload, selectedNodeId) {
  if (!payload || !selectedNodeId) return [];
  const nodes = (payload.nodes || []).map(normalizeNode);
  const nodeMap = buildNodeMap(nodes);
  const selected = nodeMap.get(selectedNodeId);
  if (!selected) return [];
  const trail = [];
  const push = (node) => {
    if (!node) return;
    if (trail.some((item) => item.id === node.id)) return;
    trail.push({ id: node.id, label: node.label, kind: node.kind, domain: node.domain, bucket: node.details?.bucket || "" });
  };

  push(nodeMap.get("brain"));
  if (selected.kind === "timeline") {
    push(selected);
    return trail;
  }

  const domainNode = selected.kind === "domain" ? selected : nodeMap.get(`domain:${selected.domain}`);
  if (domainNode && domainNode.id !== "brain") push(domainNode);

  let topicNode = null;
  let noteNode = null;

  if (selected.kind === "topic") topicNode = selected;
  if (selected.kind === "note") {
    noteNode = selected;
    topicNode = firstNeighborByKind(selected.id, ["topic"], payload, nodeMap);
  }
  if (selected.kind === "chunk") {
    noteNode = firstNeighborByKind(selected.id, ["note"], payload, nodeMap);
    topicNode = firstNeighborByKind(selected.id, ["topic"], payload, nodeMap)
      || (noteNode ? firstNeighborByKind(noteNode.id, ["topic"], payload, nodeMap) : null);
  }
  if (selected.kind === "publication") {
    topicNode = firstNeighborByKind(selected.id, ["topic"], payload, nodeMap);
    noteNode = firstNeighborByKind(selected.id, ["note"], payload, nodeMap);
  }
  if (selected.kind === "pack") {
    topicNode = firstNeighborByKind(selected.id, ["topic"], payload, nodeMap);
  }
  if (selected.kind === "outcome" || selected.kind === "episode" || selected.kind === "run") {
    const packNode = firstNeighborByKind(selected.id, ["pack"], payload, nodeMap);
    topicNode = packNode ? firstNeighborByKind(packNode.id, ["topic"], payload, nodeMap) : null;
  }

  if (topicNode) push(topicNode);
  if (noteNode) push(noteNode);
  if (selected.kind !== "brain" && selected.kind !== "domain" && selected.kind !== "topic" && selected.kind !== "note") push(selected);
  if (!trail.length || trail[trail.length - 1]?.id !== selected.id) push(selected);
  return trail;
}

function getNodeTimestamp(node) {
  if (!node) return null;
  const details = node.details || {};
  if (node.kind === "chunk") return parseTimestamp(details.published_on);
  if (node.kind === "outcome") return parseTimestamp(details.ts);
  if (node.kind === "episode") return parseTimestamp(details.ts_end || details.ts_start);
  if (node.kind === "run") return parseTimestamp(details.ts_updated || details.ts_started || details.ts_completed);
  if (node.kind === "timeline") return null;
  return null;
}

function computePlaybackBounds(nodes) {
  const values = nodes
    .map((node) => getNodeTimestamp(node))
    .filter((value) => Number.isFinite(value))
    .sort((left, right) => left - right);
  if (!values.length) {
    const now = Date.now();
    return { min: now, max: now, cutoff: now };
  }
  const min = values[0];
  const max = values[values.length - 1];
  const ratio = clamp(graphProState.filters.playbackPercent / 100, 0, 1);
  const cutoff = min + (max - min) * ratio;
  return { min, max, cutoff };
}

function formatPlaybackDate(value) {
  if (!Number.isFinite(value)) return "No dated activity";
  return new Date(value).toLocaleDateString(undefined, { year: "numeric", month: "short", day: "numeric" });
}

function startPlayback() {
  if (graphProState.playbackTimer) return;
  graphProState.playbackTimer = window.setInterval(() => {
    const next = graphProState.filters.playbackPercent >= 100 ? 0 : Math.min(100, graphProState.filters.playbackPercent + 6);
    graphProState.filters.playbackPercent = next;
    applyGraphProFilters();
    if (next >= 100) stopPlayback();
  }, 360);
}

function stopPlayback() {
  if (!graphProState.playbackTimer) return;
  window.clearInterval(graphProState.playbackTimer);
  graphProState.playbackTimer = null;
}

function applySelectionFocus(node, mode = "expand") {
  if (!node) return;
  graphProState.selectedNodeId = node.id;
  graphProState.filters.focusNodeId = node.id;
  if (node.domain && node.domain !== "core") {
    graphProState.filters.domains = new Set([node.domain]);
  }

  if (mode === "timeline" || node.kind === "timeline") {
    graphProState.filters.viewMode = "timeline";
    graphProState.filters.timelineBucket = node.details?.bucket || graphProState.filters.timelineBucket || "all";
    graphProState.filters.drillLevel = "overview";
    applyGraphProFilters();
    return;
  }

  if (mode === "causal" || node.kind === "publication") {
    graphProState.filters.viewMode = "causal";
  } else {
    graphProState.filters.viewMode = "topology";
  }
  graphProState.filters.drillLevel = deriveDrillLevelForNode(node);
  if (node.kind === "chunk") {
    graphProState.filters.detail = "all";
  }
  applyGraphProFilters();
}

function focusParentTrailStep() {
  const trail = deriveSelectionTrail(graphProState.payload, graphProState.selectedNodeId);
  if (trail.length < 2) return;
  const parent = trail[trail.length - 2];
  if (!parent) return;
  const node = graphProState.payload?.nodes?.find((item) => item.id === parent.id);
  if (!node) return;
  applySelectionFocus(normalizeNode(node), parent.kind === "timeline" ? "timeline" : "expand");
}

function contextualizeIds(seedIds, adjacency, nodeMap, detailMode) {
  const contextualIds = new Set(seedIds);
  seedIds.forEach((id) => {
    const node = nodeMap.get(id);
    if (!node) return;
    const neighbors = adjacency.get(id) || new Set();
    neighbors.forEach((neighborId) => {
      const neighbor = nodeMap.get(neighborId);
      if (!neighbor) return;
      if (neighbor.kind === "brain" || neighbor.kind === "domain" || neighbor.kind === "timeline") contextualIds.add(neighborId);
      if (detailMode !== "overview") {
        if (node.kind === "chunk" && ["note", "publication", "topic", "timeline"].includes(neighbor.kind)) contextualIds.add(neighborId);
        if (node.kind === "publication" && ["chunk", "domain", "topic", "note"].includes(neighbor.kind)) contextualIds.add(neighborId);
        if (node.kind === "topic" && ["pack", "publication", "note"].includes(neighbor.kind)) contextualIds.add(neighborId);
      }
    });
    if (node.domain && nodeMap.has(`domain:${node.domain}`)) contextualIds.add(`domain:${node.domain}`);
  });
  contextualIds.add("brain");
  return contextualIds;
}

function bfsClosure(startIds, adjacency, depth = 2) {
  const visited = new Set(startIds);
  const queue = [...startIds].map((id) => ({ id, depth: 0 }));
  while (queue.length) {
    const current = queue.shift();
    if (!current || current.depth >= depth) continue;
    const neighbors = adjacency.get(current.id);
    if (!neighbors) continue;
    neighbors.forEach((neighbor) => {
      if (visited.has(neighbor)) return;
      visited.add(neighbor);
      queue.push({ id: neighbor, depth: current.depth + 1 });
    });
  }
  return visited;
}

function getVisibleData(payload, filters) {
  if (!payload) return { nodes: [], links: [] };
  const nodes = (payload.nodes || []).map(normalizeNode);
  const links = (payload.links || []).map((link) => ({
    ...link,
    source: String(link.source),
    target: String(link.target),
  }));
  const nodeMap = buildNodeMap(nodes);
  const adjacency = buildAdjacency(links);
  const timelineLinks = links.filter(
    (link) =>
      TIMELINE_LINK_KINDS.has(String(link.kind || "")) ||
      nodeMap.get(link.source)?.kind === "timeline" ||
      nodeMap.get(link.target)?.kind === "timeline",
  );
  const timelineRenderLinks = links.filter((link) => {
    const kind = String(link.kind || "");
    return (
      TIMELINE_LINK_KINDS.has(kind) ||
      ["note_chunk", "publication_chunk", "topic_chunk", "publication_note", "publication_topic", "primary_note"].includes(kind)
    );
  });
  const timelineAdjacency = buildAdjacency(timelineLinks);
  const causalLinks = links.filter((link) => isCausalKind(link.kind));
  const causalAdjacency = buildAdjacency(causalLinks);
  const playbackBounds = computePlaybackBounds(nodes);

  const domainFilterActive = filters.domains.size > 0;
  const kindFilterActive = filters.kinds.size > 0;
  const sourceFilterActive = filters.source && filters.source !== "all";
  const detailMode = filters.detail || "all";
  const viewMode = filters.viewMode || "topology";

  let baseVisibleIds = new Set();
  nodes.forEach((node) => {
    if (!isDetailVisible(node, detailMode)) return;
    if (domainFilterActive && !filters.domains.has(node.domain)) return;
    if (kindFilterActive && !filters.kinds.has(node.kind)) return;
    const timestamp = getNodeTimestamp(node);
    if (timestamp && timestamp > playbackBounds.cutoff) return;
    baseVisibleIds.add(String(node.id));
  });

  if (sourceFilterActive) {
    const sourceSeeds = new Set();
    nodes.forEach((node) => {
      const details = node.details || {};
      if (node.kind === "publication" && node.label === filters.source) sourceSeeds.add(String(node.id));
      if (String(details.source || "") === filters.source) sourceSeeds.add(String(node.id));
    });
    const sourceContext = bfsClosure(sourceSeeds, adjacency, 3);
    baseVisibleIds = new Set([...baseVisibleIds].filter((id) => sourceContext.has(id)));
  }

  let visibleIds = new Set(baseVisibleIds);
  let activeAdjacency = adjacency;
  let activeLinks = links;

  if (viewMode === "timeline") {
    activeAdjacency = timelineAdjacency;
    activeLinks = timelineRenderLinks;
    const timelineSeeds = new Set();
    nodes.forEach((node) => {
      if (node.kind !== "timeline") return;
      const bucket = node.details?.bucket || "";
      if (filters.timelineBucket === "all" || bucket === filters.timelineBucket) timelineSeeds.add(String(node.id));
    });
    if (filters.focusNodeId && nodeMap.has(filters.focusNodeId)) timelineSeeds.add(filters.focusNodeId);
    const closure = bfsClosure(timelineSeeds, timelineAdjacency, filters.timelineBucket === "all" ? 2 : 3);
    visibleIds = setIntersection(baseVisibleIds, closure);
    timelineSeeds.forEach((id) => visibleIds.add(id));
  } else if (viewMode === "causal") {
    activeAdjacency = causalAdjacency;
    activeLinks = causalLinks;
    const causalNodeIds = new Set();
    causalLinks.forEach((link) => {
      causalNodeIds.add(link.source);
      causalNodeIds.add(link.target);
    });
    visibleIds = setIntersection(baseVisibleIds, causalNodeIds);
    const drillSeeds = deriveDrillSeeds(filters, nodeMap, nodes);
    if (drillSeeds.size > 0) {
      const closure = bfsClosure(drillSeeds, causalAdjacency, drillDepth(filters.drillLevel, viewMode));
      visibleIds = setIntersection(visibleIds, closure);
      drillSeeds.forEach((id) => visibleIds.add(id));
    }
  } else if (filters.drillLevel !== "overview") {
    const drillSeeds = deriveDrillSeeds(filters, nodeMap, nodes);
    if (drillSeeds.size > 0) {
      const closure = bfsClosure(drillSeeds, adjacency, drillDepth(filters.drillLevel, viewMode));
      visibleIds = setIntersection(baseVisibleIds, closure);
      drillSeeds.forEach((id) => visibleIds.add(id));
    }
  }

  const contextualIds = contextualizeIds(visibleIds, adjacency, nodeMap, detailMode);

  const filteredNodes = nodes.filter((node) => contextualIds.has(String(node.id)));
  const filteredIds = new Set(filteredNodes.map((node) => String(node.id)));
  const filteredLinks = activeLinks.filter((link) => filteredIds.has(link.source) && filteredIds.has(link.target));
  return { nodes: filteredNodes, links: filteredLinks };
}

function filterCounts(data) {
  return {
    nodes: data.nodes.length,
    links: data.links.length,
    chunks: data.nodes.filter((node) => node.kind === "chunk").length,
    publications: data.nodes.filter((node) => node.kind === "publication").length,
    timelines: data.nodes.filter((node) => node.kind === "timeline").length,
  };
}

function detailModeLabel(mode) {
  if (mode === "overview") return "Overview";
  if (mode === "no_chunks") return "No chunks";
  if (mode === "core_only") return "Core only";
  return "All nodes";
}

function viewModeLabel(mode) {
  if (mode === "timeline") return "Timeline";
  if (mode === "causal") return "Causal";
  return "Topology";
}

function drillLevelLabel(level) {
  if (level === "domain") return "Domain";
  if (level === "topic") return "Topic";
  if (level === "note") return "Note";
  if (level === "chunk") return "Chunk";
  return "Overview";
}

function renderFilters() {
  if (!graphProFilters || !graphProState.payload) return;
  const payload = graphProState.payload;
  const counts = filterCounts(graphProState.filteredPayload);
  const domains = payload.filters?.domains || [];
  const kinds = payload.filters?.kinds || [];
  const sources = payload.filters?.sources || [];
  const detailModes = ["overview", ...(payload.filters?.detail_modes || ["all"]).filter((mode) => mode !== "overview")];
  const viewModes = payload.filters?.view_modes || ["topology"];
  const drillLevels = payload.filters?.drill_levels || ["overview"];
  const timelineBuckets = payload.filters?.timeline_buckets || ["all"];
  const selectedNode = graphProState.filteredPayload.nodes.find((node) => node.id === graphProState.selectedNodeId)
    || graphProState.payload.nodes.find((node) => node.id === graphProState.selectedNodeId);
  const selectionTrail = deriveSelectionTrail(graphProState.payload, graphProState.selectedNodeId);
  const playbackBounds = computePlaybackBounds((payload.nodes || []).map(normalizeNode));

  graphProFilters.innerHTML = `
    <div class="graph-pro-filter-grid">
      <div class="graph-pro-group">
        <span class="graph-pro-label">Visible Graph</span>
        <div class="graph-pro-chips">
          <span class="graph-pro-pill">${counts.nodes} nodes</span>
          <span class="graph-pro-pill">${counts.links} links</span>
          <span class="graph-pro-pill">${counts.chunks} chunks</span>
          <span class="graph-pro-pill">${counts.publications} publications</span>
          <span class="graph-pro-pill">${counts.timelines} timelines</span>
        </div>
      </div>
      <div class="graph-pro-group">
        <span class="graph-pro-label">View Mode</span>
        <div class="graph-pro-chips">
          ${viewModes
            .map(
              (mode) => `
                <button type="button" class="graph-pro-chip ${
                  graphProState.filters.viewMode === mode ? "is-active" : ""
                }" data-filter-type="view" data-filter-value="${escapeHtml(mode)}">
                  ${escapeHtml(viewModeLabel(mode))}
                </button>
              `,
            )
            .join("")}
        </div>
      </div>
      <div class="graph-pro-group">
        <span class="graph-pro-label">Domain Lens</span>
        <div class="graph-pro-chips">
          ${domains
            .map(
              (domain) => `
                <button type="button" class="graph-pro-chip ${
                  graphProState.filters.domains.has(domain) ? "is-active" : ""
                }" data-filter-type="domain" data-filter-value="${escapeHtml(domain)}">
                  ${escapeHtml(titleCase(domain))}
                </button>
              `,
            )
            .join("")}
        </div>
      </div>
      <div class="graph-pro-group">
        <span class="graph-pro-label">Node Mapping</span>
        <div class="graph-pro-chips">
          ${kinds
            .map(
              (kind) => `
                <button type="button" class="graph-pro-chip ${
                  graphProState.filters.kinds.has(kind) ? "is-active" : ""
                }" data-filter-type="kind" data-filter-value="${escapeHtml(kind)}">
                  ${escapeHtml(titleCase(kind))}
                </button>
              `,
            )
            .join("")}
        </div>
      </div>
      <div class="graph-pro-group">
        <span class="graph-pro-label">Drill-Down</span>
        <div class="graph-pro-toolbar">
          <select class="graph-pro-select" id="graphProDrillSelect">
            ${drillLevels
              .map(
                (level) => `
                  <option value="${escapeHtml(level)}" ${
                    graphProState.filters.drillLevel === level ? "selected" : ""
                  }>
                    ${escapeHtml(drillLevelLabel(level))}
                  </option>
                `,
              )
              .join("")}
          </select>
          <select class="graph-pro-select" id="graphProTimelineSelect" ${
            graphProState.filters.viewMode === "timeline" ? "" : "disabled"
          }>
            ${timelineBuckets
              .map(
                (bucket) => `
                  <option value="${escapeHtml(bucket)}" ${
                    graphProState.filters.timelineBucket === bucket ? "selected" : ""
                  }>
                    ${escapeHtml(bucket === "all" ? "All time buckets" : bucket)}
                  </option>
                `,
              )
              .join("")}
          </select>
        </div>
      </div>
      <div class="graph-pro-group">
        <span class="graph-pro-label">Playback</span>
        <div class="graph-pro-toolbar">
          <input
            type="range"
            min="0"
            max="100"
            step="1"
            value="${Math.round(graphProState.filters.playbackPercent)}"
            id="graphProPlaybackRange"
            class="graph-pro-range"
          />
          <span class="graph-pro-pill">${formatPlaybackDate(playbackBounds.min)} -> ${formatPlaybackDate(playbackBounds.cutoff)}</span>
          <button type="button" class="graph-pro-reset" id="graphProPlaybackToggle">
            ${graphProState.playbackTimer ? "Pause" : "Play"}
          </button>
          <button type="button" class="graph-pro-reset" id="graphProPlaybackFull">Full History</button>
        </div>
      </div>
      <div class="graph-pro-group">
        <span class="graph-pro-label">Enterprise Controls</span>
        <div class="graph-pro-toolbar">
          <select class="graph-pro-select" id="graphProSourceSelect">
            <option value="all">All sources</option>
            ${sources
              .map(
                (source) => `
                  <option value="${escapeHtml(source)}" ${
                    graphProState.filters.source === source ? "selected" : ""
                  }>
                    ${escapeHtml(source)}
                  </option>
                `,
              )
              .join("")}
          </select>
          <select class="graph-pro-select" id="graphProDetailSelect">
            ${detailModes
              .map(
                (mode) => `
                  <option value="${escapeHtml(mode)}" ${
                    graphProState.filters.detail === mode ? "selected" : ""
                  }>
                    ${escapeHtml(detailModeLabel(mode))}
                  </option>
                `,
              )
              .join("")}
          </select>
          <button type="button" class="graph-pro-reset" id="graphProFitButton">Fit Scene</button>
          <button type="button" class="graph-pro-reset" id="graphProResetButton">Reset Filters</button>
        </div>
      </div>
      <div class="graph-pro-group">
        <span class="graph-pro-label">Focus</span>
        <div class="graph-pro-chips">
          <span class="graph-pro-pill">${escapeHtml(selectedNode ? selectedNode.label : "No node selected")}</span>
          ${
            selectedNode
              ? `
                <button type="button" class="graph-pro-reset" id="graphProExpandFocusButton">Expand Selection</button>
                <button type="button" class="graph-pro-reset" id="graphProTimelineFocusButton">Timeline Lens</button>
                <button type="button" class="graph-pro-reset" id="graphProCausalFocusButton">Causal Lens</button>
                <button type="button" class="graph-pro-reset" id="graphProUpButton">Go Up</button>
                <button type="button" class="graph-pro-reset" id="graphProClearFocusButton">Clear Focus</button>
              `
              : ""
          }
        </div>
      </div>
      <div class="graph-pro-group">
        <span class="graph-pro-label">Navigation Path</span>
        <div class="graph-pro-chips">
          ${
            selectionTrail.length
              ? selectionTrail
                  .map(
                    (item) => `
                      <button type="button" class="graph-pro-chip ${
                        item.id === graphProState.selectedNodeId ? "is-active" : ""
                      }" data-filter-type="trail" data-filter-value="${escapeHtml(item.id)}">
                        ${escapeHtml(item.label)}
                      </button>
                    `,
                  )
                  .join("")
              : '<span class="graph-pro-pill">Global overview</span>'
          }
        </div>
      </div>
    </div>
  `;

  graphProFilters.querySelectorAll("[data-filter-type='view']").forEach((button) => {
    button.addEventListener("click", () => {
      graphProState.filters.viewMode = button.getAttribute("data-filter-value") || "topology";
      applyGraphProFilters();
    });
  });
  graphProFilters.querySelectorAll("[data-filter-type='domain']").forEach((button) => {
    button.addEventListener("click", () => {
      const value = button.getAttribute("data-filter-value") || "";
      if (graphProState.filters.domains.has(value)) graphProState.filters.domains.delete(value);
      else graphProState.filters.domains.add(value);
      applyGraphProFilters();
    });
  });
  graphProFilters.querySelectorAll("[data-filter-type='kind']").forEach((button) => {
    button.addEventListener("click", () => {
      const value = button.getAttribute("data-filter-value") || "";
      if (graphProState.filters.kinds.has(value)) graphProState.filters.kinds.delete(value);
      else graphProState.filters.kinds.add(value);
      applyGraphProFilters();
    });
  });
  graphProFilters.querySelectorAll("[data-filter-type='trail']").forEach((button) => {
    button.addEventListener("click", () => {
      const value = button.getAttribute("data-filter-value") || "";
      const node = graphProState.payload?.nodes?.find((item) => item.id === value);
      if (!node) return;
      applySelectionFocus(normalizeNode(node), node.kind === "timeline" ? "timeline" : "expand");
    });
  });

  document.getElementById("graphProSourceSelect")?.addEventListener("change", (event) => {
    graphProState.filters.source = event.target.value || "all";
    applyGraphProFilters();
  });
  document.getElementById("graphProDetailSelect")?.addEventListener("change", (event) => {
    graphProState.filters.detail = event.target.value || "all";
    applyGraphProFilters();
  });
  document.getElementById("graphProDrillSelect")?.addEventListener("change", (event) => {
    graphProState.filters.drillLevel = event.target.value || "overview";
    applyGraphProFilters();
  });
  document.getElementById("graphProTimelineSelect")?.addEventListener("change", (event) => {
    graphProState.filters.timelineBucket = event.target.value || "all";
    applyGraphProFilters();
  });
  document.getElementById("graphProPlaybackRange")?.addEventListener("input", (event) => {
    stopPlayback();
    graphProState.filters.playbackPercent = Number(event.target.value || 100);
    applyGraphProFilters();
  });
  document.getElementById("graphProPlaybackToggle")?.addEventListener("click", () => {
    if (graphProState.playbackTimer) stopPlayback();
    else startPlayback();
    renderFilters();
  });
  document.getElementById("graphProPlaybackFull")?.addEventListener("click", () => {
    stopPlayback();
    graphProState.filters.playbackPercent = 100;
    applyGraphProFilters();
  });
  document.getElementById("graphProResetButton")?.addEventListener("click", () => {
    stopPlayback();
    graphProState.filters.domains.clear();
    graphProState.filters.kinds.clear();
    graphProState.filters.source = "all";
    graphProState.filters.detail = "overview";
    graphProState.filters.viewMode = "topology";
    graphProState.filters.drillLevel = "overview";
    graphProState.filters.timelineBucket = "all";
    graphProState.filters.focusNodeId = null;
    graphProState.filters.playbackPercent = 100;
    graphProState.selectedNodeId = null;
    fitGraphProCamera();
    applyGraphProFilters();
  });
  document.getElementById("graphProFitButton")?.addEventListener("click", () => {
    fitGraphProCamera();
  });
  document.getElementById("graphProClearFocusButton")?.addEventListener("click", () => {
    graphProState.filters.focusNodeId = null;
    graphProState.selectedNodeId = null;
    applyGraphProFilters();
  });
  document.getElementById("graphProExpandFocusButton")?.addEventListener("click", () => {
    if (!selectedNode) return;
    applySelectionFocus(normalizeNode(selectedNode), "expand");
  });
  document.getElementById("graphProTimelineFocusButton")?.addEventListener("click", () => {
    if (!selectedNode) return;
    applySelectionFocus(normalizeNode(selectedNode), "timeline");
  });
  document.getElementById("graphProCausalFocusButton")?.addEventListener("click", () => {
    if (!selectedNode) return;
    applySelectionFocus(normalizeNode(selectedNode), "causal");
  });
  document.getElementById("graphProUpButton")?.addEventListener("click", () => {
    focusParentTrailStep();
  });
}

function fitGraphProCamera() {
  graphProState.rotationY = 0.42;
  graphProState.rotationX = -0.18;
  graphProState.targetRotationY = 0.42;
  graphProState.targetRotationX = -0.18;
  graphProState.zoom = 1.04;
  graphProState.targetZoom = 1.04;
}

function ensureGraphCanvas() {
  if (graphProState.ready) return;
  graphProLayer.innerHTML = "";
  const canvas = document.createElement("canvas");
  canvas.className = "graph-pro-canvas";
  graphProLayer.appendChild(canvas);
  graphProState.canvas = canvas;
  graphProState.ctx = canvas.getContext("2d");
  graphProState.resizeObserver = new ResizeObserver(() => resizeGraphCanvas());
  graphProState.resizeObserver.observe(graphProLayer);
  resizeGraphCanvas();

  canvas.addEventListener("mousemove", handlePointerMove);
  canvas.addEventListener("mousedown", handlePointerDown);
  canvas.addEventListener("click", handleGraphClick);
  canvas.addEventListener(
    "wheel",
    (event) => {
      event.preventDefault();
      graphProState.targetZoom = clamp(graphProState.targetZoom + Math.sign(event.deltaY) * 0.08, 0.48, 2.3);
    },
    { passive: false },
  );
  window.addEventListener("mouseup", handlePointerUp);

  graphProState.ready = true;
  graphProState.status = "Loading Graph Pro...";
  if (!graphProState.animationFrame) graphProState.animationFrame = requestAnimationFrame(renderLoop);
}

function resizeGraphCanvas() {
  if (!graphProState.canvas || !graphProState.ctx) return;
  const rect = graphProLayer.getBoundingClientRect();
  const ratio = window.devicePixelRatio || 1;
  graphProState.canvas.width = Math.floor(rect.width * ratio);
  graphProState.canvas.height = Math.floor(rect.height * ratio);
  graphProState.canvas.style.width = `${rect.width}px`;
  graphProState.canvas.style.height = `${rect.height}px`;
  graphProState.ctx.setTransform(ratio, 0, 0, ratio, 0, 0);
}

function handlePointerMove(event) {
  if (!graphProState.canvas) return;
  const pointer = getRelativePointer(event);
  if (graphProState.dragging && graphProState.lastPointer) {
    const dx = pointer.x - graphProState.lastPointer.x;
    const dy = pointer.y - graphProState.lastPointer.y;
    graphProState.targetRotationY += dx * 0.0044;
    graphProState.targetRotationX = clamp(graphProState.targetRotationX + dy * 0.0032, -0.9, 0.55);
    graphProState.lastPointer = pointer;
    return;
  }
  const hovered = nearestProjectedNode(pointer);
  graphProState.hoveredNodeId = hovered?.id || null;
  graphProLayer.style.cursor = hovered ? "pointer" : "grab";
}

function handlePointerDown(event) {
  graphProState.dragging = true;
  graphProState.lastPointer = getRelativePointer(event);
  graphProLayer.style.cursor = "grabbing";
}

function handlePointerUp() {
  graphProState.dragging = false;
  graphProState.lastPointer = null;
  graphProLayer.style.cursor = graphProState.hoveredNodeId ? "pointer" : "grab";
}

function handleGraphClick(event) {
  const pointer = getRelativePointer(event);
  const node = nearestProjectedNode(pointer);
  if (!node) return;
  applySelectionFocus(node, node.kind === "timeline" ? "timeline" : "expand");
  window.dispatchEvent(
    new CustomEvent("graph-node-selected", {
      detail: { node },
    }),
  );
}

function getRelativePointer(event) {
  const rect = graphProState.canvas.getBoundingClientRect();
  return {
    x: event.clientX - rect.left,
    y: event.clientY - rect.top,
  };
}

function nearestProjectedNode(pointer) {
  let nearest = null;
  let minDistance = Infinity;
  graphProState.projectedNodes.forEach((node) => {
    const dx = pointer.x - node.screenX;
    const dy = pointer.y - node.screenY;
    const distance = Math.sqrt(dx * dx + dy * dy);
    const hit = Math.max(10, node.radius + 4);
    if (distance < hit && distance < minDistance) {
      minDistance = distance;
      nearest = node;
    }
  });
  return nearest;
}

function transformNode(node, width, height) {
  const frame = graphProState.frame || { centerX: 0, centerY: 0, centerZ: 0, fit: 1 };
  const cosY = Math.cos(graphProState.rotationY);
  const sinY = Math.sin(graphProState.rotationY);
  const cosX = Math.cos(graphProState.rotationX);
  const sinX = Math.sin(graphProState.rotationX);

  const spreadX = 1.32;
  const spreadY = 0.88;
  const spreadZ = 1.28;
  const baseX = (node.x - frame.centerX) * frame.fit * spreadX;
  const baseY = (node.y - frame.centerY) * frame.fit * spreadY;
  const baseZ = (node.z - frame.centerZ) * frame.fit * spreadZ;

  const x1 = baseX * cosY - baseZ * sinY;
  const z1 = baseX * sinY + baseZ * cosY;
  const y1 = baseY * cosX - z1 * sinX;
  const z2 = baseY * sinX + z1 * cosX;
  const perspective = 780 / (780 + z2 + 380);
  const screenX = width / 2 + x1 * perspective * graphProState.zoom;
  const screenY = height * 0.42 + y1 * perspective * graphProState.zoom;
  const radius = Math.max(1.8, node.size * 0.7 * perspective * graphProState.zoom);
  return {
    ...node,
    depth: z2,
    perspective,
    screenX,
    screenY,
    radius,
  };
}

function computeGraphFrame(nodes) {
  if (!nodes.length) {
    return { centerX: 0, centerY: 0, centerZ: 0, fit: 1 };
  }
  let minX = Infinity;
  let minY = Infinity;
  let minZ = Infinity;
  let maxX = -Infinity;
  let maxY = -Infinity;
  let maxZ = -Infinity;
  nodes.forEach((node) => {
    minX = Math.min(minX, node.x);
    minY = Math.min(minY, node.y);
    minZ = Math.min(minZ, node.z);
    maxX = Math.max(maxX, node.x);
    maxY = Math.max(maxY, node.y);
    maxZ = Math.max(maxZ, node.z);
  });
  const spread = Math.max(maxX - minX, maxY - minY, maxZ - minZ, 360);
  return {
    centerX: (minX + maxX) / 2,
    centerY: (minY + maxY) / 2,
    centerZ: (minZ + maxZ) / 2,
    fit: clamp(620 / spread, 0.6, 2.4),
  };
}

function drawBackground(ctx, width, height) {
  const bg = ctx.createRadialGradient(width * 0.52, height * 0.45, 40, width * 0.52, height * 0.45, height * 0.9);
  bg.addColorStop(0, "rgba(39, 57, 128, 0.24)");
  bg.addColorStop(0.55, "rgba(8, 11, 22, 0.82)");
  bg.addColorStop(1, "rgba(4, 6, 12, 1)");
  ctx.fillStyle = bg;
  ctx.fillRect(0, 0, width, height);

  ctx.save();
  ctx.strokeStyle = "rgba(103, 116, 168, 0.08)";
  ctx.lineWidth = 1;
  for (let x = 0; x < width; x += 40) {
    ctx.beginPath();
    ctx.moveTo(x + 0.5, 0);
    ctx.lineTo(x + 0.5, height);
    ctx.stroke();
  }
  for (let y = 0; y < height; y += 40) {
    ctx.beginPath();
    ctx.moveTo(0, y + 0.5);
    ctx.lineTo(width, y + 0.5);
    ctx.stroke();
  }
  ctx.restore();
}

function drawStars(ctx, width, height, timestamp) {
  graphProState.stars.forEach((star, index) => {
    const shift = ((timestamp * 0.00004 * (1 + (index % 5))) % 1) * 2 - 1;
    const depth = 700 / (700 + star.z + 800);
    const x = width / 2 + (star.x + shift * 80) * depth;
    const y = height / 2 + star.y * depth;
    if (x < -30 || x > width + 30 || y < -30 || y > height + 30) return;
    ctx.save();
    ctx.globalAlpha = star.alpha * depth;
    ctx.fillStyle = "rgba(182, 202, 255, 0.9)";
    ctx.beginPath();
    ctx.arc(x, y, star.size * depth, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  });
}

function linkGradient(ctx, link, source, target) {
  const gradient = ctx.createLinearGradient(source.screenX, source.screenY, target.screenX, target.screenY);
  gradient.addColorStop(0, rgba(source.color, 0.12));
  gradient.addColorStop(0.5, link.color || "rgba(151, 170, 255, 0.28)");
  gradient.addColorStop(1, rgba(target.color, 0.12));
  return gradient;
}

function renderLinks(ctx, links, nodeMap, timestamp) {
  links.forEach((link, index) => {
    const source = nodeMap.get(String(link.source));
    const target = nodeMap.get(String(link.target));
    if (!source || !target) return;
    const alpha = clamp((source.perspective + target.perspective) * 0.22, 0.08, 0.46);
    ctx.save();
    ctx.strokeStyle = linkGradient(ctx, link, source, target);
    ctx.globalAlpha = alpha;
    ctx.lineWidth = Math.max(0.6, sanitizeMetric(link.weight) * 1.45 * Math.min(source.perspective, target.perspective));
    ctx.beginPath();
    const controlX = (source.screenX + target.screenX) / 2;
    const controlY = (source.screenY + target.screenY) / 2 - (source.radius + target.radius) * 0.9;
    ctx.moveTo(source.screenX, source.screenY);
    ctx.quadraticCurveTo(controlX, controlY, target.screenX, target.screenY);
    ctx.stroke();

    if (!String(link.kind || "").includes("chunk")) {
      const t = ((timestamp * 0.00022) + index * 0.07) % 1;
      const packetX = (1 - t) * (1 - t) * source.screenX + 2 * (1 - t) * t * controlX + t * t * target.screenX;
      const packetY = (1 - t) * (1 - t) * source.screenY + 2 * (1 - t) * t * controlY + t * t * target.screenY;
      ctx.fillStyle = "rgba(245, 248, 255, 0.88)";
      ctx.shadowColor = "rgba(255,255,255,0.6)";
      ctx.shadowBlur = 16;
      ctx.beginPath();
      ctx.arc(packetX, packetY, 1.8 + Math.max(0.8, sanitizeMetric(link.weight) * 1.1), 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();
  });
}

function drawNodeShape(ctx, node) {
  const radius = node.radius;
  const selected = node.id === graphProState.selectedNodeId;
  const hovered = node.id === graphProState.hoveredNodeId;
  const shapeScale = selected ? 1.18 : hovered ? 1.08 : 1;
  const r = radius * shapeScale;

  ctx.save();
  ctx.translate(node.screenX, node.screenY);
  ctx.shadowColor = rgba(node.color, selected ? 0.72 : 0.42);
  ctx.shadowBlur = selected ? 28 : hovered ? 22 : 14;
  ctx.fillStyle = rgba(node.color, node.kind === "chunk" ? 0.82 : 0.96);
  ctx.strokeStyle = rgba("#f4f7ff", selected ? 0.92 : 0.28);
  ctx.lineWidth = selected ? 1.8 : 1;
  ctx.beginPath();

  if (node.kind === "pack") {
    ctx.moveTo(-r, -r * 0.58);
    ctx.lineTo(r, -r * 0.58);
    ctx.lineTo(r * 0.8, r * 0.58);
    ctx.lineTo(-r * 0.8, r * 0.58);
  } else if (node.kind === "skill") {
    ctx.moveTo(0, -r);
    ctx.lineTo(r, 0);
    ctx.lineTo(0, r);
    ctx.lineTo(-r, 0);
  } else if (node.kind === "note") {
    ctx.rect(-r * 0.82, -r * 0.68, r * 1.64, r * 1.36);
  } else if (node.kind === "publication") {
    for (let index = 0; index < 6; index += 1) {
      const angle = (Math.PI / 3) * index - Math.PI / 6;
      const x = Math.cos(angle) * r;
      const y = Math.sin(angle) * r;
      if (index === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
  } else if (node.kind === "alert") {
    ctx.moveTo(0, -r);
    ctx.lineTo(r, r);
    ctx.lineTo(-r, r);
  } else {
    ctx.arc(0, 0, r, 0, Math.PI * 2);
  }
  ctx.closePath();
  ctx.fill();
  ctx.stroke();

  if (["brain", "domain", "memory_bank", "publication"].includes(node.kind)) {
    ctx.beginPath();
    ctx.lineWidth = selected ? 2.2 : 1.2;
    ctx.strokeStyle = rgba(node.color, selected ? 0.95 : 0.5);
    ctx.arc(0, 0, r * 1.45, 0, Math.PI * 2);
    ctx.stroke();
  }

  ctx.restore();
}

function shouldLabelNode(node) {
  if (node.id === graphProState.selectedNodeId || node.id === graphProState.hoveredNodeId) return true;
  const nodeCount = graphProState.filteredPayload?.nodes?.length || 0;
  if (nodeCount > 140) return ["brain", "domain"].includes(node.kind);
  if (nodeCount > 70) return ["brain", "domain", "publication", "memory_bank"].includes(node.kind);
  return ["brain", "domain", "pack", "publication", "memory_bank", "skill"].includes(node.kind);
}

function drawNodeLabel(ctx, node) {
  const text = node.label;
  ctx.save();
  ctx.font = "12px 'IBM Plex Mono', monospace";
  const width = ctx.measureText(text).width + 18;
  const height = 24;
  const x = node.screenX - width / 2;
  const y = node.screenY - node.radius - 30;
  roundedRect(ctx, x, y, width, height, 12);
  ctx.fillStyle = "rgba(7, 10, 18, 0.76)";
  ctx.fill();
  ctx.strokeStyle = rgba(node.color, 0.38);
  ctx.stroke();
  ctx.fillStyle = "#f4f7ff";
  ctx.textAlign = "center";
  ctx.textBaseline = "middle";
  ctx.fillText(text, node.screenX, y + height / 2 + 0.5);
  ctx.restore();
}

function roundedRect(ctx, x, y, width, height, radius) {
  const safe = Math.min(radius, width / 2, height / 2);
  ctx.beginPath();
  ctx.moveTo(x + safe, y);
  ctx.arcTo(x + width, y, x + width, y + height, safe);
  ctx.arcTo(x + width, y + height, x, y + height, safe);
  ctx.arcTo(x, y + height, x, y, safe);
  ctx.arcTo(x, y, x + width, y, safe);
  ctx.closePath();
}

function renderNodeDetails(ctx, width, height) {
  const selected = graphProState.filteredPayload.nodes.find((node) => node.id === graphProState.selectedNodeId);
  if (!selected) return;
  const details = selected.details || {};
  const lines = [
    selected.label,
    `${titleCase(selected.kind)} • ${titleCase(selected.domain)}`,
    details.source ? `Source: ${details.source}` : "",
    details.path ? `Path: ${details.path}` : "",
  ].filter(Boolean);

  ctx.save();
  ctx.font = "12px 'IBM Plex Mono', monospace";
  const boxWidth = Math.min(420, Math.max(...lines.map((line) => ctx.measureText(line).width)) + 28);
  const boxHeight = lines.length * 19 + 24;
  const x = 28;
  const y = 28;
  roundedRect(ctx, x, y, boxWidth, boxHeight, 16);
  ctx.fillStyle = "rgba(8, 10, 18, 0.74)";
  ctx.fill();
  ctx.strokeStyle = rgba(selected.color, 0.42);
  ctx.stroke();
  ctx.fillStyle = "#f4f7ff";
  lines.forEach((line, index) => {
    ctx.fillText(line, x + 14, y + 20 + index * 18);
  });
  ctx.restore();
}

function renderScene(timestamp) {
  if (!graphProState.ready || !graphProState.ctx || graphProState.view !== "graph-pro") return;
  const ctx = graphProState.ctx;
  const width = graphProState.canvas.clientWidth || 1;
  const height = graphProState.canvas.clientHeight || 1;

  graphProState.rotationY = lerp(graphProState.rotationY, graphProState.targetRotationY, 0.08);
  graphProState.rotationX = lerp(graphProState.rotationX, graphProState.targetRotationX, 0.08);
  graphProState.zoom = lerp(graphProState.zoom, graphProState.targetZoom, 0.12);

  if (!graphProState.dragging) {
    graphProState.targetRotationY += 0.00045;
  }

  ctx.clearRect(0, 0, width, height);
  drawBackground(ctx, width, height);
  drawStars(ctx, width, height, timestamp);

  if (!graphProState.filteredPayload.nodes.length) {
    ctx.save();
    ctx.fillStyle = "rgba(244, 246, 255, 0.84)";
    ctx.font = "600 16px 'Space Grotesk', sans-serif";
    ctx.textAlign = "center";
    ctx.fillText(graphProState.status, width / 2, height / 2);
    ctx.restore();
    return;
  }

  graphProState.frame = computeGraphFrame(graphProState.filteredPayload.nodes);
  const projectedNodes = graphProState.filteredPayload.nodes
    .map((node) => transformNode(node, width, height))
    .sort((left, right) => left.depth - right.depth);
  graphProState.projectedNodes = projectedNodes;
  const nodeMap = new Map(projectedNodes.map((node) => [String(node.id), node]));

  renderLinks(ctx, graphProState.filteredPayload.links, nodeMap, timestamp);

  projectedNodes.forEach((node) => {
    drawNodeShape(ctx, node);
  });
  projectedNodes.forEach((node) => {
    if (shouldLabelNode(node)) drawNodeLabel(ctx, node);
  });
  renderNodeDetails(ctx, width, height);
}

function renderLoop(timestamp) {
  renderScene(timestamp);
  graphProState.animationFrame = requestAnimationFrame(renderLoop);
}

function applyGraphProFilters() {
  if (!graphProState.payload) return;
  graphProState.filteredPayload = getVisibleData(graphProState.payload, graphProState.filters);
  if (graphProState.selectedNodeId) {
    const stillVisible = graphProState.filteredPayload.nodes.some((node) => node.id === graphProState.selectedNodeId);
    if (!stillVisible && graphProState.payload.nodes.some((node) => node.id === graphProState.selectedNodeId)) {
      graphProState.filteredPayload.nodes.push(
        normalizeNode(graphProState.payload.nodes.find((node) => node.id === graphProState.selectedNodeId)),
      );
    }
  }
  const focusLabel = graphProState.selectedNodeId
    ? graphProState.payload.nodes.find((node) => node.id === graphProState.selectedNodeId)?.label || graphProState.selectedNodeId
    : "global";
  const playbackBounds = computePlaybackBounds((graphProState.payload.nodes || []).map(normalizeNode));
  graphProState.status = `${viewModeLabel(graphProState.filters.viewMode)} view • ${drillLevelLabel(
    graphProState.filters.drillLevel,
  )} drill • focus ${focusLabel} • up to ${formatPlaybackDate(playbackBounds.cutoff)}`;
  renderFilters();
}

async function refreshGraphPro() {
  if (!graphProState.ready) return;
  graphProState.status = "Refreshing Graph Pro...";
  try {
    const response = await fetch(`/api/graph-pro?ts=${Date.now()}`, { cache: "no-store" });
    if (!response.ok) throw new Error(`Graph Pro API returned ${response.status}`);
    graphProState.payload = await response.json();
    graphProState.status = "Graph Pro ready";
    applyGraphProFilters();
  } catch (error) {
    graphProState.status = `Graph Pro failed: ${error?.message || String(error)}`;
  }
}

function focusQuery(query) {
  const normalized = String(query || "").trim().toLowerCase();
  if (!normalized || !graphProState.payload?.nodes?.length) return;
  const match = graphProState.payload.nodes.find((node) => {
    const haystack = [node.label, node.id, node.domain, ...(node.tags || [])].join(" ").toLowerCase();
    return haystack.includes(normalized);
  });
  if (!match) return;
  applySelectionFocus(normalizeNode(match), match.kind === "timeline" ? "timeline" : "expand");
  window.dispatchEvent(
    new CustomEvent("graph-node-selected", {
      detail: { node: match },
    }),
  );
}

function ensureGraphPro() {
  ensureGraphCanvas();
  refreshGraphPro();
}

window.addEventListener("graph-view-change", (event) => {
  graphProState.view = event.detail?.view || "hq";
  if (graphProState.view !== "graph-pro") stopPlayback();
  if (graphProState.view === "graph-pro") ensureGraphPro();
});

window.addEventListener("graph-payload", () => {
  if (graphProState.view === "graph-pro") refreshGraphPro();
});

window.addEventListener("graph-pro-search", (event) => {
  focusQuery(event.detail?.query || "");
});

const currentView = document.querySelector(".shell")?.dataset.view || "hq";
graphProState.view = currentView;
if (currentView === "graph-pro") ensureGraphPro();
