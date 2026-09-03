<!-- locale-guard:language-bar:start -->
<!-- locale-guard:language-bar:end -->

# Documentation Operations – Bluewater Framework

📄 **File:** `docs/README.md`  
📅 **Status:** Active  
🏷️ **Tags:** documentation, publication, operations  
🔖 **Version:** 1.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Documentation source ownership, validation, and publication  
🤝 **Contributors:** Documentation maintainers and framework developers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Documentation is publishable only when it describes verified behavior and passes deterministic validation.*

---

## 📌 Purpose

This document defines how the Bluewater documentation site is organized, validated, localized, and published.

## Source layout

- `docs/en/` contains canonical English content.
- `docs/i18n/{locale}/` contains translations with paths matching the English source.
- `docs/_generated/` contains LocaleGuard-owned status and flag assets.
- `docs/en/_templates/` contains authoring templates that are excluded from translation coverage.
- `docs/mkdocs.yml` defines the published site.

## Validation

Run LocaleGuard before committing changes:

```bash
python -B tools/locale-guard/locale_guard.py update
python -B tools/locale-guard/locale_guard.py check
```

Build the site with strict link and navigation checks:

```bash
mkdocs build --strict --config-file docs/mkdocs.yml
```

## 📚 Related Documents

- [Documentation home](en/index.md)
- [Localization guide](en/contribute/localization.md)
- [Canonical document template](en/_templates/document.md)

---

This documentation is licensed under the [MIT License](../LICENSE).

---

*Last updated: 2026-09-03*
