# ISO 14001 Rules Check Tools

Current version: `v0.1.1`

Language / 語言: [English](#english) | [繁體中文](#traditional-chinese)

---

<a id="english"></a>
## English

ISO 14001 Rules Check Tools is a CLI utility for analyzing selectable-text PDFs and scanned PDFs with OCR fallback, then suggesting which ISO 14001 clauses may apply to each section of the document.

This repository is the starting point for the ISO 14001 version of the clause-checking tool. `v0.1.1` is an OCR stability patch for the existing ISO 14001-only workflow: it keeps the same scope, improves fallback behavior for scanned PDFs, and preserves the clause catalog based on the ISO 14001:2015 structure.

### What it does

- Reads text from selectable-text PDF files and falls back to OCR for scanned PDFs when text is not available
- Splits the document into sections or subsections
- Suggests possible ISO 14001 clause matches for each section
- Exports results as plain text or JSON

### Scope

- Input: PDF
- PDF types: selectable-text electronic PDFs and scanned PDFs with OCR fallback
- Output: likely ISO 14001 clause matches per section
- Current focus: a stable, explainable MVP with OCR fallback reliability

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

For development and version rules, see [docs/VERSIONING.md](/C:/Users/qc00/Documents/codex/iso14001-rules-check-tools/docs/VERSIONING.md)

### Release status

- `v0.1.0` is the first scaffold for the ISO 14001 project.
- `v0.1.1` is the first OCR stability patch for the ISO 14001-only workflow.
- The core pipeline is in place, but the clause catalog will continue to be refined for environmental management use cases.

---

<a id="traditional-chinese"></a>
## 繁體中文

ISO 14001 Rules Check Tools 是一個 CLI 工具，用來分析可選取文字 PDF 與需要 OCR 備援的掃描式 PDF，並找出文件中每個段落或小節可能對應哪些 ISO 14001 條文。

這個倉庫是 ISO 14001 版本條文檢查工具的起點。`v0.1.1` 是一個 OCR 穩定性修補版，重點仍然放在 ISO 14001-only 的工作流程：維持相同範圍、改善掃描 PDF 的 fallback 行為，並保留以 ISO 14001:2015 架構為基礎的條文 catalog。

### 這個工具會做什麼

- 先讀取可選取文字的 PDF，若沒有可用文字就改用 OCR 備援
- 將文件切成段落或小節
- 為每個段落列出可能對應的 ISO 14001 條文
- 輸出純文字報表或 JSON

### 支援範圍

- 輸入格式：PDF
- PDF 類型：可選取文字的電子檔與需要 OCR 備援的掃描式 PDF
- 輸出方向：每個段落或小節對應可能相關的 ISO 14001 條文
- 目前重點：先把流程做穩、做得容易理解，並強化 OCR fallback 穩定性

### 安裝

需要 Python 3.12 或以上。

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
- [ ] 領域化匹配改善

### 待解決問題

- 條文對應邏輯還需要持續調整，避免誤判
- 不同 PDF 排版差異很大，文件結構辨識還需要持續補強
- 目前是 CLI 工具，尚未加入視覺化介面或網頁版
- 條文 catalog 還要持續擴充，才能更貼近環境管理實務

### 路線圖

1. 完成 PDF 文字擷取
2. 完成段落 / 小節切分
3. 補齊 ISO 14001 條文 catalog
4. 提升比對精準度與報表品質
5. 視需要加入更完整的匯出格式
6. 後續再評估 Web UI

### 專案狀態

這是一個持續開發中的 MVP。

目前的重點是先把 "PDF 文字分析 + ISO 14001 條文對應" 這條主流程穩定下來，再逐步擴充功能。

開發與版本規則請見 [docs/VERSIONING.md](/C:/Users/qc00/Documents/codex/iso14001-rules-check-tools/docs/VERSIONING.md)

### 發佈狀態

- `v0.1.0` 是 ISO 14001 專案的第一個起始版本。
- `v0.1.1` 是第一個 OCR 穩定性修補版，維持 ISO 14001-only 範圍。
- 核心流程已經就位，但條文 catalog 還會繼續針對環境管理情境調整與擴充。
