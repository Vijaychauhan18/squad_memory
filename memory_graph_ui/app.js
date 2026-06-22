const shell = document.querySelector(".shell");
const graphContainer = document.getElementById("graph");
const metricsContainer = document.getElementById("metrics");
const generatedAt = document.getElementById("generatedAt");
const refreshButton = document.getElementById("refreshButton");
const nodeSearch = document.getElementById("nodeSearch");
const liveEventStream = document.getElementById("liveEventStream");
const nodeTitle = document.getElementById("nodeTitle");
const nodeMeta = document.getElementById("nodeMeta");
const nodeDetails = document.getElementById("nodeDetails");
const nodeTags = document.getElementById("nodeTags");
const viewSwitch = document.getElementById("viewSwitch");

const meetingTitle = document.getElementById("meetingTitle");
const meetingMeta = document.getElementById("meetingMeta");
const meetingPack = document.getElementById("meetingPack");
const meetingSpeaker = document.getElementById("meetingSpeaker");
const meetingListener = document.getElementById("meetingListener");
const meetingStatus = document.getElementById("meetingStatus");
const meetingCounter = document.getElementById("meetingCounter");
const meetingProgressFill = document.getElementById("meetingProgressFill");
const meetingSvg = document.getElementById("meetingSvg");
const meetingNodes = document.getElementById("meetingNodes");
const meetingBubble = document.getElementById("meetingBubble");
const meetingAgenda = document.getElementById("meetingAgenda");
const meetingTicker = document.getElementById("meetingTicker");
const meetingTranscript = document.getElementById("meetingTranscript");
const meetingPrev = document.getElementById("meetingPrev");
const meetingPause = document.getElementById("meetingPause");
const meetingNext = document.getElementById("meetingNext");
const hqBoardLabel = document.getElementById("hqBoardLabel");
const meetingLiveCard = document.getElementById("meetingLiveCard");
const meetingRoomTicker = document.getElementById("meetingRoomTicker");
const meetingBoard = document.getElementById("meetingBoard");
const meetingPodCard = document.getElementById("meetingPodCard");
const officeCanvas = document.getElementById("officeCanvas");

const canvas = document.createElement("canvas");
graphContainer.appendChild(canvas);
const ctx = canvas.getContext("2d");
const officeCtx = officeCanvas.getContext("2d");

let latestPayload = null;
let projectedNodes = [];
let selectedNode = null;
let hoveredNode = null;
let animationFrame = null;
let rotationY = 0.18;
let rotationX = -0.22;
let targetRotationY = rotationY;
let targetRotationX = rotationX;
let zoom = 1;
let dragging = false;
let lastPointer = null;
let spinEnabled = true;

const meetingState = {
  scenarios: [],
  scenarioIndex: 0,
  turnIndex: 0,
  paused: false,
  timer: null,
  turnStartedAt: 0,
  actorPositions: {},
  camera: { x: 0, y: 0, zoom: 1 },
  roomEvents: [],
};

let currentView = "hq";
let liveRefreshTimer = null;

const eventBusState = {
  items: [],
  source: null,
};

const STAR_COUNT = 320;
const stars = Array.from({ length: STAR_COUNT }, (_, index) => {
  const seed = index + 1;
  return {
    x: ((seed * 73) % 2000) - 1000,
    y: ((seed * 41) % 1500) - 750,
    z: ((seed * 97) % 1800) - 900,
    size: 0.8 + ((seed * 17) % 5) * 0.12,
    alpha: 0.18 + ((seed * 31) % 10) * 0.03,
  };
});

function hexToRgb(hex) {
  const cleaned = (hex || "#d0d6e8").replace("#", "");
  if (cleaned.length !== 6) return { r: 208, g: 214, b: 232 };
  return {
    r: Number.parseInt(cleaned.slice(0, 2), 16),
    g: Number.parseInt(cleaned.slice(2, 4), 16),
    b: Number.parseInt(cleaned.slice(4, 6), 16),
  };
}

function rgba(hex, alpha) {
  const { r, g, b } = hexToRgb(hex);
  return `rgba(${r}, ${g}, ${b}, ${alpha})`;
}

function truncateText(value, length = 72) {
  const text = String(value || "").trim();
  if (text.length <= length) return text;
  return `${text.slice(0, Math.max(0, length - 1)).trimEnd()}…`;
}

function formatEventType(eventType) {
  return String(eventType || "event").replace(/[._]/g, " ");
}

function eventAccent(event) {
  const group = String(event?.event_group || "");
  const type = String(event?.event_type || "");
  if (group === "task" || type.startsWith("task.")) return "rgba(255, 125, 183, 0.9)";
  if (group === "scorecard" || type.startsWith("task.scored")) return "rgba(255, 209, 102, 0.92)";
  if (group === "feedback") return "rgba(110, 242, 197, 0.92)";
  if (group === "query") return "rgba(135, 168, 255, 0.9)";
  return "rgba(135, 168, 255, 0.85)";
}

function eventTitle(event) {
  if (event.event_type === "task.completed") {
    return `${event.skill || "agent"} completed ${event.pack_id || "task"}`;
  }
  if (event.event_type === "task.scored") {
    return `${event.skill || "agent"} scored ${event.pack_id || "task"}`;
  }
  if (String(event.event_type || "").startsWith("query.")) {
    return `${formatEventType(event.event_type)} • ${event.skill || event.role || "routing"}`;
  }
  if (event.event_type === "feedback.recorded") {
    return `Feedback • ${event.status || "recorded"}`;
  }
  return formatEventType(event.event_type);
}

function eventDetail(event) {
  if (event.query) return truncateText(event.query, 88);
  if (event.path) return truncateText(event.path, 88);
  return truncateText(JSON.stringify(event.metadata || {}), 88);
}

function renderEventStream(events) {
  if (!liveEventStream) return;
  if (!events || !events.length) {
    liveEventStream.innerHTML = `
      <div class="event-card" style="--event-accent: rgba(135, 168, 255, 0.85)">
        <div class="event-card-head">
          <span class="event-card-type">Waiting</span>
          <span class="event-card-time">Live</span>
        </div>
        <div class="event-card-title">Event bus is ready</div>
        <div class="event-card-detail">Queries, task completions, and scorecards will stream here as the squad works.</div>
      </div>
    `;
    return;
  }
  liveEventStream.innerHTML = events
    .slice(0, 12)
    .map((event) => {
      const accent = eventAccent(event);
      const ts = event.ts ? new Date(event.ts).toLocaleTimeString([], { hour: "2-digit", minute: "2-digit", second: "2-digit" }) : "live";
      const pills = [event.role, event.pack_id, event.status].filter(Boolean).slice(0, 3);
      return `
        <article class="event-card" style="--event-accent: ${accent}">
          <div class="event-card-head">
            <span class="event-card-type">${escapeHtml(formatEventType(event.event_type))}</span>
            <span class="event-card-time">${escapeHtml(ts)}</span>
          </div>
          <div class="event-card-title">${escapeHtml(eventTitle(event))}</div>
          <div class="event-card-detail">${escapeHtml(eventDetail(event))}</div>
          <div class="event-card-meta">
            ${pills.map((pill) => `<span class="event-pill">${escapeHtml(String(pill))}</span>`).join("")}
          </div>
        </article>
      `;
    })
    .join("");
}

function hydrateEventStream(events) {
  eventBusState.items = Array.isArray(events) ? [...events].sort((a, b) => Number(b.id || 0) - Number(a.id || 0)) : [];
  renderEventStream(eventBusState.items);
}

function pushEvent(event) {
  const normalized = {
    id: Number(event?.id || 0),
    ts: String(event?.ts || ""),
    event_type: String(event?.event_type || "event"),
    event_group: String(event?.event_group || ""),
    source: String(event?.source || ""),
    status: String(event?.status || ""),
    query: String(event?.query || ""),
    role: String(event?.role || ""),
    pack_id: String(event?.pack_id || ""),
    skill: String(event?.skill || ""),
    path: String(event?.path || ""),
    metadata: event?.metadata || {},
  };
  eventBusState.items = [normalized, ...eventBusState.items.filter((item) => Number(item.id || 0) !== normalized.id)].slice(0, 20);
  renderEventStream(eventBusState.items);
  generatedAt.textContent = `Updated ${new Date().toLocaleString()} • live event`;
  window.dispatchEvent(new CustomEvent("memory-event", { detail: normalized }));
}

function scheduleLiveRefresh() {
  if (liveRefreshTimer) window.clearTimeout(liveRefreshTimer);
  liveRefreshTimer = window.setTimeout(() => {
    liveRefreshTimer = null;
    loadGraph();
  }, 900);
}

function connectEventStream() {
  if (!window.EventSource) return;
  if (eventBusState.source) {
    eventBusState.source.close();
  }
  const since = eventBusState.items.length ? Number(eventBusState.items[0].id || 0) : 0;
  const source = new EventSource(`/api/events/stream?since=${since}`);
  source.addEventListener("memory-event", (payload) => {
    try {
      const event = JSON.parse(payload.data);
      pushEvent(event);
      scheduleLiveRefresh();
    } catch (_error) {
      // ignore malformed event frames
    }
  });
  source.onerror = () => {
    source.close();
    eventBusState.source = null;
    window.setTimeout(connectEventStream, 2500);
  };
  eventBusState.source = source;
}

function initialsForLabel(label) {
  const parts = String(label || "")
    .trim()
    .split(/\s+/)
    .filter(Boolean);
  if (!parts.length) return "AI";
  if (parts.length === 1) return parts[0].slice(0, 2).toUpperCase();
  return `${parts[0][0] || ""}${parts[1][0] || ""}`.toUpperCase();
}

function hashString(value) {
  let hash = 0;
  const text = String(value || "");
  for (let index = 0; index < text.length; index += 1) {
    hash = (hash * 31 + text.charCodeAt(index)) >>> 0;
  }
  return hash;
}

function avatarPalette(skill, domain, accent) {
  const skins = ["#f3d1b3", "#e8bc96", "#c98e62", "#a96b45", "#7b4d2d"];
  const hairs = ["#1d1a1a", "#3d2a1e", "#5f4327", "#8f6a48", "#d7b16d", "#4a4f74"];
  const hash = hashString(`${skill}:${domain}`);
  return {
    skin: skins[hash % skins.length],
    hair: hairs[(hash >> 3) % hairs.length],
    accent,
  };
}

function podCardPosition(domain) {
  const positions = {
    writer: { left: "23%", top: "26%" },
    marketing: { left: "22%", top: "48%" },
    charles: { left: "27%", top: "70%" },
    seo: { left: "73%", top: "22%" },
    developer: { left: "58%", top: "74%" },
    qa: { left: "78%", top: "61%" },
    support: { left: "15%", top: "72%" },
    core: { left: "50%", top: "18%" },
  };
  return positions[domain] || positions.core;
}

const OFFICE_LAYOUT = {
  room: { width: 16.8, depth: 11.6, wallHeight: 2.2 },
  table: { x: 7.0, y: 4.2, width: 2.7, depth: 1.8, height: 0.64 },
  board: { x: 13.8, y: 0.55, width: 1.45, depth: 0.22, height: 1.8 },
  desks: [
    { x: 1.8, y: 2.0, width: 1.8, depth: 1.05 },
    { x: 3.9, y: 1.45, width: 1.8, depth: 1.05 },
    { x: 1.55, y: 5.05, width: 1.8, depth: 1.05 },
    { x: 3.75, y: 7.1, width: 1.85, depth: 1.05 },
    { x: 10.6, y: 1.5, width: 1.9, depth: 1.05 },
    { x: 12.25, y: 3.2, width: 1.85, depth: 1.05 },
    { x: 7.2, y: 7.25, width: 1.9, depth: 1.05 },
    { x: 10.1, y: 7.8, width: 1.9, depth: 1.05 },
    { x: 12.4, y: 6.4, width: 1.85, depth: 1.05 },
  ],
  labels: {
    writer: { text: "Content Pod", x: 2.9, y: 0.55 },
    marketing: { text: "Growth Pod", x: 2.2, y: 4.15 },
    charles: { text: "Social Pod", x: 2.4, y: 8.5 },
    seo: { text: "SEO Pod", x: 11.9, y: 0.55 },
    developer: { text: "Dev Pod", x: 8.0, y: 10.2 },
    qa: { text: "QA Gate", x: 12.5, y: 8.9 },
    support: { text: "Ops / Support", x: 0.95, y: 9.35 },
    core: { text: "Brief Wall", x: 13.7, y: 0.08 },
  },
  slots: {
    writer: [
      { x: 2.65, y: 2.5, seated: true },
      { x: 4.65, y: 1.95, seated: true },
      { x: 2.3, y: 5.6, seated: true },
    ],
    marketing: [
      { x: 2.8, y: 4.5, seated: true },
      { x: 2.55, y: 6.95, seated: true },
    ],
    charles: [
      { x: 4.5, y: 7.65, seated: true },
      { x: 3.15, y: 8.7, seated: true },
    ],
    seo: [
      { x: 11.15, y: 2.0, seated: true },
      { x: 10.4, y: 1.8, seated: true },
      { x: 12.95, y: 3.9, seated: true },
    ],
    developer: [
      { x: 7.95, y: 7.95, seated: true },
      { x: 10.85, y: 8.45, seated: true },
      { x: 8.5, y: 7.0, seated: true },
    ],
    qa: [
      { x: 12.8, y: 6.95, seated: true },
      { x: 12.1, y: 7.95, seated: true },
    ],
    support: [
      { x: 1.5, y: 8.8, seated: true },
      { x: 2.8, y: 8.15, seated: true },
    ],
    core: [
      { x: 7.45, y: 1.05, seated: false },
      { x: 9.1, y: 1.0, seated: false },
    ],
    brain: [{ x: 7.95, y: 1.05, seated: false }],
  },
  activeSlots: {
    speaker: { x: 7.25, y: 4.95, seated: false, focus: true },
    listener: { x: 9.15, y: 4.35, seated: false, focus: true },
  },
  hub: { x: 7.95, y: 5.65 },
  entry: {
    writer: { x: 4.7, y: 3.6 },
    marketing: { x: 4.1, y: 5.4 },
    charles: { x: 4.8, y: 7.75 },
    seo: { x: 10.8, y: 3.25 },
    developer: { x: 9.15, y: 7.4 },
    qa: { x: 11.4, y: 7.05 },
    support: { x: 3.35, y: 8.3 },
    core: { x: 8.2, y: 2.15 },
  },
  focusCamera: {
    core: { x: 0, y: 0, zoom: 1 },
    writer: { x: -0.22, y: -0.04, zoom: 1.03 },
    marketing: { x: -0.2, y: 0.03, zoom: 1.03 },
    charles: { x: -0.18, y: 0.08, zoom: 1.035 },
    seo: { x: 0.2, y: -0.05, zoom: 1.04 },
    developer: { x: 0.06, y: 0.09, zoom: 1.035 },
    qa: { x: 0.18, y: 0.08, zoom: 1.035 },
    support: { x: -0.25, y: 0.1, zoom: 1.03 },
  },
  decor: {
    towers: [
      { x: 14.55, y: 2.0, width: 0.55, depth: 0.55, height: 1.3 },
      { x: 0.95, y: 6.9, width: 0.55, depth: 0.55, height: 1.22 },
      { x: 13.9, y: 8.9, width: 0.55, depth: 0.55, height: 1.18 },
    ],
    rails: [
      { from: { x: 1.2, y: 9.5 }, to: { x: 5.8, y: 9.5 } },
      { from: { x: 10.4, y: 9.15 }, to: { x: 14.8, y: 9.15 } },
      { from: { x: 2.0, y: 1.5 }, to: { x: 5.6, y: 1.5 } },
    ],
    beacons: [
      { x: 1.35, y: 1.15, color: "rgba(110, 242, 197, ALPHA)" },
      { x: 15.0, y: 1.2, color: "rgba(135, 168, 255, ALPHA)" },
      { x: 15.0, y: 9.85, color: "rgba(210, 123, 255, ALPHA)" },
      { x: 1.25, y: 9.9, color: "rgba(255, 125, 183, ALPHA)" },
    ],
  },
};

function clamp(value, min, max) {
  return Math.min(max, Math.max(min, value));
}

function lerp(start, end, alpha) {
  return start + (end - start) * alpha;
}

function easeInOutSine(value) {
  return -(Math.cos(Math.PI * clamp(value, 0, 1)) - 1) / 2;
}

function roundedRect(ctx2d, x, y, width, height, radius) {
  const safe = Math.min(radius, width / 2, height / 2);
  ctx2d.beginPath();
  ctx2d.moveTo(x + safe, y);
  ctx2d.arcTo(x + width, y, x + width, y + height, safe);
  ctx2d.arcTo(x + width, y + height, x, y + height, safe);
  ctx2d.arcTo(x, y + height, x, y, safe);
  ctx2d.arcTo(x, y, x + width, y, safe);
  ctx2d.closePath();
}

function buildOfficeStage(width, height, focusDomain = "core", pulse = 0) {
  const room = OFFICE_LAYOUT.room;
  const camera = OFFICE_LAYOUT.focusCamera[focusDomain] || OFFICE_LAYOUT.focusCamera.core;
  const liveCamera = meetingState.camera || camera;
  const baseTileWidth = Math.min(width / (room.width + room.depth + 8), 32);
  const tileWidth = baseTileWidth * ((liveCamera.zoom || 1) + pulse * 0.008);
  const tileHeight = tileWidth * 0.52;
  return {
    width,
    height,
    originX: width * (0.48 + (liveCamera.x || 0) * 0.18),
    originY: height * (0.18 + (liveCamera.y || 0) * 0.12),
    tileWidth,
    tileHeight,
    heightScale: tileWidth * 0.88,
  };
}

function updateOfficeCamera(focusDomain) {
  const target = OFFICE_LAYOUT.focusCamera[focusDomain] || OFFICE_LAYOUT.focusCamera.core;
  const current = meetingState.camera || { ...target };
  current.x = lerp(current.x || 0, target.x || 0, 0.08);
  current.y = lerp(current.y || 0, target.y || 0, 0.08);
  current.zoom = lerp(current.zoom || 1, target.zoom || 1, 0.08);
  meetingState.camera = current;
}

function projectIsoPoint(stage, x, y, z = 0) {
  return {
    x: stage.originX + (x - y) * stage.tileWidth,
    y: stage.originY + (x + y) * stage.tileHeight - z * stage.heightScale,
  };
}

function drawIsoPolygon(ctx2d, points, fill, stroke = "", alpha = 1) {
  if (!points.length) return;
  ctx2d.save();
  ctx2d.globalAlpha = alpha;
  ctx2d.beginPath();
  ctx2d.moveTo(points[0].x, points[0].y);
  for (let index = 1; index < points.length; index += 1) {
    ctx2d.lineTo(points[index].x, points[index].y);
  }
  ctx2d.closePath();
  if (fill) {
    ctx2d.fillStyle = fill;
    ctx2d.fill();
  }
  if (stroke) {
    ctx2d.strokeStyle = stroke;
    ctx2d.lineWidth = 1;
    ctx2d.stroke();
  }
  ctx2d.restore();
}

function drawIsoBlock(ctx2d, stage, x, y, width, depth, height, colors, alpha = 1) {
  const top = [
    projectIsoPoint(stage, x, y, height),
    projectIsoPoint(stage, x + width, y, height),
    projectIsoPoint(stage, x + width, y + depth, height),
    projectIsoPoint(stage, x, y + depth, height),
  ];
  const left = [
    projectIsoPoint(stage, x, y, 0),
    projectIsoPoint(stage, x, y + depth, 0),
    projectIsoPoint(stage, x, y + depth, height),
    projectIsoPoint(stage, x, y, height),
  ];
  const right = [
    projectIsoPoint(stage, x + width, y, 0),
    projectIsoPoint(stage, x + width, y + depth, 0),
    projectIsoPoint(stage, x + width, y + depth, height),
    projectIsoPoint(stage, x + width, y, height),
  ];
  drawIsoPolygon(ctx2d, left, colors.left, colors.stroke, alpha);
  drawIsoPolygon(ctx2d, right, colors.right, colors.stroke, alpha);
  drawIsoPolygon(ctx2d, top, colors.top, colors.stroke, alpha);
}

function renderOfficeGrid(ctx2d, stage) {
  const { width, depth } = OFFICE_LAYOUT.room;
  ctx2d.save();
  ctx2d.strokeStyle = "rgba(72, 82, 116, 0.22)";
  ctx2d.lineWidth = 1;
  for (let x = 0; x <= width; x += 1) {
    const from = projectIsoPoint(stage, x, 0, 0);
    const to = projectIsoPoint(stage, x, depth, 0);
    ctx2d.beginPath();
    ctx2d.moveTo(from.x, from.y);
    ctx2d.lineTo(to.x, to.y);
    ctx2d.stroke();
  }
  for (let y = 0; y <= depth; y += 1) {
    const from = projectIsoPoint(stage, 0, y, 0);
    const to = projectIsoPoint(stage, width, y, 0);
    ctx2d.beginPath();
    ctx2d.moveTo(from.x, from.y);
    ctx2d.lineTo(to.x, to.y);
    ctx2d.stroke();
  }
  ctx2d.restore();
}

function drawOfficeLabel(ctx2d, stage, label, point, active = false) {
  const projected = projectIsoPoint(stage, point.x, point.y, 0.06);
  const text = String(label || "");
  ctx2d.save();
  ctx2d.font = "11px 'IBM Plex Mono', monospace";
  const metrics = ctx2d.measureText(text);
  const width = metrics.width + 18;
  const height = 24;
  roundedRect(ctx2d, projected.x - width / 2, projected.y - 12, width, height, 12);
  ctx2d.fillStyle = active ? "rgba(135, 168, 255, 0.26)" : "rgba(8, 12, 22, 0.72)";
  ctx2d.fill();
  ctx2d.strokeStyle = active ? "rgba(135, 168, 255, 0.58)" : "rgba(255, 255, 255, 0.12)";
  ctx2d.stroke();
  ctx2d.fillStyle = active ? "#f8fbff" : "rgba(244, 246, 255, 0.82)";
  ctx2d.textAlign = "center";
  ctx2d.textBaseline = "middle";
  ctx2d.fillText(text, projected.x, projected.y);
  ctx2d.restore();
}

function drawIsoPath(ctx2d, stage, points, options = {}) {
  if (!points || points.length < 2) return;
  ctx2d.save();
  ctx2d.strokeStyle = options.color || "rgba(135, 168, 255, 0.38)";
  ctx2d.lineWidth = options.lineWidth || 3;
  if (options.dash) ctx2d.setLineDash(options.dash);
  ctx2d.beginPath();
  const first = projectIsoPoint(stage, points[0].x, points[0].y, points[0].z || 0.05);
  ctx2d.moveTo(first.x, first.y);
  for (let index = 1; index < points.length; index += 1) {
    const point = projectIsoPoint(stage, points[index].x, points[index].y, points[index].z || 0.05);
    ctx2d.lineTo(point.x, point.y);
  }
  ctx2d.stroke();
  ctx2d.restore();
}

function drawPlant(ctx2d, stage, plant) {
  drawIsoBlock(ctx2d, stage, plant.x, plant.y, 0.35, 0.35, 0.22, {
    top: "rgba(140, 104, 72, 0.98)",
    left: "rgba(86, 58, 40, 0.98)",
    right: "rgba(72, 49, 34, 0.98)",
    stroke: "rgba(255,255,255,0.06)",
  });
  const center = projectIsoPoint(stage, plant.x + 0.18, plant.y + 0.18, 0.55);
  ctx2d.save();
  ctx2d.fillStyle = "rgba(87, 170, 116, 0.98)";
  ctx2d.shadowColor = "rgba(87, 170, 116, 0.28)";
  ctx2d.shadowBlur = 12;
  ctx2d.beginPath();
  ctx2d.arc(center.x, center.y, plant.size * stage.tileWidth * 0.38, 0, Math.PI * 2);
  ctx2d.fill();
  ctx2d.restore();
}

function drawBeacon(ctx2d, stage, beacon, timestamp) {
  const point = projectIsoPoint(stage, beacon.x, beacon.y, 0.25);
  const pulse = 0.5 + 0.5 * Math.sin(timestamp * 0.0035 + beacon.x + beacon.y);
  const color = beacon.color.replace("ALPHA", String(0.28 + pulse * 0.22));
  ctx2d.save();
  const gradient = ctx2d.createRadialGradient(point.x, point.y, 2, point.x, point.y, 24);
  gradient.addColorStop(0, color);
  gradient.addColorStop(1, beacon.color.replace("ALPHA", "0"));
  ctx2d.fillStyle = gradient;
  ctx2d.beginPath();
  ctx2d.arc(point.x, point.y, 24, 0, Math.PI * 2);
  ctx2d.fill();
  ctx2d.restore();
}

function drawSceneGlow(ctx2d, stage, x, y, radiusX, radiusY, color, alpha = 0.22) {
  const point = projectIsoPoint(stage, x, y, 0.02);
  ctx2d.save();
  const gradient = ctx2d.createRadialGradient(point.x, point.y, 8, point.x, point.y, radiusX);
  gradient.addColorStop(0, color.replace("ALPHA", String(alpha)));
  gradient.addColorStop(1, color.replace("ALPHA", "0"));
  ctx2d.fillStyle = gradient;
  ctx2d.beginPath();
  ctx2d.ellipse(point.x, point.y, radiusX, radiusY, 0, 0, Math.PI * 2);
  ctx2d.fill();
  ctx2d.restore();
}

function drawFloatingCallout(ctx2d, x, y, title, detail, color = "rgba(135, 168, 255, 0.22)") {
  const titleText = truncateText(title, 24);
  const detailText = truncateText(detail, 42);
  ctx2d.save();
  ctx2d.font = "700 10px 'IBM Plex Mono', monospace";
  const titleWidth = ctx2d.measureText(titleText).width;
  ctx2d.font = "12px 'Space Grotesk', sans-serif";
  const detailWidth = ctx2d.measureText(detailText).width;
  const width = Math.max(titleWidth, detailWidth) + 22;
  const height = 42;
  roundedRect(ctx2d, x - width / 2, y - height, width, height, 12);
  ctx2d.fillStyle = "rgba(7, 10, 18, 0.84)";
  ctx2d.fill();
  ctx2d.strokeStyle = color;
  ctx2d.lineWidth = 1.4;
  ctx2d.stroke();
  ctx2d.fillStyle = "rgba(203, 214, 255, 0.86)";
  ctx2d.font = "700 10px 'IBM Plex Mono', monospace";
  ctx2d.textAlign = "center";
  ctx2d.fillText(titleText, x, y - 25);
  ctx2d.fillStyle = "#f3f6ff";
  ctx2d.font = "12px 'Space Grotesk', sans-serif";
  ctx2d.fillText(detailText, x, y - 10);
  ctx2d.restore();
}

function pushRoomEvent(scenario, turn) {
  if (!scenario || !turn) return;
  const speaker = labelForSkill(turn.speaker);
  const color = turn.speaker && turn.speaker !== "room"
    ? rgba((scenario.participants.find((item) => item.skill === turn.speaker) || {}).color || "#87a8ff", 0.42)
    : "rgba(135, 168, 255, 0.42)";
  meetingState.roomEvents = [
    {
      id: `${Date.now()}-${Math.random().toString(16).slice(2, 7)}`,
      title: speaker,
      detail: turn.message,
      color,
      createdAt: performance.now(),
    },
    ...(meetingState.roomEvents || []),
  ].slice(0, 6);
}

function drawWallBoard(ctx2d, stage, scenario, turn, timestamp) {
  const anchor = projectIsoPoint(stage, 14.55, 0.78, 1.62);
  const width = 132;
  const height = 78;
  const pulse = 0.5 + 0.5 * Math.sin(timestamp * 0.004);
  ctx2d.save();
  roundedRect(ctx2d, anchor.x - width / 2, anchor.y - height / 2, width, height, 12);
  ctx2d.fillStyle = "rgba(12, 18, 30, 0.92)";
  ctx2d.fill();
  ctx2d.strokeStyle = "rgba(135, 168, 255, 0.28)";
  ctx2d.lineWidth = 1.2;
  ctx2d.stroke();

  ctx2d.fillStyle = "rgba(193, 207, 255, 0.82)";
  ctx2d.font = "700 10px 'IBM Plex Mono', monospace";
  ctx2d.textAlign = "left";
  ctx2d.fillText("WAR ROOM", anchor.x - 50, anchor.y - 22);
  ctx2d.fillStyle = "#f4f7ff";
  ctx2d.font = "600 12px 'Space Grotesk', sans-serif";
  ctx2d.fillText(truncateText(scenario?.title || "Live squad sync", 22), anchor.x - 50, anchor.y - 6);
  ctx2d.fillStyle = "rgba(191, 199, 225, 0.82)";
  ctx2d.font = "11px 'Space Grotesk', sans-serif";
  ctx2d.fillText(truncateText(turn?.message || "Awaiting handoff", 28), anchor.x - 50, anchor.y + 10);

  const bars = [
    { label: "Flow", value: 0.72 + pulse * 0.18, color: "rgba(110, 242, 197, 0.88)" },
    { label: "Risk", value: 0.36 + pulse * 0.1, color: "rgba(255, 128, 165, 0.88)" },
    { label: "Sync", value: 0.58 + pulse * 0.14, color: "rgba(135, 168, 255, 0.92)" },
  ];
  bars.forEach((bar, index) => {
    const y = anchor.y + 22 + index * 14;
    ctx2d.fillStyle = "rgba(255,255,255,0.08)";
    roundedRect(ctx2d, anchor.x - 22, y - 6, 50, 8, 4);
    ctx2d.fill();
    ctx2d.fillStyle = bar.color;
    roundedRect(ctx2d, anchor.x - 22, y - 6, 50 * clamp(bar.value, 0, 1), 8, 4);
    ctx2d.fill();
    ctx2d.fillStyle = "rgba(190, 198, 225, 0.78)";
    ctx2d.font = "700 9px 'IBM Plex Mono', monospace";
    ctx2d.fillText(bar.label.toUpperCase(), anchor.x - 50, y + 1);
  });
  ctx2d.restore();
}

function drawRoomEvents(ctx2d, stage, timestamp) {
  const events = (meetingState.roomEvents || []).filter((event) => timestamp - event.createdAt < 5200);
  meetingState.roomEvents = events;
  events
    .slice(0, 3)
    .forEach((event, index) => {
      const age = clamp((timestamp - event.createdAt) / 5200, 0, 1);
      const board = projectIsoPoint(stage, 12.4, 1.35 + index * 0.92, 1.15);
      const driftY = age * 12;
      const opacity = 1 - age;
      ctx2d.save();
      ctx2d.globalAlpha = opacity * 0.92;
      roundedRect(ctx2d, board.x - 64, board.y - 20 - driftY, 128, 34, 10);
      ctx2d.fillStyle = "rgba(9, 12, 20, 0.84)";
      ctx2d.fill();
      ctx2d.strokeStyle = event.color;
      ctx2d.lineWidth = 1.2;
      ctx2d.stroke();
      ctx2d.fillStyle = "#f4f7ff";
      ctx2d.font = "700 9px 'IBM Plex Mono', monospace";
      ctx2d.textAlign = "left";
      ctx2d.fillText(event.title.toUpperCase(), board.x - 54, board.y - 6 - driftY);
      ctx2d.fillStyle = "rgba(199, 205, 229, 0.84)";
      ctx2d.font = "11px 'Space Grotesk', sans-serif";
      ctx2d.fillText(truncateText(event.detail, 34), board.x - 54, board.y + 8 - driftY);
      ctx2d.restore();
    });
}

function distance2d(a, b) {
  return Math.hypot((a.x || 0) - (b.x || 0), (a.y || 0) - (b.y || 0));
}

function buildMovementRoute(current, target) {
  const from = {
    x: current.x ?? target.x,
    y: current.y ?? target.y,
  };
  if (distance2d(from, target) < 0.7) return [{ x: target.x, y: target.y }];
  const currentEntry = OFFICE_LAYOUT.entry[current.domain] || OFFICE_LAYOUT.entry[target.domain] || OFFICE_LAYOUT.hub;
  const targetEntry = OFFICE_LAYOUT.entry[target.domain] || OFFICE_LAYOUT.hub;
  const route = [];
  if (distance2d(from, currentEntry) > 1.2) route.push({ x: currentEntry.x, y: currentEntry.y });
  if (distance2d(currentEntry, OFFICE_LAYOUT.hub) > 0.9) route.push({ x: OFFICE_LAYOUT.hub.x, y: OFFICE_LAYOUT.hub.y });
  if (distance2d(targetEntry, OFFICE_LAYOUT.hub) > 0.9) route.push({ x: targetEntry.x, y: targetEntry.y });
  route.push({ x: target.x, y: target.y });
  return route.filter((point, index) => index === 0 || distance2d(point, route[index - 1]) > 0.45);
}

function officeTargetsForScenario(scenario, turn) {
  const targets = {};
  if (!scenario) return targets;
  const zoneIndex = Object.fromEntries(Object.keys(OFFICE_LAYOUT.slots).map((key) => [key, 0]));
  scenario.participants.forEach((participant) => {
    const role = participant.skill === turn?.speaker
      ? "speaker"
      : participant.skill === turn?.listener && turn?.listener !== "room"
        ? "listener"
        : "";
    if (role) {
      targets[participant.skill] = {
        ...OFFICE_LAYOUT.activeSlots[role],
        domain: participant.domain || "core",
        role,
      };
      return;
    }
    const zone = participant.domain || "core";
    const slots = OFFICE_LAYOUT.slots[zone] || OFFICE_LAYOUT.slots.core;
    const index = zoneIndex[zone] || 0;
    zoneIndex[zone] = index + 1;
    targets[participant.skill] = {
      ...slots[index % slots.length],
      domain: zone,
      role: "member",
    };
  });
  return targets;
}

function updateActorPositions(targets) {
  Object.entries(targets).forEach(([skill, target]) => {
    const current = meetingState.actorPositions[skill] || { ...target };
    const targetKey = `${target.x.toFixed(2)}:${target.y.toFixed(2)}:${target.role}:${target.domain}`;
    if (current.targetKey !== targetKey) {
      current.route = buildMovementRoute(current, target);
      current.routeIndex = 0;
      current.targetKey = targetKey;
    }
    const route = current.route || [{ x: target.x, y: target.y }];
    const waypoint = route[Math.min(current.routeIndex || 0, route.length - 1)] || target;
    const dx = waypoint.x - current.x;
    const dy = waypoint.y - current.y;
    const dist = Math.hypot(dx, dy);
    const speed = target.role === "speaker" || target.role === "listener" ? 0.17 : 0.11;
    if (dist <= speed) {
      current.x = waypoint.x;
      current.y = waypoint.y;
      if ((current.routeIndex || 0) < route.length - 1) {
        current.routeIndex = (current.routeIndex || 0) + 1;
      }
      current.moving = false;
    } else if (dist > 0) {
      current.x += (dx / dist) * speed;
      current.y += (dy / dist) * speed;
      current.moving = true;
    } else {
      current.moving = false;
    }
    current.z = lerp(current.z || 0, target.z || 0, 0.14);
    current.seated = (current.routeIndex || 0) >= route.length - 1 ? target.seated : false;
    current.seatedBlend = lerp(current.seatedBlend ?? (current.seated ? 1 : 0), current.seated ? 1 : 0, 0.16);
    current.walkPhase = (current.walkPhase || 0) + (current.moving ? 0.36 : 0.06);
    current.role = target.role;
    current.domain = target.domain;
    current.focus = target.focus || false;
    meetingState.actorPositions[skill] = current;
  });
}

function drawAgentSprite(ctx2d, stage, actor, participant, timestamp) {
  const projected = projectIsoPoint(stage, actor.x, actor.y, actor.z || 0);
  const pulse = actor.role === "speaker" ? Math.sin(timestamp * 0.0065) * 3.4 : actor.role === "listener" ? Math.sin(timestamp * 0.0054) * 1.8 : 0;
  const scale = actor.role === "speaker" ? 1.12 : actor.role === "listener" ? 1.04 : 0.98;
  const seatedBlend = actor.seatedBlend ?? (actor.seated ? 1 : 0);
  const accent = participant.color || "#87a8ff";
  const initials = initialsForLabel(participant.label);
  const bob = actor.moving ? Math.sin(actor.walkPhase || 0) * 2.4 : 0;
  const baseY = projected.y + seatedBlend * 8 + bob + pulse;

  ctx2d.save();
  ctx2d.translate(projected.x, baseY);
  ctx2d.scale(scale, scale);

  ctx2d.fillStyle = "rgba(0, 0, 0, 0.16)";
  ctx2d.beginPath();
  ctx2d.ellipse(0, 18, lerp(18, 15, seatedBlend), lerp(7, 6, seatedBlend), 0, 0, Math.PI * 2);
  ctx2d.fill();

  if (actor.role === "speaker" || actor.role === "listener") {
    ctx2d.strokeStyle = actor.role === "speaker" ? rgba(accent, 0.62) : "rgba(255,255,255,0.24)";
    ctx2d.lineWidth = actor.role === "speaker" ? 3.5 : 2;
    ctx2d.beginPath();
    ctx2d.arc(0, -2, actor.role === "speaker" ? 20 : 16, 0, Math.PI * 2);
    ctx2d.stroke();
  }

  roundedRect(ctx2d, -11, -15 + seatedBlend * 2, 22, 24 - seatedBlend * 3, 9);
  ctx2d.fillStyle = "rgba(10, 14, 24, 0.94)";
  ctx2d.fill();
  ctx2d.strokeStyle = rgba(accent, actor.role === "speaker" ? 0.72 : 0.42);
  ctx2d.lineWidth = actor.role === "speaker" ? 2.2 : 1.5;
  ctx2d.stroke();

  const gradient = ctx2d.createLinearGradient(0, -18, 0, 12);
  gradient.addColorStop(0, rgba(accent, 0.86));
  gradient.addColorStop(1, "rgba(255,255,255,0.18)");
  roundedRect(ctx2d, -7, -11 + seatedBlend * 2, 14, 16 - seatedBlend * 2, 7);
  ctx2d.fillStyle = gradient;
  ctx2d.fill();

  ctx2d.beginPath();
  ctx2d.moveTo(0, 8 - seatedBlend * 2);
  ctx2d.lineTo(0, 16 - seatedBlend * 2);
  ctx2d.lineWidth = 2;
  ctx2d.strokeStyle = "rgba(255,255,255,0.32)";
  ctx2d.stroke();

  ctx2d.beginPath();
  ctx2d.arc(0, -18 + seatedBlend * 2, 8.2, 0, Math.PI * 2);
  ctx2d.fillStyle = "rgba(245, 248, 255, 0.94)";
  ctx2d.fill();

  ctx2d.beginPath();
  ctx2d.arc(0, -18 + seatedBlend * 2, 7, 0, Math.PI * 2);
  ctx2d.fillStyle = accent;
  ctx2d.fill();

  ctx2d.fillStyle = "#0d111a";
  ctx2d.font = "700 7px 'IBM Plex Mono', monospace";
  ctx2d.textAlign = "center";
  ctx2d.textBaseline = "middle";
  ctx2d.fillText(initials, 0, -18 + seatedBlend * 2);

  const labelY = actor.role === "speaker" || actor.role === "listener" ? -34 : -28;
  ctx2d.font = "700 7px 'IBM Plex Mono', monospace";
  const labelWidth = ctx2d.measureText(initials).width + 18;
  roundedRect(ctx2d, -labelWidth / 2, labelY - 7, labelWidth, 14, 7);
  ctx2d.fillStyle = "rgba(7, 10, 18, 0.8)";
  ctx2d.fill();
  ctx2d.strokeStyle = "rgba(255,255,255,0.14)";
  ctx2d.lineWidth = 1;
  ctx2d.stroke();
  ctx2d.fillStyle = "#f8fbff";
  ctx2d.fillText(initials, 0, labelY);

  ctx2d.restore();
}

function renderOfficeScene(timestamp = 0) {
  const width = officeCanvas.clientWidth;
  const height = officeCanvas.clientHeight;
  if (!width || !height) return;
  const scenario = currentScenario();
  const turn = currentTurn(scenario);
  const focusDomain = (scenario?.participants.find((item) => item.skill === turn?.speaker)?.domain) || "core";
  const stagePulse = scenario ? 0.5 + 0.5 * Math.sin(timestamp * 0.0018) : 0;
  updateOfficeCamera(focusDomain);
  const stage = buildOfficeStage(width, height, focusDomain, stagePulse);
  officeCtx.clearRect(0, 0, width, height);

  const room = OFFICE_LAYOUT.room;
  const floor = [
    projectIsoPoint(stage, 0, 0, 0),
    projectIsoPoint(stage, room.width, 0, 0),
    projectIsoPoint(stage, room.width, room.depth, 0),
    projectIsoPoint(stage, 0, room.depth, 0),
  ];
  const leftWall = [
    projectIsoPoint(stage, 0, 0, 0),
    projectIsoPoint(stage, 0, room.depth, 0),
    projectIsoPoint(stage, 0, room.depth, room.wallHeight),
    projectIsoPoint(stage, 0, 0, room.wallHeight),
  ];
  const backWall = [
    projectIsoPoint(stage, 0, 0, 0),
    projectIsoPoint(stage, room.width, 0, 0),
    projectIsoPoint(stage, room.width, 0, room.wallHeight),
    projectIsoPoint(stage, 0, 0, room.wallHeight),
  ];
  const rightWall = [
    projectIsoPoint(stage, room.width, 0, 0),
    projectIsoPoint(stage, room.width, room.depth, 0),
    projectIsoPoint(stage, room.width, room.depth, room.wallHeight),
    projectIsoPoint(stage, room.width, 0, room.wallHeight),
  ];

  drawIsoPolygon(officeCtx, leftWall, "rgba(75, 83, 118, 0.92)", "rgba(255,255,255,0.06)");
  drawIsoPolygon(officeCtx, backWall, "rgba(93, 103, 140, 0.95)", "rgba(255,255,255,0.06)");
  drawIsoPolygon(officeCtx, rightWall, "rgba(57, 63, 90, 0.95)", "rgba(255,255,255,0.04)");
  drawIsoPolygon(officeCtx, floor, "rgba(218, 203, 177, 0.98)", "rgba(66, 52, 37, 0.2)");
  renderOfficeGrid(officeCtx, stage);

  Object.entries(OFFICE_LAYOUT.labels).forEach(([domain, config]) => {
    if (domain === focusDomain) {
      drawSceneGlow(
        officeCtx,
        stage,
        config.x,
        config.y + 1.5,
        stage.tileWidth * 2.6,
        stage.tileHeight * 2.2,
        "rgba(135, 168, 255, ALPHA)",
        0.18,
      );
    }
  });

  Object.entries(OFFICE_LAYOUT.labels).forEach(([domain, config]) => {
    drawOfficeLabel(officeCtx, stage, config.text, config, domain === focusDomain);
  });

  OFFICE_LAYOUT.desks.forEach((desk, index) => {
    const activeDesk = focusDomain === "writer" && index <= 2
      || focusDomain === "marketing" && index === 3
      || focusDomain === "charles" && index === 3
      || focusDomain === "seo" && index >= 4 && index <= 5
      || focusDomain === "developer" && index >= 6 && index <= 7
      || focusDomain === "qa" && index === 8
      || focusDomain === "support" && index === 2;
    drawIsoBlock(
      officeCtx,
      stage,
      desk.x,
      desk.y,
      desk.width,
      desk.depth,
      0.55,
      activeDesk
        ? {
            top: "rgba(48, 58, 88, 0.98)",
            left: "rgba(28, 33, 51, 0.98)",
            right: "rgba(20, 24, 38, 0.98)",
            stroke: "rgba(255,255,255,0.08)",
          }
        : {
            top: "rgba(38, 45, 68, 0.96)",
            left: "rgba(24, 29, 46, 0.96)",
            right: "rgba(17, 21, 34, 0.96)",
            stroke: "rgba(255,255,255,0.06)",
          },
    );
    drawIsoBlock(
      officeCtx,
      stage,
      desk.x + 0.42,
      desk.y + 0.18,
      0.7,
      0.22,
      0.16,
      {
        top: activeDesk ? "rgba(146, 241, 209, 0.98)" : "rgba(197, 210, 245, 0.96)",
        left: activeDesk ? "rgba(73, 155, 130, 0.96)" : "rgba(133, 145, 190, 0.96)",
        right: activeDesk ? "rgba(51, 117, 99, 0.96)" : "rgba(102, 114, 156, 0.96)",
        stroke: "rgba(19, 23, 36, 0.18)",
      },
    );
  });

  OFFICE_LAYOUT.decor.towers.forEach((tower) => {
    drawIsoBlock(officeCtx, stage, tower.x, tower.y, tower.width, tower.depth, tower.height, {
      top: "rgba(41, 48, 72, 0.98)",
      left: "rgba(21, 26, 41, 0.98)",
      right: "rgba(14, 18, 30, 0.98)",
      stroke: "rgba(255,255,255,0.05)",
    });
    drawIsoBlock(officeCtx, stage, tower.x + 0.08, tower.y + 0.08, 0.22, 0.12, 0.08, {
      top: "rgba(146, 241, 209, 0.92)",
      left: "rgba(67, 150, 127, 0.9)",
      right: "rgba(39, 107, 89, 0.94)",
      stroke: "rgba(255,255,255,0.04)",
    });
  });

  OFFICE_LAYOUT.decor.rails.forEach((rail) => {
    drawIsoPath(officeCtx, stage, [rail.from, rail.to], {
      color: "rgba(255,255,255,0.12)",
      lineWidth: 2,
      dash: [6, 10],
    });
  });

  OFFICE_LAYOUT.decor.beacons.forEach((beacon) => {
    drawBeacon(officeCtx, stage, beacon, timestamp);
  });

  drawIsoBlock(officeCtx, stage, 5.9, 7.8, 1.5, 0.85, 0.28, {
    top: "rgba(43, 51, 78, 0.94)",
    left: "rgba(25, 30, 48, 0.98)",
    right: "rgba(16, 20, 34, 0.98)",
    stroke: "rgba(255,255,255,0.04)",
  });

  drawIsoBlock(officeCtx, stage, OFFICE_LAYOUT.board.x, OFFICE_LAYOUT.board.y, OFFICE_LAYOUT.board.width, OFFICE_LAYOUT.board.depth, OFFICE_LAYOUT.board.height, {
    top: "rgba(25, 31, 50, 0.96)",
    left: "rgba(18, 22, 36, 0.96)",
    right: "rgba(10, 14, 24, 0.96)",
    stroke: "rgba(255,255,255,0.08)",
  });
  drawWallBoard(officeCtx, stage, scenario, turn, timestamp);

  drawIsoBlock(officeCtx, stage, OFFICE_LAYOUT.table.x, OFFICE_LAYOUT.table.y, OFFICE_LAYOUT.table.width, OFFICE_LAYOUT.table.depth, OFFICE_LAYOUT.table.height, {
    top: "rgba(189, 138, 88, 0.98)",
    left: "rgba(120, 77, 46, 0.98)",
    right: "rgba(93, 58, 34, 0.98)",
    stroke: "rgba(255,255,255,0.08)",
  });

  const targets = officeTargetsForScenario(scenario, turn);
  updateActorPositions(targets);

  if (scenario) {
    const routeSource = OFFICE_LAYOUT.entry[focusDomain] || OFFICE_LAYOUT.hub;
    drawIsoPath(officeCtx, stage, [routeSource, OFFICE_LAYOUT.hub, { x: OFFICE_LAYOUT.table.x + 0.9, y: OFFICE_LAYOUT.table.y + 0.9 }], {
      color: "rgba(135, 168, 255, 0.34)",
      lineWidth: 4,
      dash: [10, 8],
    });
  }

  if (scenario && turn && turn.listener !== "room" && targets[turn.speaker] && targets[turn.listener]) {
    const from = projectIsoPoint(stage, meetingState.actorPositions[turn.speaker].x, meetingState.actorPositions[turn.speaker].y, 1.35);
    const to = projectIsoPoint(stage, meetingState.actorPositions[turn.listener].x, meetingState.actorPositions[turn.listener].y, 1.3);
    const controlX = (from.x + to.x) / 2;
    const controlY = Math.min(from.y, to.y) - 34;
    officeCtx.save();
    officeCtx.strokeStyle = "rgba(255,255,255,0.38)";
    officeCtx.lineWidth = 2;
    officeCtx.setLineDash([8, 8]);
    officeCtx.beginPath();
    officeCtx.moveTo(from.x, from.y);
    officeCtx.quadraticCurveTo(controlX, controlY, to.x, to.y);
    officeCtx.stroke();
    officeCtx.restore();

    const t = easeInOutSine(((timestamp - meetingState.turnStartedAt) % 1400) / 1400);
    const packetX = (1 - t) * (1 - t) * from.x + 2 * (1 - t) * t * controlX + t * t * to.x;
    const packetY = (1 - t) * (1 - t) * from.y + 2 * (1 - t) * t * controlY + t * t * to.y;
    officeCtx.save();
    officeCtx.fillStyle = "rgba(246, 250, 255, 0.98)";
    officeCtx.shadowColor = "rgba(255,255,255,0.78)";
    officeCtx.shadowBlur = 18;
    officeCtx.beginPath();
    officeCtx.arc(packetX, packetY, 5.2, 0, Math.PI * 2);
    officeCtx.fill();
    officeCtx.restore();
  }

  if (scenario) {
    const actors = scenario.participants
      .map((participant) => ({
        participant,
        actor: meetingState.actorPositions[participant.skill] || { ...(targets[participant.skill] || { x: 0, y: 0, z: 0 }) },
      }))
      .sort((left, right) => (left.actor.x + left.actor.y) - (right.actor.x + right.actor.y));

    actors.forEach(({ participant, actor }) => {
      drawAgentSprite(officeCtx, stage, actor, participant, timestamp);
    });

    if (turn?.speaker && meetingState.actorPositions[turn.speaker]) {
      const speakerPos = meetingState.actorPositions[turn.speaker];
      const speakerPoint = projectIsoPoint(stage, speakerPos.x, speakerPos.y, 1.65);
      drawFloatingCallout(
        officeCtx,
        speakerPoint.x,
        speakerPoint.y - 12,
        labelForSkill(turn.speaker),
        turn.message,
        rgba(targets[turn.speaker]?.focus ? "#87a8ff" : "#ffffff", 0.46),
      );
    }
    if (turn?.listener && turn.listener !== "room" && meetingState.actorPositions[turn.listener]) {
      const listenerPos = meetingState.actorPositions[turn.listener];
      const listenerPoint = projectIsoPoint(stage, listenerPos.x, listenerPos.y, 1.45);
      drawFloatingCallout(
        officeCtx,
        listenerPoint.x,
        listenerPoint.y - 8,
        labelForSkill(turn.listener),
        `Receiving from ${labelForSkill(turn.speaker)}`,
        "rgba(255,255,255,0.24)",
      );
    }
    drawRoomEvents(officeCtx, stage, timestamp);
  } else {
    officeCtx.save();
    officeCtx.fillStyle = "rgba(244, 246, 255, 0.84)";
    officeCtx.font = "600 18px 'Space Grotesk', sans-serif";
    officeCtx.textAlign = "center";
    officeCtx.fillText("No live meetings yet", width / 2, height / 2);
    officeCtx.restore();
  }
}

function setView(view) {
  currentView = ["hq", "split", "graph", "graph-pro"].includes(view) ? view : "hq";
  shell.dataset.view = currentView;
  Array.from(viewSwitch.querySelectorAll("button")).forEach((button) => {
    button.classList.toggle("is-active", button.dataset.view === currentView);
  });
  window.dispatchEvent(
    new CustomEvent("graph-view-change", {
      detail: { view: currentView },
    }),
  );
  requestAnimationFrame(resizeCanvas);
}

async function loadGraph() {
  refreshButton.disabled = true;
  refreshButton.textContent = "Refreshing...";
  try {
    const response = await fetch(`/api/graph?ts=${Date.now()}`, { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`Graph API returned ${response.status}`);
    }
    const payload = await response.json();
    latestPayload = payload;
    renderMetrics(payload.meta);
    hydrateEventStream(payload.recent_events || []);
    connectEventStream();
    generatedAt.textContent = `Updated ${new Date(payload.generated_at).toLocaleString()}`;
    window.dispatchEvent(
      new CustomEvent("graph-payload", {
        detail: payload,
      }),
    );
    updateInspector({
      label: "Squad Brain",
      kind: "brain",
      domain: "brain",
      details: {
        nodes: payload.meta.nodes_total,
        links: payload.meta.links_total,
        files: payload.meta.memory_paths_total || 0,
        chunks: payload.meta.chunks_total || 0,
        meetings: payload.meta.meetings_total || 0,
        manual_scorecards: payload.meta.manual_scorecards,
        evaluation: payload.meta.evaluation,
      },
      tags: ["live", "memory", "graph"],
    });
    setMeetingScenarios(payload.meetings || []);
    if (!animationFrame) {
      animationFrame = requestAnimationFrame(renderLoop);
    }
  } catch (error) {
    generatedAt.textContent = "Graph refresh failed";
    nodeTitle.textContent = "Graph Error";
    nodeMeta.textContent = "The live graph payload could not be loaded.";
    nodeDetails.textContent = String(error && error.message ? error.message : error);
    meetingTitle.textContent = "Meeting Stream Error";
    meetingMeta.textContent = "The graph loaded incorrectly, so the meeting lane has no live data.";
    meetingBubble.innerHTML = "<strong>Viewer error:</strong> The local graph payload could not be loaded.";
    meetingTranscript.innerHTML = "";
    if (meetingLiveCard) meetingLiveCard.innerHTML = "";
    if (meetingRoomTicker) meetingRoomTicker.innerHTML = "";
  } finally {
    refreshButton.disabled = false;
    refreshButton.textContent = "Refresh";
  }
}

function renderMetrics(meta) {
  const items = [
    ["Nodes", meta.nodes_total],
    ["Links", meta.links_total],
    ["Topics", meta.topics_total],
    ["Episodes", meta.episodes_total || 0],
    ["Contexts", meta.workspace_contexts_total || 0],
    ["Workspace", meta.workspace_items_total || 0],
    ["Runs", meta.active_runs_total || meta.runs_total || 0],
    ["Blockers", meta.open_blockers_total || 0],
    ["Files", meta.memory_paths_total || 0],
    ["Chunks", meta.chunks_total || 0],
    ["Events", meta.recent_events_total || 0],
    ["Meetings", meta.meetings_total || 0],
    ["Outcomes", meta.outcomes_total],
    ["Scorecards", meta.manual_scorecards],
    ["Eval", `${Math.round((meta.evaluation.primary_skill_accuracy || 0) * 100)}%`],
    ["Task Eval", `${Math.round((((meta.task_evaluation || {}).pass_rate) || 0) * 100)}%`],
  ];
  metricsContainer.innerHTML = items
    .map(
      ([label, value]) => `
        <div class="metric-card">
          <span class="metric-label">${label}</span>
          <strong>${value}</strong>
        </div>
      `,
    )
    .join("");
}

function updateInspector(node) {
  nodeTitle.textContent = node.label || node.id;
  const metaBits = [node.kind];
  if (node.domain) metaBits.push(node.domain);
  if (node.status) metaBits.push(node.status);
  nodeMeta.textContent = metaBits.join(" • ");
  nodeTags.innerHTML = (node.tags || []).map((tag) => `<span class="tag">${tag}</span>`).join("");
  nodeDetails.textContent = JSON.stringify(node.details || node.metrics || {}, null, 2);
}

function focusNode(node) {
  if (!node) return;
  selectedNode = node;
  spinEnabled = false;
  updateInspector(node);

  if (node.kind === "outcome" && node.id.startsWith("outcome:")) {
    selectMeetingByOutcome(Number(node.id.split(":")[1]));
  } else if (node.kind === "pack" && node.id.startsWith("pack:")) {
    selectMeetingByPack(node.id.split(":")[1]);
  } else if (node.kind === "skill" && node.id.startsWith("skill:")) {
    selectMeetingBySkill(node.id.split(":")[1]);
  }
}

function searchNode() {
  const query = nodeSearch.value.trim().toLowerCase();
  if (currentView === "graph-pro") {
    window.dispatchEvent(
      new CustomEvent("graph-pro-search", {
        detail: { query },
      }),
    );
    return;
  }
  if (!latestPayload) return;
  if (!query) return;
  const match = latestPayload.nodes.find((node) => {
    const haystack = [node.label, node.id, node.domain, ...(node.tags || [])].join(" ").toLowerCase();
    return haystack.includes(query);
  });
  if (match) focusNode(match);
}

function resizeCanvas() {
  const rect = graphContainer.getBoundingClientRect();
  const ratio = window.devicePixelRatio || 1;
  canvas.width = Math.floor(rect.width * ratio);
  canvas.height = Math.floor(rect.height * ratio);
  canvas.style.width = `${rect.width}px`;
  canvas.style.height = `${rect.height}px`;
  ctx.setTransform(ratio, 0, 0, ratio, 0, 0);

  const officeRect = officeCanvas.getBoundingClientRect();
  officeCanvas.width = Math.floor(officeRect.width * ratio);
  officeCanvas.height = Math.floor(officeRect.height * ratio);
  officeCanvas.style.width = `${officeRect.width}px`;
  officeCanvas.style.height = `${officeRect.height}px`;
  officeCtx.setTransform(ratio, 0, 0, ratio, 0, 0);
}

function transformPoint(node) {
  const x0 = node.x || 0;
  const y0 = node.y || 0;
  const z0 = node.z || 0;
  const cosY = Math.cos(rotationY);
  const sinY = Math.sin(rotationY);
  const cosX = Math.cos(rotationX);
  const sinX = Math.sin(rotationX);

  const x1 = x0 * cosY - z0 * sinY;
  const z1 = x0 * sinY + z0 * cosY;
  const y1 = y0 * cosX - z1 * sinX;
  const z2 = y0 * sinX + z1 * cosX;

  return { x: x1, y: y1, z: z2 };
}

function projectPoint(point, width, height) {
  const camera = 980 / zoom;
  const depth = camera + point.z;
  const scale = camera / Math.max(120, depth);
  return {
    sx: width / 2 + point.x * scale,
    sy: height / 2 + point.y * scale,
    scale,
    depth: point.z,
  };
}

function buildProjectedNodes(width, height) {
  if (!latestPayload) return { nodes: [], map: new Map() };
  const map = new Map();
  const transformed = latestPayload.nodes.map((node) => {
    const point = transformPoint(node);
    const projection = projectPoint(point, width, height);
    const item = {
      ...node,
      ...projection,
      radius: Math.max(2.2, (node.size || 8) * 0.36 * projection.scale),
    };
    map.set(node.id, item);
    return item;
  });
  return { nodes: transformed.sort((a, b) => a.depth - b.depth), map };
}

function renderBackground(width, height) {
  const grad = ctx.createRadialGradient(width * 0.52, height * 0.44, 30, width * 0.5, height * 0.52, width * 0.84);
  grad.addColorStop(0, "rgba(18, 24, 48, 0.96)");
  grad.addColorStop(0.42, "rgba(8, 12, 24, 0.98)");
  grad.addColorStop(1, "rgba(3, 4, 8, 1)");
  ctx.fillStyle = grad;
  ctx.fillRect(0, 0, width, height);

  const hazeA = ctx.createRadialGradient(width * 0.18, height * 0.16, 0, width * 0.18, height * 0.16, width * 0.34);
  hazeA.addColorStop(0, "rgba(110, 242, 197, 0.09)");
  hazeA.addColorStop(1, "rgba(110, 242, 197, 0)");
  ctx.fillStyle = hazeA;
  ctx.fillRect(0, 0, width, height);

  const hazeB = ctx.createRadialGradient(width * 0.82, height * 0.2, 0, width * 0.82, height * 0.2, width * 0.28);
  hazeB.addColorStop(0, "rgba(135, 168, 255, 0.12)");
  hazeB.addColorStop(1, "rgba(135, 168, 255, 0)");
  ctx.fillStyle = hazeB;
  ctx.fillRect(0, 0, width, height);
}

function renderStars(width, height) {
  stars.forEach((star) => {
    const point = transformPoint(star);
    const projection = projectPoint(point, width, height);
    ctx.fillStyle = `rgba(170, 182, 255, ${star.alpha})`;
    ctx.beginPath();
    ctx.arc(projection.sx, projection.sy, star.size * projection.scale * 1.2, 0, Math.PI * 2);
    ctx.fill();
  });
}

function drawGraphLabel(node, radius, active, inMeeting, isSpeaker) {
  const label = truncateText(node.label || node.id, 28);
  ctx.save();
  ctx.font = active ? "700 14px 'Space Grotesk', sans-serif" : "600 12px 'Space Grotesk', sans-serif";
  const width = ctx.measureText(label).width + 18;
  const x = node.sx + radius + 10;
  const y = node.sy - radius - 18;
  roundedRect(ctx, x - 6, y - 10, width, 22, 11);
  ctx.fillStyle = active
    ? "rgba(8, 11, 20, 0.92)"
    : inMeeting || isSpeaker
      ? "rgba(8, 11, 20, 0.84)"
      : "rgba(8, 11, 20, 0.72)";
  ctx.fill();
  ctx.strokeStyle = active ? "rgba(255,255,255,0.2)" : rgba(node.color || "#d0d6e8", inMeeting ? 0.26 : 0.14);
  ctx.lineWidth = 1;
  ctx.stroke();
  ctx.fillStyle = "rgba(243, 245, 255, 0.96)";
  ctx.textBaseline = "middle";
  ctx.fillText(label, x + 3, y + 1);
  ctx.restore();
}

function getMeetingHighlightState(timestamp) {
  const scenario = currentScenario();
  const turn = currentTurn(scenario);
  const activeSkills = new Set();
  const activeDomains = new Set();

  if (scenario) {
    scenario.participants.forEach((participant) => {
      activeSkills.add(`skill:${participant.skill}`);
      if (participant.domain) activeDomains.add(`domain:${participant.domain}`);
    });
    if (scenario.pack_id) activeSkills.add(`pack:${scenario.pack_id}`);
    if (scenario.outcome_id) activeSkills.add(`outcome:${scenario.outcome_id}`);
  }

  return {
    scenario,
    turn,
    activeNodeIds: activeSkills,
    activeDomains,
    speakerId: turn && turn.speaker && turn.speaker !== "room" ? `skill:${turn.speaker}` : "",
    listenerId: turn && turn.listener && turn.listener !== "room" ? `skill:${turn.listener}` : "",
    pulse: 0.5 + 0.5 * Math.sin(timestamp * 0.006),
  };
}

function renderLoop(timestamp = 0) {
  const width = graphContainer.clientWidth;
  const height = graphContainer.clientHeight;
  if (canvas.width === 0 || canvas.height === 0 || canvas.style.width !== `${width}px`) {
    resizeCanvas();
  }

  if (spinEnabled && !dragging) targetRotationY += 0.0024;
  rotationY += (targetRotationY - rotationY) * 0.08;
  rotationX += (targetRotationX - rotationX) * 0.08;

  ctx.clearRect(0, 0, width, height);
  renderBackground(width, height);
  renderStars(width, height);

  if (latestPayload) {
    const { nodes, map } = buildProjectedNodes(width, height);
    projectedNodes = nodes;
    const meetingHighlight = getMeetingHighlightState(timestamp);

    latestPayload.links.forEach((link) => {
      const source = map.get(typeof link.source === "string" ? link.source : link.source.id);
      const target = map.get(typeof link.target === "string" ? link.target : link.target.id);
      if (!source || !target) return;
      const sourceActive = meetingHighlight.activeNodeIds.has(source.id) || meetingHighlight.activeDomains.has(source.id);
      const targetActive = meetingHighlight.activeNodeIds.has(target.id) || meetingHighlight.activeDomains.has(target.id);
      const meetingLinked = sourceActive && targetActive;
      const gradient = ctx.createLinearGradient(source.sx, source.sy, target.sx, target.sy);
      gradient.addColorStop(0, meetingLinked ? rgba(source.color || "#d0d6e8", 0.18 + meetingHighlight.pulse * 0.26) : rgba(source.color || "#d0d6e8", 0.06));
      gradient.addColorStop(1, meetingLinked ? rgba(target.color || "#d0d6e8", 0.18 + meetingHighlight.pulse * 0.26) : rgba(target.color || "#d0d6e8", 0.03));
      ctx.strokeStyle = gradient;
      ctx.lineWidth = Math.max(0.4, (link.weight || 1) * (meetingLinked ? 1.3 : 0.72));
      ctx.beginPath();
      ctx.moveTo(source.sx, source.sy);
      ctx.lineTo(target.sx, target.sy);
      ctx.stroke();
    });

    nodes.forEach((node) => {
      const active = selectedNode && selectedNode.id === node.id;
      const hovered = hoveredNode && hoveredNode.id === node.id;
      const inMeeting = meetingHighlight.activeNodeIds.has(node.id) || meetingHighlight.activeDomains.has(node.id);
      const isSpeaker = meetingHighlight.speakerId === node.id;
      const isListener = meetingHighlight.listenerId === node.id;
      const isMemoryBank = node.kind === "memory_bank";
      const radius = node.radius * (active ? 1.35 : hovered ? 1.15 : isSpeaker ? 1.3 : inMeeting ? 1.12 : 1);

      ctx.save();
      ctx.shadowColor = node.color || "#d0d6e8";
      ctx.shadowBlur = active ? 34 : isSpeaker ? 40 : isMemoryBank ? 30 : inMeeting ? 24 : 14;
      const fill = ctx.createRadialGradient(node.sx - radius * 0.3, node.sy - radius * 0.4, 1, node.sx, node.sy, radius * 1.6);
      fill.addColorStop(0, "rgba(255,255,255,0.72)");
      fill.addColorStop(0.25, node.color || "#d0d6e8");
      fill.addColorStop(1, rgba(node.color || "#d0d6e8", 0.74));
      ctx.fillStyle = fill;
      ctx.beginPath();
      ctx.arc(node.sx, node.sy, radius, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();

      if (isMemoryBank) {
        ctx.strokeStyle = rgba(node.color || "#d0d6e8", 0.16 + meetingHighlight.pulse * 0.08);
        ctx.lineWidth = 1.2;
        ctx.beginPath();
        ctx.arc(node.sx, node.sy, radius + 8 + meetingHighlight.pulse * 4, 0, Math.PI * 2);
        ctx.stroke();
      }

      if (inMeeting) {
        const ringRadius = radius + 6 + meetingHighlight.pulse * (isSpeaker ? 9 : 4);
        ctx.strokeStyle = rgba(node.color || "#d0d6e8", isSpeaker ? 0.62 : isListener ? 0.44 : 0.28);
        ctx.lineWidth = isSpeaker ? 2.4 : 1.25;
        ctx.beginPath();
        ctx.arc(node.sx, node.sy, ringRadius, 0, Math.PI * 2);
        ctx.stroke();
      }

      if (active || hovered || node.kind === "domain" || node.kind === "memory_bank") {
        ctx.strokeStyle = active ? "rgba(255,255,255,0.92)" : inMeeting ? rgba(node.color || "#fff", 0.52) : "rgba(255,255,255,0.38)";
        ctx.lineWidth = active ? 2 : inMeeting ? 1.6 : 1;
        ctx.beginPath();
        ctx.arc(node.sx, node.sy, radius + 4, 0, Math.PI * 2);
        ctx.stroke();
      }

      if (node.kind === "domain" || node.kind === "memory_bank" || active || hovered || isSpeaker) {
        drawGraphLabel(node, radius, active, inMeeting, isSpeaker);
      }
    });
  }

  renderOfficeScene(timestamp);

  animationFrame = requestAnimationFrame(renderLoop);
}

function getRelativePointer(event) {
  const rect = canvas.getBoundingClientRect();
  return { x: event.clientX - rect.left, y: event.clientY - rect.top };
}

function nearestNode(pointer) {
  let best = null;
  let bestDist = Infinity;
  for (const node of projectedNodes) {
    const dx = node.sx - pointer.x;
    const dy = node.sy - pointer.y;
    const dist = Math.sqrt(dx * dx + dy * dy);
    if (dist < Math.max(10, node.radius + 6) && dist < bestDist) {
      best = node;
      bestDist = dist;
    }
  }
  return best;
}

function setMeetingScenarios(scenarios) {
  meetingState.scenarios = Array.isArray(scenarios) ? scenarios : [];
  meetingState.scenarioIndex = 0;
  meetingState.turnIndex = 0;
  meetingState.paused = false;
  meetingState.turnStartedAt = performance.now();
  meetingState.roomEvents = [];
  meetingPause.textContent = "Pause";
  if (meetingState.timer) clearInterval(meetingState.timer);
  if (!meetingState.scenarios.length) {
    meetingTitle.textContent = "Realtime Handoff Room";
    meetingMeta.textContent = "No live meeting scenarios are available yet.";
    meetingPack.textContent = "Waiting";
    meetingSpeaker.textContent = "Room";
    meetingListener.textContent = "Room";
    meetingStatus.textContent = "Idle";
    meetingCounter.textContent = "Meeting 0 / 0";
    meetingProgressFill.style.width = "0%";
    meetingNodes.innerHTML = "";
    meetingSvg.innerHTML = "";
    meetingBubble.innerHTML = "<strong>No live meeting.</strong> Complete more tasks or packs to populate this lane.";
    meetingAgenda.innerHTML = "";
    meetingTicker.innerHTML = "";
    meetingTranscript.innerHTML = "";
    if (meetingLiveCard) meetingLiveCard.innerHTML = "";
    if (meetingRoomTicker) meetingRoomTicker.innerHTML = "";
    if (meetingBoard) meetingBoard.dataset.focus = "core";
    if (meetingPodCard) meetingPodCard.innerHTML = "";
    return;
  }
  renderMeetingScenario();
  meetingState.timer = setInterval(() => {
    if (!meetingState.paused) advanceMeeting();
  }, 2600);
}

function currentScenario() {
  if (!meetingState.scenarios.length) return null;
  return meetingState.scenarios[meetingState.scenarioIndex % meetingState.scenarios.length];
}

function currentTurn(scenario) {
  if (!scenario || !scenario.turns || !scenario.turns.length) return null;
  return scenario.turns[meetingState.turnIndex % scenario.turns.length];
}

function participantLayout(participants, speaker, listener) {
  const positions = [];
  const speakerSlot = { left: 49, top: 40 };
  const listenerSlot = { left: 59, top: 37 };
  const zoneSlots = {
    writer: [{ left: 20, top: 31 }, { left: 31, top: 28 }, { left: 19, top: 58 }],
    marketing: [{ left: 24, top: 44 }, { left: 20, top: 68 }],
    charles: [{ left: 31, top: 62 }, { left: 24, top: 74 }],
    seo: [{ left: 72, top: 29 }, { left: 66, top: 26 }, { left: 78, top: 40 }],
    developer: [{ left: 56, top: 70 }, { left: 64, top: 66 }, { left: 58, top: 58 }],
    qa: [{ left: 75, top: 56 }, { left: 69, top: 61 }],
    support: [{ left: 14, top: 68 }, { left: 21, top: 61 }],
    core: [{ left: 48, top: 18 }, { left: 60, top: 18 }],
    brain: [{ left: 48, top: 18 }],
  };
  const zoneIndex = Object.fromEntries(Object.keys(zoneSlots).map((key) => [key, 0]));

  participants.forEach((participant) => {
    if (participant.skill === speaker) {
      positions.push(speakerSlot);
      return;
    }
    if (participant.skill === listener && listener !== "room") {
      positions.push(listenerSlot);
      return;
    }
    const zone = participant.domain || "core";
    const slots = zoneSlots[zone] || zoneSlots.core;
    const index = zoneIndex[zone] || 0;
    positions.push(slots[index % slots.length]);
    zoneIndex[zone] = index + 1;
  });
  return positions;
}

function renderMeetingScenario() {
  const scenario = currentScenario();
  if (!scenario) return;
  meetingState.turnStartedAt = performance.now();
  const turn = currentTurn(scenario);
  pushRoomEvent(scenario, turn);
  const progress = scenario.turns.length ? ((meetingState.turnIndex + 1) / scenario.turns.length) * 100 : 0;
  const speaker = turn ? turn.speaker : "";
  const listener = turn ? turn.listener : "";
  const speakerParticipant = scenario.participants.find((participant) => participant.skill === speaker) || scenario.participants[0];
  const listenerParticipant = scenario.participants.find((participant) => participant.skill === listener) || null;
  const focusDomain = (speakerParticipant && speakerParticipant.domain) || "core";

  meetingTitle.textContent = scenario.title;
  meetingMeta.textContent = `${scenario.status} • ${scenario.query}`;
  meetingPack.textContent = scenario.title;
  meetingSpeaker.textContent = labelForSkill(speaker);
  meetingListener.textContent = listener && listener !== "room" ? labelForSkill(listener) : "Room";
  meetingStatus.textContent = scenario.synthetic ? "live" : scenario.status;
  meetingCounter.textContent = `Meeting ${meetingState.scenarioIndex + 1} / ${meetingState.scenarios.length}`;
  meetingProgressFill.style.width = `${progress}%`;
  if (hqBoardLabel) {
    hqBoardLabel.textContent = truncateText(
      scenario.pack_id === "technical_seo_war_room" ? "Tech SEO Board" : scenario.title,
      22,
    );
  }
  if (meetingBoard) {
    meetingBoard.dataset.focus = focusDomain;
    meetingBoard.classList.add("office-mode");
  }

  const positions = participantLayout(scenario.participants, speaker, listener);
  meetingNodes.innerHTML = scenario.participants
    .map((participant, index) => {
      const pos = positions[index];
      const isSpeaker = participant.skill === speaker;
      const isListener = participant.skill === listener;
      const activeTask = isSpeaker
        ? truncateText(turn ? turn.message : scenario.query, 56)
        : isListener
          ? truncateText(`Receiving: ${turn ? turn.message : scenario.query}`, 48)
          : "";
      const classes = [
        "meeting-node",
        isSpeaker ? "active" : "",
        isListener ? "listener" : "",
        !isSpeaker && !isListener ? "seated" : "standing",
        speaker && participant.skill !== speaker && participant.skill !== listener ? "dim" : "",
      ]
        .filter(Boolean)
        .join(" ");
      const palette = avatarPalette(participant.skill, participant.domain, participant.color);
      return `
        <div class="${classes} domain-${participant.domain || "core"}" data-skill="${participant.skill}" style="left:${pos.left}%;top:${pos.top}%;--agent-skin:${palette.skin};--agent-hair:${palette.hair};--agent-accent:${palette.accent};">
          <div class="meeting-node-avatar">
            ${!isSpeaker && !isListener ? '<div class="meeting-node-desk"></div><div class="meeting-node-chair"></div><div class="meeting-node-monitor"></div>' : ""}
            <div class="meeting-node-shadow"></div>
            <div class="meeting-node-hair"></div>
            <div class="meeting-node-head">
              <span class="meeting-node-eye meeting-node-eye-left"></span>
              <span class="meeting-node-eye meeting-node-eye-right"></span>
            </div>
            <div class="meeting-node-arm meeting-node-arm-left"></div>
            <div class="meeting-node-arm meeting-node-arm-right"></div>
            <div class="meeting-node-body"></div>
            <div class="meeting-node-leg meeting-node-leg-left"></div>
            <div class="meeting-node-leg meeting-node-leg-right"></div>
            <div class="meeting-node-badge">${escapeHtml(initialsForLabel(participant.label))}</div>
          </div>
          <div class="meeting-node-label">${participant.label}</div>
          <div class="meeting-node-role">${participant.role}</div>
          ${activeTask ? `<div class="meeting-node-task">${escapeHtml(activeTask)}</div>` : ""}
        </div>
      `;
    })
    .join("");

  const map = new Map(scenario.participants.map((participant, index) => [participant.skill, positions[index]]));
  const lines = [];
  meetingSvg.setAttribute("viewBox", "0 0 100 100");
  meetingSvg.setAttribute("preserveAspectRatio", "none");
  scenario.participants.forEach((participant, index) => {
    const pos = positions[index];
    const pathToCenter = `M ${pos.left} ${pos.top} L 50 50`;
    lines.push(`
      <line
        x1="${pos.left}"
        y1="${pos.top}"
        x2="50"
        y2="50"
        stroke="${rgba(participant.color, participant.skill === speaker ? 0.7 : 0.18)}"
        stroke-width="${participant.skill === speaker ? 2.4 : 1.1}"
      />
    `);
    if (participant.skill === speaker || participant.skill === listener) {
      lines.push(`
        <circle r="${participant.skill === speaker ? 1.1 : 0.85}" fill="${participant.color}">
          <animateMotion dur="${participant.skill === speaker ? "1.05s" : "1.35s"}" repeatCount="indefinite" path="${pathToCenter}" />
        </circle>
      `);
    }
  });
  if (turn && map.has(turn.speaker) && turn.listener !== "room" && map.has(turn.listener)) {
    const from = map.get(turn.speaker);
    const to = map.get(turn.listener);
    const handoffPath = `M ${from.left} ${from.top} L ${to.left} ${to.top}`;
    lines.push(`
      <line
        x1="${from.left}"
        y1="${from.top}"
        x2="${to.left}"
        y2="${to.top}"
        stroke="${rgba("#ffffff", 0.75)}"
        stroke-width="2.4"
        stroke-dasharray="8 8"
      >
        <animate attributeName="stroke-dashoffset" values="16;0" dur="0.9s" repeatCount="indefinite" />
      </line>
      <circle r="1.2" fill="${rgba("#ffffff", 0.95)}">
        <animateMotion dur="0.95s" repeatCount="indefinite" path="${handoffPath}" />
      </circle>
    `);
  }
  meetingSvg.innerHTML = lines.join("");

  meetingBubble.innerHTML = turn
    ? `<strong>${labelForSkill(turn.speaker)}</strong>${turn.listener !== "room" ? ` → <strong>${labelForSkill(turn.listener)}</strong>` : ""}<br />${escapeHtml(turn.message)}`
    : "<strong>No active turn.</strong>";

  if (meetingLiveCard) {
    meetingLiveCard.innerHTML = `
      <span class="meeting-live-eyebrow">Live Task</span>
      <strong>${escapeHtml(scenario.title)}</strong>
      <p>${escapeHtml(truncateText(scenario.query, 136))}</p>
    `;
  }

  if (meetingPodCard && speakerParticipant) {
    const pos = podCardPosition(focusDomain);
    meetingPodCard.style.left = pos.left;
    meetingPodCard.style.top = pos.top;
    meetingPodCard.innerHTML = `
      <span class="meeting-pod-card-label">${escapeHtml(labelForSkill(speakerParticipant.skill))}</span>
      <strong>${escapeHtml((focusDomain || "core").replace(/[-_]/g, " "))}</strong>
      <p>${escapeHtml(truncateText(turn ? turn.message : scenario.query, 92))}</p>
      ${listenerParticipant ? `<small>handoff → ${escapeHtml(labelForSkill(listenerParticipant.skill))}</small>` : ""}
    `;
  }

  meetingAgenda.innerHTML = (scenario.agenda || [])
    .slice(0, 4)
    .map((item, index) => {
      const activeChip = index === Math.min((scenario.agenda || []).length - 1, meetingState.turnIndex % Math.max(1, (scenario.agenda || []).length));
      return `<div class="meeting-chip ${activeChip ? "active" : ""}">${escapeHtml(truncateText(item, 58))}</div>`;
    })
    .join("");

  meetingTicker.innerHTML = scenario.turns
    .slice(0, 5)
    .map((item, index) => {
      return `
        <div class="meeting-ticker-card ${index === meetingState.turnIndex ? "active" : ""}">
          <strong>${escapeHtml(labelForSkill(item.speaker))}${item.listener && item.listener !== "room" ? ` → ${escapeHtml(labelForSkill(item.listener))}` : ""}</strong>
          <p>${escapeHtml(truncateText(item.message, 110))}</p>
        </div>
      `;
    })
    .join("");

  if (meetingRoomTicker) {
    meetingRoomTicker.innerHTML = scenario.turns
      .slice(0, 4)
      .map((item, index) => {
        const active = index === meetingState.turnIndex;
        return `
          <div class="meeting-room-event ${active ? "active" : ""}">
            <strong>${escapeHtml(labelForSkill(item.speaker))}</strong>
            <span>${escapeHtml(truncateText(item.message, 78))}</span>
          </div>
        `;
      })
      .join("");
  }

  const recentTurns = scenario.turns
    .slice(Math.max(0, meetingState.turnIndex - 2), Math.min(scenario.turns.length, meetingState.turnIndex + 2))
    .map((item, index) => {
      const absoluteIndex = Math.max(0, meetingState.turnIndex - 2) + index;
      return `<div class="meeting-line ${absoluteIndex === meetingState.turnIndex ? "active" : ""}"><strong>${labelForSkill(item.speaker)}</strong> ${absoluteIndex === meetingState.turnIndex ? "•" : "·"} ${escapeHtml(item.message)}</div>`;
    });
  meetingTranscript.innerHTML = recentTurns.join("");
}

function labelForSkill(skill) {
  if (!skill || skill === "room") return "Room";
  const scenario = currentScenario();
  const participant = scenario ? scenario.participants.find((item) => item.skill === skill) : null;
  if (participant) return participant.label;
  return skill
    .replace(/[-_]/g, " ")
    .replace(/\b\w/g, (char) => char.toUpperCase());
}

function escapeHtml(value) {
  return String(value)
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
}

function advanceMeeting() {
  const scenario = currentScenario();
  if (!scenario) return;
  meetingState.turnIndex += 1;
  if (meetingState.turnIndex >= scenario.turns.length) {
    meetingState.turnIndex = 0;
    meetingState.scenarioIndex = (meetingState.scenarioIndex + 1) % meetingState.scenarios.length;
  }
  renderMeetingScenario();
}

function selectMeetingByPack(packId) {
  const index = meetingState.scenarios.findIndex((scenario) => scenario.pack_id === packId);
  if (index >= 0) {
    meetingState.scenarioIndex = index;
    meetingState.turnIndex = 0;
    renderMeetingScenario();
  }
}

function selectMeetingByOutcome(outcomeId) {
  const index = meetingState.scenarios.findIndex((scenario) => Number(scenario.outcome_id) === Number(outcomeId));
  if (index >= 0) {
    meetingState.scenarioIndex = index;
    meetingState.turnIndex = 0;
    renderMeetingScenario();
  }
}

function selectMeetingBySkill(skill) {
  const index = meetingState.scenarios.findIndex((scenario) =>
    scenario.participants.some((participant) => participant.skill === skill),
  );
  if (index >= 0) {
    meetingState.scenarioIndex = index;
    meetingState.turnIndex = 0;
    renderMeetingScenario();
  }
}

canvas.addEventListener("mousemove", (event) => {
  const pointer = getRelativePointer(event);
  if (dragging && lastPointer) {
    const dx = pointer.x - lastPointer.x;
    const dy = pointer.y - lastPointer.y;
    targetRotationY += dx * 0.0045;
    targetRotationX += dy * 0.0035;
    lastPointer = pointer;
    return;
  }
  hoveredNode = nearestNode(pointer);
  graphContainer.style.cursor = hoveredNode ? "pointer" : "grab";
});

canvas.addEventListener("mousedown", (event) => {
  dragging = true;
  spinEnabled = false;
  lastPointer = getRelativePointer(event);
  graphContainer.style.cursor = "grabbing";
});

window.addEventListener("mouseup", () => {
  dragging = false;
  lastPointer = null;
  graphContainer.style.cursor = hoveredNode ? "pointer" : "grab";
});

canvas.addEventListener("click", (event) => {
  const pointer = getRelativePointer(event);
  const node = nearestNode(pointer);
  if (node) focusNode(node);
});

canvas.addEventListener(
  "wheel",
  (event) => {
    event.preventDefault();
    zoom = Math.min(2.4, Math.max(0.55, zoom + Math.sign(event.deltaY) * 0.08));
  },
  { passive: false },
);

refreshButton.addEventListener("click", loadGraph);
nodeSearch.addEventListener("keydown", (event) => {
  if (event.key === "Enter") searchNode();
});
viewSwitch.addEventListener("click", (event) => {
  const button = event.target.closest("[data-view]");
  if (!button) return;
  setView(button.dataset.view);
});
meetingPrev.addEventListener("click", () => {
  if (!meetingState.scenarios.length) return;
  meetingState.scenarioIndex = (meetingState.scenarioIndex - 1 + meetingState.scenarios.length) % meetingState.scenarios.length;
  meetingState.turnIndex = 0;
  renderMeetingScenario();
});
meetingNext.addEventListener("click", () => {
  if (!meetingState.scenarios.length) return;
  meetingState.scenarioIndex = (meetingState.scenarioIndex + 1) % meetingState.scenarios.length;
  meetingState.turnIndex = 0;
  renderMeetingScenario();
});
meetingPause.addEventListener("click", () => {
  meetingState.paused = !meetingState.paused;
  meetingPause.textContent = meetingState.paused ? "Resume" : "Pause";
});
meetingNodes.addEventListener("click", (event) => {
  const node = event.target.closest("[data-skill]");
  if (!node || !latestPayload) return;
  const skillId = `skill:${node.getAttribute("data-skill")}`;
  const match = latestPayload.nodes.find((item) => item.id === skillId);
  if (match) focusNode(match);
});

window.addEventListener("resize", resizeCanvas);
window.addEventListener("graph-node-selected", (event) => {
  const node = event.detail?.node;
  if (!node) return;
  focusNode(node);
});

const initialView = new URLSearchParams(window.location.search).get("view") || "hq";
setView(initialView);
resizeCanvas();
setInterval(loadGraph, 30000);
loadGraph();
