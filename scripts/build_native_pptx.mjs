#!/usr/bin/env node

/**
 * Build a native, editable PPTX from a Knowledge Cat deck-plan JSON file.
 *
 * The builder uses @oai/artifact-tool so text, shapes, charts, tables, and
 * speaker notes remain native PowerPoint objects. The final PPTX is re-imported
 * before rendering previews and writing the inspection log.
 */

import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { createRequire } from "node:module";
import { pathToFileURL } from "node:url";

const SLIDE_SIZE = { width: 1280, height: 720 };
const PAGE = { left: 76, top: 62, width: 1128, height: 590 };
const COLORS = {
  ink: "#12202F",
  muted: "#5B6875",
  paper: "#F5F1E8",
  white: "#FFFFFF",
  accent: "#E95D45",
  blue: "#3E6E8F",
  green: "#5C7A63",
  line: "#D7D0C3",
  pale: "#E9E3D8",
};

function parseArgs(argv) {
  const args = {};
  for (let index = 0; index < argv.length; index += 1) {
    const token = argv[index];
    if (!token.startsWith("--")) throw new Error(`Unexpected argument: ${token}`);
    const value = argv[index + 1];
    if (!value || value.startsWith("--")) {
      args[token.slice(2)] = true;
      continue;
    }
    args[token.slice(2)] = value;
    index += 1;
  }
  return args;
}

function requireString(args, key) {
  const value = args[key];
  if (typeof value !== "string" || !value.trim()) {
    throw new Error(`Missing required --${key}`);
  }
  return path.resolve(value);
}

async function importArtifactTool(workspace) {
  const resolver = createRequire(path.join(workspace, "package.json"));
  let entrypoint;
  try {
    entrypoint = resolver.resolve("@oai/artifact-tool");
  } catch (error) {
    throw new Error(
      [
        "@oai/artifact-tool is not available in the selected workspace.",
        "Initialize the workspace with the Presentations skill helper first:",
        "node <presentations-skill>/container_tools/setup_artifact_tool_workspace.mjs --workspace <workspace>",
        `Resolver error: ${error.message}`,
      ].join("\n"),
    );
  }
  return import(pathToFileURL(entrypoint).href);
}

async function writeBlob(outputPath, blob) {
  await fs.mkdir(path.dirname(outputPath), { recursive: true });
  await fs.writeFile(outputPath, new Uint8Array(await blob.arrayBuffer()));
}

async function readImageBytes(imagePath) {
  const bytes = await fs.readFile(imagePath);
  return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
}

async function renderContactSheet(Presentation, slidePaths, outputPath) {
  const sheet = Presentation.create({ slideSize: { width: 1920, height: 1080 } });
  const slide = sheet.slides.add();
  slide.background.fill = COLORS.ink;
  addText(
    slide,
    "contact-sheet-title",
    "NATIVE PPTX · RENDERED QA",
    { left: 56, top: 26, width: 900, height: 34 },
    { fontSize: 18, bold: true, color: COLORS.white },
  );
  addText(
    slide,
    "contact-sheet-meta",
    `${slidePaths.length} final-slide previews · generated after PPTX re-import`,
    { left: 1110, top: 30, width: 750, height: 28 },
    { fontSize: 14, color: "#A9B5C0", alignment: "right" },
  );
  const columns = 3;
  const rows = Math.ceil(slidePaths.length / columns);
  const gap = 24;
  const left = 56;
  const top = 82;
  const cellWidth = (1920 - left * 2 - gap * (columns - 1)) / columns;
  const cellHeight = (1080 - top - 44 - gap * (rows - 1)) / rows;
  for (const [index, slidePath] of slidePaths.entries()) {
    const column = index % columns;
    const row = Math.floor(index / columns);
    slide.images.add({
      blob: await readImageBytes(slidePath),
      contentType: "image/png",
      alt: `Rendered preview of slide ${index + 1}`,
      fit: "contain",
      position: {
        left: left + column * (cellWidth + gap),
        top: top + row * (cellHeight + gap),
        width: cellWidth,
        height: cellHeight,
      },
      geometry: "rect",
    });
  }
  await writeBlob(outputPath, await sheet.export({ slide, format: "png", scale: 1 }));
}

function addShape(slide, name, geometry, position, options = {}) {
  return slide.shapes.add({
    geometry,
    name,
    position,
    fill: options.fill ?? "none",
    line: options.line ?? { style: "solid", fill: "none", width: 0 },
  });
}

function addText(slide, name, text, position, style = {}) {
  const shape = addShape(slide, name, "textbox", position);
  shape.text = String(text ?? "");
  shape.text.style = {
    fontSize: style.fontSize ?? 20,
    color: style.color ?? COLORS.ink,
    bold: style.bold ?? false,
    italic: style.italic ?? false,
    alignment: style.alignment ?? "left",
    verticalAlignment: style.verticalAlignment ?? "top",
  };
  return shape;
}

function addRule(slide, name, left, top, width, color = COLORS.line, weight = 2) {
  return addShape(
    slide,
    name,
    "rect",
    { left, top, width, height: weight },
    { fill: color },
  );
}

function addChrome(slide, planSlide, totalSlides) {
  addText(
    slide,
    `slide-${planSlide.number}-eyebrow`,
    String(planSlide.role || "PRESENTATION").toUpperCase(),
    { left: PAGE.left, top: 32, width: 350, height: 24 },
    { fontSize: 12, bold: true, color: COLORS.accent },
  );
  addText(
    slide,
    `slide-${planSlide.number}-number`,
    `${String(planSlide.number).padStart(2, "0")} / ${String(totalSlides).padStart(2, "0")}`,
    { left: 1080, top: 34, width: 124, height: 22 },
    { fontSize: 11, bold: true, color: COLORS.muted, alignment: "right" },
  );
}

function addTitle(slide, planSlide, top = 78, width = 1030, fontSize = 38) {
  addText(
    slide,
    `slide-${planSlide.number}-action-title`,
    planSlide.action_title,
    { left: PAGE.left, top, width, height: 104 },
    { fontSize, bold: true, color: COLORS.ink },
  );
}

function renderCover(slide, planSlide, deck) {
  addShape(
    slide,
    "cover-accent-plane",
    "rect",
    { left: 812, top: 0, width: 468, height: 720 },
    { fill: COLORS.ink },
  );
  addText(
    slide,
    "cover-kicker",
    String(planSlide.role || "NATIVE PPTX").toUpperCase(),
    { left: PAGE.left, top: 86, width: 360, height: 30 },
    { fontSize: 14, bold: true, color: COLORS.accent },
  );
  addText(
    slide,
    "cover-title",
    planSlide.action_title,
    { left: PAGE.left, top: 162, width: 650, height: 210 },
    { fontSize: 50, bold: true, color: COLORS.ink },
  );
  addText(
    slide,
    "cover-subtitle",
    planSlide.key_message,
    { left: PAGE.left, top: 410, width: 620, height: 98 },
    { fontSize: 22, color: COLORS.muted },
  );
  addText(
    slide,
    "cover-proof",
    "REAL TEXT\nREAL SHAPES\nREAL DATA",
    { left: 868, top: 162, width: 300, height: 210 },
    { fontSize: 26, bold: true, color: COLORS.white },
  );
  addText(
    slide,
    "cover-meta",
    deck.design_posture || "Knowledge Cat native case",
    { left: PAGE.left, top: 616, width: 620, height: 24 },
    { fontSize: 12, color: COLORS.muted },
  );
}

function renderStatement(slide, planSlide, totalSlides) {
  addChrome(slide, planSlide, totalSlides);
  addTitle(slide, planSlide, 86, 1040, 40);
  const native = planSlide.native_content || {};
  addText(
    slide,
    `slide-${planSlide.number}-stat`,
    native.stat || "4×",
    { left: PAGE.left, top: 250, width: 270, height: 150 },
    { fontSize: 88, bold: true, color: COLORS.accent },
  );
  addText(
    slide,
    `slide-${planSlide.number}-message`,
    planSlide.key_message,
    { left: 390, top: 250, width: 760, height: 130 },
    { fontSize: 27, color: COLORS.ink },
  );
  const items = native.items || planSlide.evidence || [];
  const text = items.slice(0, 4).map((item, index) => `${index + 1}. ${typeof item === "string" ? item : item.label}`).join("\n");
  addRule(slide, `slide-${planSlide.number}-rule`, 390, 420, 760, COLORS.accent, 3);
  addText(
    slide,
    `slide-${planSlide.number}-items`,
    text,
    { left: 390, top: 454, width: 760, height: 150 },
    { fontSize: 18, color: COLORS.muted },
  );
}

function renderChart(slide, planSlide, totalSlides) {
  addChrome(slide, planSlide, totalSlides);
  addTitle(slide, planSlide);
  const chart = planSlide.native_content?.chart;
  if (!chart || !Array.isArray(chart.categories) || !Array.isArray(chart.series)) {
    throw new Error(`Slide ${planSlide.number} uses chart layout without native_content.chart data.`);
  }
  addText(
    slide,
    `slide-${planSlide.number}-message`,
    planSlide.key_message,
    { left: PAGE.left, top: 202, width: 330, height: 130 },
    { fontSize: 22, color: COLORS.muted },
  );
  addRule(slide, `slide-${planSlide.number}-accent`, PAGE.left, 352, 260, COLORS.accent, 4);
  addText(
    slide,
    `slide-${planSlide.number}-evidence`,
    (planSlide.evidence || []).join("\n"),
    { left: PAGE.left, top: 380, width: 330, height: 130 },
    { fontSize: 16, color: COLORS.muted },
  );
  slide.charts.add(chart.type || "bar", {
    position: { left: 456, top: 210, width: 710, height: 385 },
    title: chart.title || "",
    titleTextStyle: { fontSize: 18, fill: COLORS.ink, bold: true },
    categories: chart.categories,
    series: chart.series.map((series, index) => ({
      name: series.name,
      values: series.values,
      fill: series.fill || (index === 0 ? COLORS.accent : COLORS.blue),
    })),
    hasLegend: chart.series.length > 1,
    legend: { position: "bottom", textStyle: { fontSize: 16, fill: COLORS.muted } },
    barOptions: { direction: "column", grouping: "clustered", gapWidth: 62 },
    dataLabels: { showValue: true, position: "outEnd", textStyle: { fontSize: 16, fill: COLORS.ink } },
    yAxis: {
      visible: true,
      min: 0,
      textStyle: { fontSize: 16, fill: COLORS.muted },
      majorGridlines: { style: "solid", fill: COLORS.line, width: 1 },
    },
    xAxis: { visible: true, textStyle: { fontSize: 16, fill: COLORS.ink } },
    chartFill: "none",
    chartLine: { style: "solid", fill: "none", width: 0 },
    plotAreaFill: "none",
    plotAreaLine: { style: "solid", fill: "none", width: 0 },
  });
}

function renderTable(slide, planSlide, totalSlides) {
  addChrome(slide, planSlide, totalSlides);
  addTitle(slide, planSlide);
  const tableData = planSlide.native_content?.table;
  if (!tableData || !Array.isArray(tableData.headers) || !Array.isArray(tableData.rows)) {
    throw new Error(`Slide ${planSlide.number} uses table layout without native_content.table data.`);
  }
  addText(
    slide,
    `slide-${planSlide.number}-message`,
    planSlide.key_message,
    { left: PAGE.left, top: 188, width: 1080, height: 58 },
    { fontSize: 20, color: COLORS.muted },
  );
  const values = [tableData.headers, ...tableData.rows];
  const table = slide.tables.add({
    rows: values.length,
    columns: tableData.headers.length,
    left: PAGE.left,
    top: 272,
    width: PAGE.width,
    height: Math.min(300, values.length * 54),
    values,
  });
  table.styleOptions = { headerRow: true, bandedRows: true };
  table.borders.assign({ style: "solid", fill: COLORS.line, width: 1 });
  for (let column = 0; column < tableData.headers.length; column += 1) {
    const cell = table.getCell(0, column);
    cell.fill = COLORS.ink;
    cell.text.style = { fontSize: 16, bold: true, color: COLORS.white };
  }
  for (let row = 1; row < values.length; row += 1) {
    for (let column = 0; column < tableData.headers.length; column += 1) {
      const cell = table.getCell(row, column);
      cell.fill = row % 2 === 0 ? COLORS.pale : COLORS.white;
      cell.text.style = { fontSize: 16, color: COLORS.ink };
    }
  }
}

function renderProcess(slide, planSlide, totalSlides) {
  addChrome(slide, planSlide, totalSlides);
  addTitle(slide, planSlide);
  const steps = planSlide.native_content?.steps || [];
  if (steps.length < 3) {
    throw new Error(`Slide ${planSlide.number} uses process layout but has fewer than 3 steps.`);
  }
  const left = PAGE.left + 20;
  const top = 272;
  const gap = 26;
  const width = (PAGE.width - 40 - gap * (steps.length - 1)) / steps.length;
  addRule(slide, `slide-${planSlide.number}-process-line`, left + 28, top + 42, PAGE.width - 96, COLORS.line, 3);
  steps.forEach((step, index) => {
    const x = left + index * (width + gap);
    addShape(slide, `slide-${planSlide.number}-step-${index + 1}-node`, "ellipse", { left: x, top: top + 17, width: 50, height: 50 }, { fill: index === steps.length - 1 ? COLORS.accent : COLORS.ink });
    addText(slide, `slide-${planSlide.number}-step-${index + 1}-number`, String(index + 1), { left: x, top: top + 27, width: 50, height: 24 }, { fontSize: 15, bold: true, color: COLORS.white, alignment: "center" });
    addText(slide, `slide-${planSlide.number}-step-${index + 1}-title`, step.title, { left: x, top: top + 92, width, height: 62 }, { fontSize: 20, bold: true, color: COLORS.ink });
    addText(slide, `slide-${planSlide.number}-step-${index + 1}-detail`, step.detail || "", { left: x, top: top + 162, width, height: 116 }, { fontSize: 16, color: COLORS.muted });
  });
}

function renderClosing(slide, planSlide, deck) {
  addShape(slide, "closing-bg", "rect", { left: 0, top: 0, width: 1280, height: 720 }, { fill: COLORS.ink });
  addText(slide, "closing-kicker", String(planSlide.role || "HANDOFF").toUpperCase(), { left: PAGE.left, top: 82, width: 300, height: 28 }, { fontSize: 14, bold: true, color: COLORS.accent });
  addText(slide, "closing-title", planSlide.action_title, { left: PAGE.left, top: 164, width: 1000, height: 180 }, { fontSize: 48, bold: true, color: COLORS.white });
  addRule(slide, "closing-rule", PAGE.left, 390, 220, COLORS.accent, 5);
  addText(slide, "closing-message", planSlide.key_message, { left: PAGE.left, top: 430, width: 830, height: 100 }, { fontSize: 23, color: "#D8E0E7" });
  addText(slide, "closing-meta", deck.title, { left: PAGE.left, top: 620, width: 700, height: 24 }, { fontSize: 12, color: "#A9B5C0" });
}

function renderFallback(slide, planSlide, totalSlides) {
  addChrome(slide, planSlide, totalSlides);
  addTitle(slide, planSlide);
  addText(slide, `slide-${planSlide.number}-message`, planSlide.key_message, { left: PAGE.left, top: 235, width: 640, height: 140 }, { fontSize: 27, color: COLORS.ink });
  addRule(slide, `slide-${planSlide.number}-rule`, PAGE.left, 410, 280, COLORS.accent, 4);
  addText(slide, `slide-${planSlide.number}-evidence`, (planSlide.evidence || []).join("\n"), { left: PAGE.left, top: 444, width: 720, height: 120 }, { fontSize: 17, color: COLORS.muted });
  addText(slide, `slide-${planSlide.number}-visual-intent`, planSlide.visual, { left: 865, top: 250, width: 290, height: 230 }, { fontSize: 20, bold: true, color: COLORS.blue, alignment: "right" });
}

function buildPresentation(Presentation, plan) {
  if (plan.deck?.output_lane !== "native-pptx") {
    throw new Error(`Expected deck.output_lane native-pptx, got ${plan.deck?.output_lane}`);
  }
  if (!Array.isArray(plan.slides) || plan.slides.length === 0) {
    throw new Error("Plan must contain at least one slide.");
  }
  const presentation = Presentation.create({ slideSize: SLIDE_SIZE });
  const totalSlides = plan.slides.length;
  for (const planSlide of plan.slides) {
    const slide = presentation.slides.add();
    slide.background.fill = COLORS.paper;
    const kind = planSlide.native_content?.kind || planSlide.layout || "default";
    if (kind === "cover") renderCover(slide, planSlide, plan.deck);
    else if (kind === "statement") renderStatement(slide, planSlide, totalSlides);
    else if (kind === "chart") renderChart(slide, planSlide, totalSlides);
    else if (kind === "table") renderTable(slide, planSlide, totalSlides);
    else if (kind === "process") renderProcess(slide, planSlide, totalSlides);
    else if (kind === "closing") renderClosing(slide, planSlide, plan.deck);
    else renderFallback(slide, planSlide, totalSlides);
    slide.speakerNotes.textFrame.setText(planSlide.speaker_note || planSlide.key_message);
    slide.speakerNotes.setVisible(true);
  }
  return presentation;
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    console.log("Usage: build_native_pptx.mjs --plan <deck-plan.json> --output <deck.pptx> --workspace <artifact-workspace> [--preview-dir <dir>] [--inspection <file>]");
    return;
  }
  const planPath = requireString(args, "plan");
  const outputPath = requireString(args, "output");
  const workspace = requireString(args, "workspace");
  const previewDir = args["preview-dir"] ? path.resolve(args["preview-dir"]) : path.join(path.dirname(outputPath), "screenshots");
  const inspectionPath = args.inspection ? path.resolve(args.inspection) : path.join(path.dirname(outputPath), "inspection.ndjson");
  await fs.mkdir(workspace, { recursive: true });
  await fs.mkdir(path.dirname(outputPath), { recursive: true });
  await fs.mkdir(previewDir, { recursive: true });

  const plan = JSON.parse(await fs.readFile(planPath, "utf8"));
  const { FileBlob, Presentation, PresentationFile } = await importArtifactTool(workspace);
  const presentation = buildPresentation(Presentation, plan);
  const pptx = await PresentationFile.exportPptx(presentation);
  await pptx.save(outputPath);
  await fs.rm(`${outputPath}.inspect.ndjson`, { force: true });

  const reopened = await PresentationFile.importPptx(await FileBlob.load(outputPath));
  const inspection = await reopened.inspect({
    kind: "slide,textbox,shape,chart,table,notes",
    maxChars: 100000,
  });
  await fs.writeFile(inspectionPath, inspection.ndjson, "utf8");

  const renderedSlidePaths = [];
  for (const [index, slide] of reopened.slides.items.entries()) {
    const stem = `slide-${String(index + 1).padStart(2, "0")}`;
    const previewPath = path.join(previewDir, `${stem}.png`);
    await writeBlob(previewPath, await reopened.export({ slide, format: "png", scale: 1 }));
    renderedSlidePaths.push(previewPath);
    const layout = await slide.export({ format: "layout" });
    await fs.writeFile(path.join(previewDir, `${stem}.layout.json`), await layout.text(), "utf8");
  }
  await renderContactSheet(Presentation, renderedSlidePaths, path.join(previewDir, "contact-sheet.png"));

  console.log(`Created native PPTX: ${outputPath}`);
  console.log(`Rendered previews: ${previewDir}`);
  console.log(`Inspection: ${inspectionPath}`);
}

main().catch((error) => {
  console.error(error.stack || error.message || String(error));
  process.exitCode = 1;
});
