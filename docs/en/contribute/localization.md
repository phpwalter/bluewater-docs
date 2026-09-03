<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Localization Contributions – Bluewater Framework

📄 **File:** `docs/en/contribute/localization.md`  
📅 **Status:** Active  
🏷️ **Tags:** contributing, localization, locale-guard  
🔖 **Version:** 1.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Translation layout, supported locales, and deterministic coverage  
🤝 **Contributors:** Translators and documentation maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Translation coverage is derived from files; it is never maintained as a hand-edited percentage.*

---

## 📌 Purpose

This guide explains how English, Spanish, German, and Japanese documentation is governed with LocaleGuard.

## Locale layout

English is canonical under `docs/en`. Translations mirror the path relative to that root:

```text
docs/en/architecture/system-overview.md
docs/i18n/es/architecture/system-overview.md
docs/i18n/de/architecture/system-overview.md
docs/i18n/ja/architecture/system-overview.md
```

LocaleGuard identifies a document by this relative path. It measures existence and governance state; it does not translate or judge translation quality.

## Updating generated content

```bash
python -B tools/locale-guard/locale_guard.py update
python -B tools/locale-guard/locale_guard.py check
python -B tools/locale-guard/locale_guard.py missing es
```

Commit the generated report, copied flag assets, and updated marker regions with the documentation change.

## 📚 Related Documents

- [Documentation contribution guide](documentation.md)
- [LocaleGuard project](https://github.com/phpwalter/locale-guard)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
