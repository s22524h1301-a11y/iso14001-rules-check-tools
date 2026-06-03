# ISO 14001 Rules Check Tools

Current version: `v0.2.0`

Language / 語言: [English](#english) | [中文](#中文)

---

<a id="english"></a>
## English

ISO 14001 Rules Check Tools is a CLI utility for analyzing selectable-text PDFs and scanned PDFs, then suggesting which ISO 14001 clauses may apply to each section of the document.

This repository is the standalone ISO 14001 version of the clause-checking tool. `v0.2.0` expands the reporting layer with CSV output and improves the clause catalog/ranking while keeping the pipeline explainable.

### What it does

- Reads text from selectable-text PDF files
- Falls back to OCR when a PDF has no extractable text
- Splits the document into sections or subsections
- Suggests possible ISO 14001 clause matches for each section
- Exports results as plain text, JSON, or CSV

### Scope

- Input: PDF
- PDF types: selectable-text electronic PDFs and scanned PDFs with OCR fallback
- Output: likely ISO 14001 clause matches per section
- Current focus: a stable, explainable MVP with spreadsheet-friendly reporting

### Installation

Requires Python 3.12 or later.

```bash
pip install -e .
```

If you want to run tests:

```bash
pip install -e ".[dev]"
```

### Usage

Show CLI help:

```bash
python -m iso14001_rules_check_tools --help
```

Analyze a PDF with text output:

```bash
python -m iso14001_rules_check_tools path/to/document.pdf
```

Analyze a PDF with JSON output:

```bash
python -m iso14001_rules_check_tools --json path/to/document.pdf
```

Analyze a PDF with CSV output:

```bash
python -m iso14001_rules_check_tools --csv path/to/document.pdf
```

The CLI prints section headings, matched clause IDs, and section bodies by default. Use `--json` or `--csv` to emit structured output instead.

### Current progress

- [x] Project scaffold
- [x] CLI entry point
- [x] PDF text extraction
- [x] OCR fallback for scanned PDFs
- [x] Section splitting
- [x] Text, JSON, and CSV reporting pipeline
- [x] Basic tests
- [x] Initial ISO 14001 clause catalog structure
- [ ] ISO 14001 clause coverage refinement
- [ ] Domain-specific matching improvements

### Open issues

- Clause matching still needs tuning to reduce false positives
- PDF layouts vary a lot, so structure parsing will need continued refinement
- This is still a CLI tool, not a web UI
- The clause catalog will need to grow as we refine environmental-use cases

### Roadmap

1. Improve PDF text extraction
2. Improve section and subsection splitting
3. Refine the ISO 14001 clause catalog
4. Improve matching precision and reporting
5. Add richer export formats if needed
6. Consider a web UI later

### Project status

This is an MVP in active development.

The main goal is to keep the "PDF text analysis + ISO 14001 clause mapping" pipeline stable and explainable, then expand capability gradually.

For development and version rules, see [docs/VERSIONING.md](docs/VERSIONING.md).

### Release status

- `v0.2.0` adds CSV reporting and improves clause catalog/ranking for spreadsheet-friendly review.
- The core pipeline remains in place, and the catalog will continue to be refined for environmental management use cases.

---

<a id="中文"></a>
## 中文

ISO 14001 Rules Check Tools 是一個 CLI 工具，用來分析可直接擷取文字的 PDF 與掃描式 PDF，並推測文件各章節可能對應的 ISO 14001 條文。

這個 repo 是獨立的 ISO 14001 版本。`v0.2.0` 擴充了 CSV 報表輸出，也改善了條文 catalog 與 ranking，同時維持流程可理解、可驗證。

### 主要功能

- 讀取可擷取文字的 PDF
- 當 PDF 沒有可擷取文字時，自動切換 OCR
- 將文件切分成章節或小節
- 為每個章節建議可能的 ISO 14001 條文對應
- 匯出純文字、JSON 或 CSV 結果

### 範圍

- 輸入：PDF
- 支援 PDF 類型：可擷取文字的電子檔與需要 OCR 備援的掃描式 PDF
- 輸出：每個章節的 ISO 14001 條文建議
- 目前重點：穩定、可解釋、方便試算表檢視的 MVP

### 安裝

需要 Python 3.12 或以上。

```bash
pip install -e .
```

若要執行測試：

```bash
pip install -e ".[dev]"
```

### 使用方式

顯示 CLI 說明：

```bash
python -m iso14001_rules_check_tools --help
```

以文字格式分析 PDF：

```bash
python -m iso14001_rules_check_tools path/to/document.pdf
```

以 JSON 格式分析 PDF：

```bash
python -m iso14001_rules_check_tools --json path/to/document.pdf
```

以 CSV 格式分析 PDF：

```bash
python -m iso14001_rules_check_tools --csv path/to/document.pdf
```

CLI 預設會輸出章節標題、匹配到的條文 ID 與章節內容。若要結構化輸出，可以使用 `--json` 或 `--csv`。

### 目前進度

- [x] 專案骨架
- [x] CLI 入口
- [x] PDF 文字擷取
- [x] 掃描式 PDF 的 OCR 備援
- [x] 章節切分
- [x] 文字、JSON 與 CSV 報表管線
- [x] 基礎測試
- [x] 初始 ISO 14001 條文 catalog 結構
- [ ] ISO 14001 條文覆蓋率細化
- [ ] 領域化比對精度提升

### 已知限制

- 條文匹配仍需要持續微調，以降低誤判
- PDF 版型差異很大，章節解析仍會持續改善
- 目前仍是 CLI 工具，尚未有 Web UI
- 條文 catalog 會隨環境管理案例逐步擴充

### 路線圖

1. 改善 PDF 文字擷取
2. 改善章節與小節切分
3. 細化 ISO 14001 條文 catalog
4. 提升比對精度與報表可讀性
5. 視需要再增加更多匯出格式
6. 之後再考慮 Web UI

### 專案狀態

這是一個持續開發中的 MVP。

目前的核心目標是維持「PDF 文字分析 + ISO 14001 條文對應」流程穩定且可解釋，再逐步擴充能力。

開發與版本規則請見 [docs/VERSIONING.md](docs/VERSIONING.md)。

### Release 狀態

- `v0.2.0` 新增 CSV 報表，並改善條文 catalog / ranking，方便用試算表進行檢視。
- 核心流程維持不變，條文 catalog 會持續針對環境管理情境調整與擴充。
