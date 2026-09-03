### 📘 `docs/contribute/header-template.md` — Document Header Template Guide

# 🧩 Document Header Template – Bluewater Framework

📄 **File:** `docs/contribute/header-template.md`
🧮 **Status:** 📘 Final
🛫 **ETA:** N/A
🔖 **Version:** 1.0
📅 **Date:** 2025-06-06
🏷️ **Tags:** meta, headers, documentation-style
🌍 **Scope:** Define and enforce a standardized metadata header for all documentation files within the Bluewater Framework project.
👥 **Contributors:** – Technical Writers, Architects, Core Maintainers
👨‍💻 **Author:** Walter Torres

---

## 🧭 Purpose

This document provides the canonical metadata and formatting template for all documentation files under `docs/`. It standardizes headers, versioning, and editorial status to improve consistency, tooling, and navigation.

---

## 📋 Markdown Header Template

```markdown
### 📘 `docs/[section]/<filename>.md` — <Document Title>

# <Emoji> <Document Title> – Bluewater Framework

📄 **File:** `docs/[section]/<filename>.md`  
🧮 **Status:** ⏳ Planned  
🛫 **ETA:** [YYYY-MM-DD (3 weeks from file creation)]  
🔖 **Version:** 0.1  
📅 **Date:** [YYYY-MM-DD (file creation date)]  
🏷️ **Tags:** tag1, tag2, tag3  
🌍 **Scope:** <Define this document’s intent, target audience, and architectural boundaries>  
👥 **Contributors:** – <List the roles responsible for or impacted by this document>  
👨‍💻 **Author:** Walter Torres

<!--
🧮 STATUS OPTIONS (choose only one from below):
  - 🚧 Stub / Placeholder
  - 📝 In Review
  - ⏳ Planned
  - 🔐 Internal Only
  - ✍️ Draft
  - ✅ Approved
  - 📘 Final
  - ⚠️ Deprecated
  - ♻️ Needs Update
  - 🗑️ Obsolete
-->
```

---

## 🖼 Diagram Pathing Convention

Use the following for inserting diagrams consistently:

```markdown
![Descriptive Title](../../assets/diagrams/[section]/<image-name>.png)
```

* `[section]`: Matches the document's directory (e.g., `architecture`, `platform`)
* `<image-name>.png`: Use descriptive kebab-case file names

---

## 🧠 Usage Notes

* Only the **active status line** should be shown; the others are included as internal guidance.
* Dates should always be in `YYYY-MM-DD` format for consistency and automation.
* Placeholders or stub documents must use `🚧 Stub / Placeholder` and `0.0` as their version.

---
