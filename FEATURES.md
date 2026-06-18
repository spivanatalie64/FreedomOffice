# FreedomOffice Feature Map

> **Document Purpose:** This file maps every major Microsoft Office feature to its FreedomOffice equivalent. It serves as both a migration guide for users coming from Microsoft Office and a development roadmap for contributors.
>
> **Status Key:**
> - ✅ **Available** — Feature exists natively in FreedomOffice (inherited from LibreOffice)
> - ⚙️ **Via FOSS alternative** — Feature available through a free/open source integration
> - 🚧 **In development** — Feature is planned or partially implemented
> - 📌 **Not planned / alternative workflow** — No direct equivalent exists; a different approach is recommended

---

## Word Processing (FreedomWriter ↔ Microsoft Word)

FreedomWriter inherits the full word processing engine from LibreOffice Writer. It supports .docx, .doc, .odt, .rtf, .txt, and many other formats natively.

| MS Word Feature | Status | FreedomOffice Equivalent |
|----------------|--------|------------------------|
| **Track Changes / Review** | ✅ Available | Tools → Track Changes. Full redlining, accept/reject, comments in margins. Compatible with .docx tracked changes. |
| **Comments** | ✅ Available | Insert → Comment (Ctrl+Alt+C). Sidebar comments with reply threading. Round-trips with .docx. |
| **Mail Merge** | ✅ Available | Tools → Mail Merge Wizard. Supports data sources from spreadsheets, databases, and address books. |
| **Table of Contents** | ✅ Available | Insert → Table of Contents and Index. Auto-generated from heading styles. Multiple format presets. |
| **Footnotes/Endnotes** | ✅ Available | Insert → Footnote/Endnote. Full formatting and layout control. |
| **Citations & Bibliography** | ✅ Available | Insert → Table of Contents and Index → Bibliography Entry. Supports Zotero integration via extension. |
| **Indexing** | ✅ Available | Insert → Table of Contents and Index → Index. Multi-level index generation. |
| **Cross-references** | ✅ Available | Insert → Cross-Reference. Reference headings, bookmarks, figures, tables. |
| **Headers/Footers** | ✅ Available | Insert → Header/Footer. Different first page, odd/even pages. |
| **Page Numbering** | ✅ Available | Insert → Page Number. Skip first page, start at arbitrary number, format presets. |
| **Sections / Columns** | ✅ Available | Format → Columns. Section breaks via Insert → Section Break. Mixed layouts per page. |
| **Styles & Templates** | ✅ Available | Sidebar Styles panel (F11). Paragraph, character, page, frame, list styles. Full template system (.ott, .otp, .ots). |
| **SmartArt** | ⚙️ Via OLE | No native SmartArt equivalent, but Microsoft SmartArt renders correctly in .docx via OLE embedding. FreedomOffice has its own diagram tools (Insert → Object → Chart, Flowchart shapes). |
| **Equations** | ✅ Available | Insert → Object → Formula or Insert → Formula (Ctrl+Alt+O). MathML, LaTeX input, and GUI equation editor via FreedomEquation. |
| **Watermarks** | ✅ Available | Format → Watermark (or Insert → Watermark). Text/image watermarks behind content. |
| **Document Encryption** | ✅ Available | Tools → Protect Document. Password protection for open/modify. File → Save As → Save with password. |
| **Read Mode** | ✅ Available | View → Read Mode (or Ctrl+Shift+I). Full-screen, paginated reading view. |
| **Focus Mode** | ✅ Available | View → User Interface → Compact view or full-screen. Sidebar auto-hide options. |
| **Resume Reading** | ✅ Available | Remembered cursor position on document reopen. Bookmark support for explicit markers. |
| **Editor (Spelling/Grammar AI)** | ⚙️ Via opencode AI | FreedomOffice has built-in spell check (Hunspell) and grammar check (LightProof). The **Editor AI** experience is available via opencode AI integration — select text and invoke AI for advanced grammar, style, and clarity suggestions. |
| **Dictation** | ⚙️ Via Vosk / Whisper | Integrate via **Vosk** (offline, lightweight) or **Whisper.cpp** (higher accuracy). Voice input can pipe text directly into FreedomWriter via the operating system's text input method or a dedicated extension. |
| **Translator** | ⚙️ Via LibreTranslate | Run a local LibreTranslate server or use a public instance. FreedomWriter can integrate via macro or extension to send selected text for translation. |
| **AutoSummarize** | ⚙️ Via opencode AI | Select document text → invoke opencode AI with "summarize this" prompt. Can be scripted into a one-click macro. |
| **Researcher** | ⚙️ Via opencode AI + Web Search | Invoke opencode AI to research a topic. Combine with web search results via spruniversity (search twin) to provide cited sources inline. |
| **Designer** | ✅ Available (Fluent theme) | FreedomOffice applies the **FreedomOffice Fluent theme** — clean, modern design language. Document design suggestions are available via the sidebar (Properties → Page Style). |
| **Templates** | ✅ Available | File → New → Templates. Ships with built-in FOSS templates (.ott). Community template repository at freedomoffice.org/templates. |
| **Version History** | ⚙️ Via Nextcloud | Saved documents on Nextcloud get full version history with diff views. File → Versions in the Nextcloud web UI. Can be accessed directly from FreedomWriter via Nextcloud WebDAV mount. |
| **Co-authoring** | ⚙️ Via Collabora Online | Real-time collaborative editing when hosted on **Collabora Online** (based on LibreOffice Online technology). Multiple users edit simultaneously with cursor presence. Self-hosted or via a provider. |

---

## Spreadsheets (FreedomSheet ↔ Microsoft Excel)

FreedomSheet inherits the full Calc engine from LibreOffice. Supports .xlsx, .xls, .ods, .csv, .tsv, and many other formats.

| MS Excel Feature | Status | FreedomOffice Equivalent |
|------------------|--------|------------------------|
| **PivotTables** | ✅ Available | Data → PivotTable → Create. Drag-and-drop field layout. Grouping, filtering, sorting. Compatible with .xlsx pivot tables. |
| **Charts (all types)** | ✅ Available | Insert → Chart. Bar, line, pie, area, scatter, bubble, stock, radar, column, 3D variants. Fully customizable. |
| **Conditional Formatting** | ✅ Available | Format → Conditional Formatting. Color scales, data bars, icon sets, formula-based rules. |
| **Data Validation** | ✅ Available | Data → Validity. Dropdowns, number ranges, date limits, custom formulas. Input messages and error alerts. |
| **What-If Analysis (Goal Seek, Scenario Manager)** | ✅ Available | Tools → Goal Seek. Tools → Solver (for complex what-if). Tools → Scenarios for scenario management. |
| **Power Query** | ⚙️ Via Base + SQL | Power Query's ETL functionality is available through **LibreOffice Base** (connect to databases, query, transform) or direct SQL queries. For advanced data transformation, use Data → Sheet → Sheet from SQL or the built-in filter/sort/split tools. Python macros can replicate Power Query's M language. |
| **Power Pivot** | ⚙️ Via PivotTables | Power Pivot's in-memory analytics are handled by FreedomSheet's **PivotTable** engine with external data sources. Large datasets can be loaded via Data → Data Source. |
| **Dynamic Arrays** | ✅ Available | FreedomSheet supports array formulas (Ctrl+Shift+Enter) and newer dynamic array behavior via the `ARRAY()` function and formula auto-expansion. |
| **XLOOKUP, LET, LAMBDA functions** | ⚙️ Partial / Alternative | `XLOOKUP` is available as a native function. `LET` and `LAMBDA` are not natively implemented but can be replicated via **named expressions** and **User-Defined Functions** in LibreOffice Basic or Python macros. |
| **Sparklines** | ✅ Available | Insert → Sparkline. Line, column, win/loss sparklines in cells. |
| **Slicers / Timelines** | ⚙️ Partial | Slicers for PivotTables are available (Data → PivotTable → Slicer). Timeline date filtering is not a native control but can be achieved via date group filters on PivotTable fields. |
| **Forecast Sheets** | ✅ Available | Data → Statistics → Forecast. Linear and exponential smoothing forecast models with confidence intervals. |
| **Stock data types** | ⚙️ Via Yahoo Finance / Alpha Vantage | Use the **Yahoo Finance** or **Alpha Vantage API** via a macro or extension. A Python macro can fetch real-time/near-real-time stock data and populate cells. The `STOCKHISTORY` function is available in Calc via extensions. |
| **Geography data types** | ⚙️ Via OpenStreetMap | OpenStreetMap data can be queried via the **Overpass API** using Python macros or extensions. FreedomSheet can import geo data as structured tables. |
| **Macros (VBA-compatible)** | ✅ Available | Tools → Macros → Organize Macros → LibreOffice Basic. VBA compatibility layer handles many common .xlsm macros. **LibreOffice Basic** is the primary macro language. Python, Java, JavaScript macros also supported. |
| **Solver Add-in** | ✅ Available | Tools → Solver. Linear and nonlinear optimization. Supports evolutionary algorithms and constraint-based solving. |

---

## Presentations (FreedomShow ↔ Microsoft PowerPoint)

FreedomShow inherits the full Impress engine from LibreOffice. Supports .pptx, .ppt, .odp, and many other formats.

| MS PowerPoint Feature | Status | FreedomOffice Equivalent |
|----------------------|--------|------------------------|
| **Slide Masters** | ✅ Available | View → Slide Master. Edit master slides, layouts, and background styles. Multiple masters per presentation. |
| **Transitions** | ✅ Available | Slide → Slide Transition. Fade, dissolve, push, wipe, zoom, blinds, checkerboard, comb, cover, uncover, and many more. Custom speed and sound options. |
| **Animations** | ✅ Available | Slide → Animation. Entrance, emphasis, exit, and motion path animations. Trigger on click, with previous, after previous. Custom timing and property animation. |
| **Morph transition** | ⚙️ Cross-fade alternative | FreedomShow does not have a 1:1 Morph transition. **Cross-fade** between slides achieves a similar visual effect. For advanced morph-like animation, duplicate the slide and animate object properties manually. |
| **Presenter View** | ✅ Available | Slide Show → Presenter View (F5). Shows current slide, next slide, speaker notes, timer, and slide navigator. |
| **Recording** | ✅ Available | Slide Show → Record Slideshow. Record narration, slide timings, and pointer movements. |
| **Rehearse Timings** | ✅ Available | Slide Show → Rehearse Timings. Advance through slides while timings are recorded. |
| **Export to video** | ✅ Available | File → Export → Export as Video. MP4 output with slide timings, transitions, and narration. |
| **Designer** | ✅ Available (Fluent theme) | The **FreedomOffice Fluent theme** applies modern, clean slide designs. Slide → Slide Properties → Design Template for quick styling. |
| **Icons** | ⚙️ Via FreedomOffice Fluent icons | FreedomOffice ships with a **Fluent icon set** — modern, consistent vector icons for shapes, actions, and UI. Available via Insert → Image → Icons. |
| **3D Models** | ⚙️ Partial (GLTF support) | FreedomOffice supports 3D model rendering via **GLTF** files. Insert 3D models as objects. Rotation, scaling, positioning. Not yet at PowerPoint's level of 3D animation polish, but fully functional. |
| **Zoom feature** | ✅ Available (Slide navigation) | Slide Show → Navigation Panel. Thumbnail grid view for jumping between sections. Alternatively, use a hyperlinked table of contents slide. |
| **Subtitles** | ⚙️ Via Whisper integration | Real-time subtitles during presentations can be achieved by piping audio to **Whisper.cpp** and displaying captions in a secondary window or overlay. Scripted integration available. |

---

## Database (FreedomBase ↔ Microsoft Access)

FreedomBase inherits the full Base engine from LibreOffice.

| MS Access Feature | Status | FreedomOffice Equivalent |
|------------------|--------|------------------------|
| **Table Designer** | ✅ Available | Tables → Create Table in Design View. Field names, types, properties, primary keys, indexing. |
| **Queries (SQL)** | ✅ Available | Queries → Create Query in SQL View. Full SQL editing with syntax highlighting. Query wizard for visual building. |
| **Forms** | ✅ Available | Forms → Create Form in Design View. Drag-and-drop form builder with field binding. Wizards for quick forms. |
| **Reports** | ✅ Available | Reports → Create Report in Design View. Grouping, sorting, summaries, headers/footers. Wizards for quick reports. |
| **Macros** | ✅ Available | Tools → Macros. LibreOffice Basic, Python, JavaScript macros with database event triggers. |
| **Relationships** | ✅ Available | Tools → Relationships. Visual editor for table joins, foreign keys, cardinality. |
| **Import/Export** | ✅ Available | File → Open/Save. Import from Access (.mdb/.accdb), CSV, Excel, dBase, ODBC. Export to all supported formats. |
| **Linked Tables** | ✅ Available | File → New → Database → Connect to existing database. Link to external databases (MySQL, PostgreSQL, SQLite, ODBC). |
| **ODBC/JDBC Connections** | ✅ Available | File → New → Database → Connect to ODBC/JDBC. Supports MySQL, PostgreSQL, Oracle, SQL Server, SQLite, and more. |

---

## Drawing (FreedomDraw ↔ Microsoft Visio)

FreedomDraw inherits the full Draw engine from LibreOffice.

| MS Visio Feature | Status | FreedomOffice Equivalent |
|-----------------|--------|------------------------|
| **Stencils / Templates** | ✅ Available | File → New → Drawing. Template gallery for flowcharts, diagrams, maps, and more. Custom stencil sets (.sda). |
| **Connectors** | ✅ Available | Insert → Connector. Dynamic connectors between shapes that reroute on move. Glue points for precise attachment. |
| **Layers** | ✅ Available | View → Sidebar → Layers. Show/hide, lock/unlock, print control per layer. |
| **Shape Data** | ✅ Available | Right-click shape → Description. Custom properties and metadata per shape. |
| **Export to Vector Formats** | ✅ Available | File → Export. SVG, EPS, PDF, EMF, WMF. Full vector fidelity. |
| **Cross-functional Flowcharts** | ✅ Available | Flowchart shapes (swimlanes) available in the drawing toolbar. Insert → Shapes → Flowchart. |
| **Network Diagrams** | ✅ Available | Shape libraries for network equipment, cabling, and topology diagrams. Community stencils available. |
| **Floor Plans** | ✅ Available | Shape libraries for architectural elements. Scale drawing support with dimension lines. |

---

## Equation Editor (FreedomEquation ↔ Microsoft Equation Editor)

FreedomEquation inherits the full Math engine from LibreOffice.

| MS Equation Feature | Status | FreedomOffice Equivalent |
|--------------------|--------|------------------------|
| **Visual equation editor** | ✅ Available | Insert → Object → Formula (or standalone: Applications → FreedomEquation). GUI element palette. |
| **MathML support** | ✅ Available | Full MathML import/export. Copy/paste MathML between applications. |
| **LaTeX input** | ✅ Available | Insert → Formula → Type LaTeX directly. Real-time preview. |
| **All equation types** | ✅ Available | Algebra, calculus, trigonometry, matrices, integrals, sums, limits, set theory, logic, symbols, Greek alphabet, operators, functions, brackets, arrows. Anything in mathematical notation. |
| **Handwriting recognition** | 📌 Not planned | Use a third-party LaTeX handwriting tool (e.g., MathPix) and paste the LaTeX output into FreedomEquation. |

---

## Services & Cloud Integration

| MS Service | FOSS Alternative | Integration Method | Status |
|-----------|-----------------|-------------------|--------|
| **OneDrive** | **Nextcloud** | WebDAV protocol built into FreedomOffice. File → Open → Remote Files. Connect Nextcloud as a WebDAV server. | ✅ Available |
| **SharePoint** | **Nextcloud** | WebDAV or Nextcloud Desktop Sync. Document libraries supported via WebDAV mount. | ✅ Available |
| **Teams** | **Element / Matrix** | Desktop integration via Element desktop app. Invite FreedomOffice link handler for document types. | ⚙️ Via desktop integration |
| **Outlook** | **Thunderbird** | FreedomOffice registers as the default mailto: handler. Thunderbird + FreedomOffice companion for mail merge and document sharing. | ⚙️ Via desktop integration |
| **OneNote** | **Joplin / Nextcloud Notes** | Joplin for rich note-taking with .md/.jex export. Nextcloud Notes for collaborative markdown. Link from FreedomOffice via hyperlinks or embedded objects. | ⚙️ Via FOSS alternative |
| **Planner** | **OpenProject / WeKan** | Web-based project management. FreedomOffice documents can be linked from tasks. OpenProject has direct document upload. | ⚙️ Via web integration |
| **Power Automate** | **n8n / Node-RED** | API-based workflow automation. FreedomOffice documents can trigger workflows (new file, modification, etc.) via n8n webhooks or Node-RED flows. | ⚙️ Via API integration |
| **Power BI** | **Apache Superset / Metabase** | Export FreedomSheet data as OData or CSV → import into Superset/Metabase for dashboards and visualization. | ⚙️ Via data export |
| **Microsoft Forms** | **Nextcloud Forms / LimeSurvey** | Web-based form creation. Results export to FreedomSheet for analysis. | ⚙️ Via web link |
| **To Do** | **Vikunja / Nextcloud Tasks** | Web-based task management. Tasks can reference FreedomOffice documents via links. | ⚙️ Via web link |
| **Bookings** | **Nextcloud Calendar** | Calendar-based appointment booking. Export calendar events to FreedomWriter documents for reports. | ⚙️ Via web link |
| **Clipchamp** | **Kdenlive / Olive** | Professional video editing on desktop. Export finished videos for embedding in FreedomShow presentations. | ⚙️ Via desktop integration |
| **Stream** | **PeerTube / Jellyfin** | Self-hosted video platform. Embed videos in FreedomShow or link from FreedomWriter documents. | ⚙️ Via web link |

---

## AI Features (Copilot Replacement)

FreedomOffice does not have a built-in Copilot. Instead, it integrates with **opencode AI** — the same AI agent writing this document — and other FOSS AI tools to provide equivalent capabilities.

| MS Copilot Feature | FreedomOffice Implementation | Details |
|-------------------|----------------------------|---------|
| **Chat with AI** | **opencode AI integration** | Invoke opencode AI directly from FreedomOffice. Ask questions, get answers, generate content. The AI has full context of your document. |
| **Draft a document** | **opencode custom prompt** | "Draft a business letter about [topic]." opencode AI generates the content inline or in a new document. |
| **Summarize document** | **opencode AI with context** | "Summarize this document in 3 paragraphs." The AI reads the current document and produces a summary. |
| **Analyze spreadsheet** | **opencode AI + Python** | "Analyze this data and tell me trends." opencode AI writes and executes Python analysis on FreedomSheet data using pandas/numpy. Results returned as text or charts. |
| **Create presentation** | **opencode AI + script** | "Create a 10-slide presentation about [topic]." opencode AI generates slide content, applies themes, and assembles the presentation via the Universal Network Objects (UNO) API. |
| **Generate images** | **opencode + Stable Diffusion** | "Generate an image of [description]." opencode calls a local Stable Diffusion instance (Automatic1111 / ComfyUI) and inserts the result into the document. |
| **Translate** | **LibreTranslate API** | "Translate this paragraph to Spanish." opencode AI sends text to a local LibreTranslate server and replaces/inserts the translation. |
| **Dictation** | **Whisper.cpp** | Speak → Whisper.cpp transcribes → text appears in document. Offline, private, no data leaves the machine. |
| **Read Aloud** | **Festival / eSpeak** | Text-to-speech using Festival (high-quality) or eSpeak (lightweight). Select text → hear it read aloud. |
| **Document Q&A** | **opencode AI + RAG** | "What does the contract say about termination?" opencode AI reads your documents and answers questions with citations. Retrieval-Augmented Generation over your local document store. |
| **Smart Compose** | **opencode AI autocomplete** | Start typing → opencode AI suggests completions. Context-aware sentence and paragraph completion. |
| **Data Pattern Detection** | **opencode AI + pandas** | "Find anomalies in this dataset." The AI analyzes data with Python and highlights cells, creates PivotTables, or writes a summary. |

---

## Application Shell & Common Features

Features shared across all FreedomOffice applications.

| Feature | Status | Details |
|---------|--------|---------|
| **Ribbon UI** | ✅ Available (NotebookBar) | FreedomOffice uses the **NotebookBar** — a tabbed toolbar interface. Switch between Tabbed, Tabbed Compact, Single Toolbar, and Classic views. View → User Interface. |
| **Tabbed browsing** | ✅ Available | Multiple documents in a single window with tabs. Ctrl+Tab to switch. |
| **Quick Access Toolbar** | ✅ Available | Custom toolbar above the ribbon. Add your most-used commands. |
| **Dark Mode** | ✅ Available | Tools → Options → FreedomOffice → Application Colors → Dark theme. Also follows system theme. |
| **PDF Export** | ✅ Available | File → Export as PDF. Full PDF/A compliance. Hyperlinks, bookmarks, forms, comments export options. |
| **PDF Import** | ✅ Available | File → Open → PDF file. Editable text and layout. Draw-based editing for complex PDFs. |
| **Accessibility** | ✅ Available | Screen reader support (Orca on Linux, NVDA/JAWS on Windows). High contrast themes. Keyboard navigation. |
| **Extension Manager** | ✅ Available | Tools → Extension Manager. Browse and install extensions from the FreedomOffice extension repository. |
| **Macro Recording** | ✅ Available | Tools → Macros → Record Macro. Recorded as LibreOffice Basic. Edit and assign to keyboard shortcuts/toolbar buttons. |
| **Spell Check** | ✅ Available | Hunspell-based. Grammar check via LightProof. On-the-fly underlining. Multiple language dictionaries. |
| **Thesaurus** | ✅ Available | Right-click → Thesaurus. Synonym lookup with wordnet-based dictionary. |
| **AutoCorrect** | ✅ Available | Tools → AutoCorrect. Word completion, replacements, exceptions. |
| **Multi-platform** | ✅ Available | Linux, Windows, macOS. Same feature set on all platforms. |
| **Mobile view** | 🚧 In development | FreedomOffice Online (Collabora-based) provides mobile web access. Native mobile apps are planned. |

---

## File Format Support

| Format | Read | Write | Notes |
|--------|------|-------|-------|
| **.docx** (Office Open XML) | ✅ | ✅ | Full round-trip with tracked changes, comments, formatting, images |
| **.doc** (Word 97-2003) | ✅ | ✅ | Legacy binary format |
| **.docm** (macro-enabled) | ✅ | ✅ | VBA macros executed in compatibility mode |
| **.dotx** (template) | ✅ | ✅ | Template support |
| **.xlsx** | ✅ | ✅ | Full round-trip with pivot tables, charts, conditional formatting |
| **.xls** (Excel 97-2003) | ✅ | ✅ | Legacy binary format |
| **.xlsm** (macro-enabled) | ✅ | ✅ | VBA compatibility |
| **.pptx** | ✅ | ✅ | Full round-trip with animations, transitions, embedded media |
| **.ppt** (PowerPoint 97-2003) | ✅ | ✅ | Legacy binary format |
| **.ppsx** (slideshow) | ✅ | ✅ | Slideshow mode |
| **.odt / .ods / .odp / .odb / .odg / .odf** | ✅ | ✅ | **Native format** — Open Document Format |
| **.pdf** | ✅ | ✅ | Import editable; export with full options |
| **.rtf** | ✅ | ✅ | Rich Text Format |
| **.html / .htm** | ✅ | ✅ | Web documents |
| **.epub** | ❌ Read-only | ✅ | Export only (Writer → EPUB) |
| **.txt** | ✅ | ✅ | Plain text with encoding options |
| **.csv / .tsv** | ✅ | ✅ | Configurable delimiters, encoding |
| **.xml** | ✅ | ✅ | Various XML schemas |
| **.svg** | ✅ | ❌ Native | Import as vector graphic. Export via Draw |
| **.wmf / .emf** | ✅ | ✅ | Windows Metafile support |

---

## Development & Customization

| Feature | Status | Details |
|---------|--------|---------|
| **UNO API** | ✅ Available | Universal Network Objects — FreedomOffice's component model for programmatic control. |
| **LibreOffice Basic** | ✅ Available | Built-in BASIC-like scripting language with IDE (Tools → Macros → Organize Macros). |
| **Python macros** | ✅ Available | ScriptForge Python library. Full UNO access. |
| **JavaScript macros** | ✅ Available | UNO access via JavaScript. |
| **Java UNO** | ✅ Available | Full UNO API for Java. Extensions, add-ons, and services. |
| **Extension SDK** | ✅ Available | Comprehensive SDK for building extensions in C++, Java, Python, or JavaScript. |
| **Command-line conversion** | ✅ Available | `freedomoffice --headless --convert-to pdf mydoc.docx`. Batch conversion, headless server mode. |
| **Automation tests** | ✅ Available | Python-based UI and functional testing framework. |
| **REST API** | 🚧 In development | FreedomOffice Online REST API (Collabora Online). Document editing via web. |

---

## Comparison Summary

```
                  Microsoft Office              FreedomOffice
                  ─────────────────           ─────────────────
License           Proprietary ($)             MPL-2.0 / LGPL-3.0 (Free)
Platform          Windows, Mac, Web           Linux, Windows, Mac, Web
Format            .docx/.xlsx/.pptx            .odt/.ods/.odp (native)
                                                .docx/.xlsx/.pptx (support)
Cloud             OneDrive/SPO                Nextcloud (self-hosted)
AI                Copilot (subscription)      opencode AI / FOSS models
Collaboration     SharePoint sync             Collabora Online (self-hosted)
Extensions        Office Add-ins (web)        UNO Extensions (native)
Macros            VBA                         LibreOffice Basic + Python + JS
Support           Paid support / forums       Community + paid options
```

---

## Contributing

This feature map is maintained as part of the FreedomOffice project. To suggest corrections or additions:

1. Open an issue at https://github.com/acreetionos/freedomoffice/issues
2. Submit a PR with changes to this file
3. Discuss on Matrix: #freedomoffice:matrix.org

---

*Last updated: June 2026*
*FreedomOffice is a project of Natalie Spiva — AcreetionOS Project*
*Built on the shoulders of LibreOffice and the FOSS community*
