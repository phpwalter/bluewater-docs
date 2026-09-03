### 📘 `docs/docs-guides.md` — Stub Content

# 🚀 Getting Started – Bluewater Guides

📄 **File:** `docs/guides/getting-started.md`  
📅 **Status:** Published  
🏷️ **Tags:** setup, installation, cli, first steps  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – New developers and adopters  
👨‍💻 **Author:** Bluewater Team

---

## 📌 Purpose

This document outlines the structure, standards, and plan for user-facing and developer-facing documentation across the Bluewater project.

Goals:

- ✅ Onboard developers quickly
- 📚 Explain framework internals clearly
- 🔍 Enable issue discovery, debugging, and extension

---

## 📂 Documentation Structure

### 🧪 End-User Docs

| File             | Purpose                                |
|------------------|----------------------------------------|
| `README.md`      | Project overview + usage guide         |
| `CLI.md`         | CLI tool usage                         |
| `docs/structure.md` | Directory layout reference          |
| `docs/security.md` | Auth mechanisms and config           |
| `docs/installation.md` | Setup steps, Composer usage     |

---

### 🧑‍💻 Internal/Contributor Docs

| File                        | Purpose                             |
|-----------------------------|-------------------------------------|
| `docs/architecture.md`      | System design, goals, components    |
| `docs/specifications.md`    | Technical behavior and constraints  |
| `docs/core-modules.md`      | Module responsibilities/interfaces  |
| `docs/cli-tooling.md`       | CLI internals and expansion plan    |
| `docs/auth-modules.md`      | JWT/OAuth/mTLS architecture         |

---

## 🧱 Docs Standards

- All markdown files should follow:
  - ✅ **Consistent headings** (`#`, `##`, `###`)
  - ✅ **Table of contents** (if over 100 lines)
  - ✅ **Link other docs** where helpful
- All examples should be:
  - ✅ **Copy-pastable**
  - 💬 **Commented**
  - 📦 Minimal but complete

---

## 🔧 Build Targets

> Future automation goals:

- [ ] Docs hosted on GitHub Pages
- [ ] Auto-generated OpenAPI + CLI docs
- [ ] Theme using Docusaurus or MkDocs

---

## 🧭 Next Steps

- [ ] Write `docs/installation.md` (includes CLI + app layout)
- [ ] Auto-link documentation into `README.md`
- [ ] Write "Extending Bluewater" guide

---

🧠 *Good frameworks work fast. Great ones are also documented.*  
— Bluewater Principle
```
