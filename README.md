# ISO 14001 Rules Check Tools

Current version: `v0.1.0`

Language / 語言: [English](#english) | [繁體中文](#traditional-chinese)

---

<a id="english"></a>
## English

ISO 14001 Rules Check Tools is a CLI for ISO 14001 document review. It is scoped to ISO 14001 only and does not cover ISO 9001.

### v0.1.0 scope

- Selectable-text PDFs
- Scanned PDFs with OCR fallback
- ISO 14001:2015 clause mapping
- Text and JSON output

### What it does

- Reads PDF content from selectable-text PDFs first
- Falls back to OCR for scanned PDFs when text is not available
- Splits the document into sections
- Suggests likely ISO 14001 clause matches for each section
- Exports results as plain text or JSON

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

The CLI prints section headings, matched clause IDs, and section bodies by default. Use `--json` to emit structured JSON output instead.

### Current progress

- [x] Project scaffold
- [x] CLI entry point
- [x] PDF text extraction
- [x] Section splitting
- [x] Text and JSON reporting pipeline
- [x] Basic tests
- [x] Initial ISO 14001 clause catalog structure
- [ ] ISO 14001 clause coverage refinement
- [ ] OCR fallback implementation, planned as part of v0.1.0
- [ ] Domain-specific matching improvements

### Project status

This is an MVP in active development.

The current goal is to keep the ISO 14001 PDF analysis pipeline stable and explainable, then expand capability gradually.

For development and version rules, see [docs/VERSIONING.md](docs/VERSIONING.md).

### Release status

- `v0.1.0` is the first ISO 14001 release scope for selectable-text PDFs, scanned PDFs with OCR fallback, ISO 14001:2015, and text/JSON output.
- The clause catalog will continue to be refined for environmental management use cases.

<a id="traditional-chinese"></a>
## 繁體中文

ISO 14001 Rules Check Tools 是一個用來進行 ISO 14001 文件檢查的 CLI 工具。這個專案只涵蓋 ISO 14001，不包含 ISO 9001。

### v0.1.0 範圍

- 可選取文字的 PDF
- 掃描式 PDF 與 OCR 備援
- ISO 14001:2015 條文對應
- 純文字與 JSON 輸出

### 功能說明

- 先讀取可選取文字的 PDF 內容
- 當掃描式 PDF 沒有可用文字時，會使用 OCR 備援
- 將文件切分成段落或小節
- 為每個段落找出可能對應的 ISO 14001 條文
- 輸出純文字或 JSON 報表

### 安裝

需要 Python 3.12 或更新版本。

```bash
pip install -e .
```

如果要執行測試：

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

CLI 預設會輸出段落標題、條文命中結果和段落內容；如果加上 `--json`，就會輸出結構化 JSON。

### 目前進度

- [x] 專案骨架
- [x] CLI 入口
- [x] PDF 文字擷取
- [x] 段落切分
- [x] 純文字與 JSON 報表流程
- [x] 基本測試
- [x] ISO 14001 條文 catalog 初始架構
- [ ] ISO 14001 條文覆蓋持續補齊
- [ ] OCR 備援實作
- [ ] 領域化匹配改善

### 專案狀態

目前仍處於 MVP 的持續開發階段。

現階段重點是先把 ISO 14001 PDF 分析流程維持穩定且可解釋，再逐步擴充功能。

開發與版本規則請見 [docs/VERSIONING.md](docs/VERSIONING.md)。

### 發佈狀態

- `v0.1.0` 是第一個 ISO 14001 發佈範圍，涵蓋可選取文字的 PDF、掃描式 PDF 的 OCR 備援、ISO 14001:2015，以及純文字 / JSON 輸出。
- 條文 catalog 之後會繼續依環境管理情境補強。
