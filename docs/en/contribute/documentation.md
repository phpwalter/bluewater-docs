<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../i18n/es/contribute/documentation.md) | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Documentation Contributions – Bluewater Framework

📄 **File:** `docs/en/contribute/documentation.md`  
📅 **Status:** Active  
🏷️ **Tags:** contributing, documentation, quality  
🔖 **Version:** 1.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Authoring, review, validation, and synchronization rules  
🤝 **Contributors:** Documentation and framework maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Documentation changes with behavior, not after behavior.*

---

## 📌 Purpose

This guide defines the acceptance criteria for Bluewater documentation contributions.

## Authoring rules

1. Start from [`docs/en/_templates/document.md`](../_templates/document.md).
2. Describe behavior implemented by the referenced source branch.
3. Use repository-relative file paths and valid relative links.
4. State security boundaries and failure behavior precisely.
5. Include executable examples without credentials or realistic secrets.
6. Remove placeholders before marking a document Active or Published.
7. Preserve the LocaleGuard language-bar markers exactly.

## Ownership and synchronization

Technical guidance originates in `bluewater-framework`. Architecture, navigation, localization, and publication are maintained in `bluewater-docs`. A framework behavior change must update its source documentation before the synchronized publication copy.

## Required checks

```bash
python -B tools/locale-guard/locale_guard.py update
python -B tools/locale-guard/locale_guard.py check
mkdocs build --strict --config-file docs/mkdocs.yml
```

## 📚 Related Documents

- [Localization guide](localization.md)
- [Documentation operations](https://github.com/phpwalter/bluewater-docs/blob/main/docs/README.md)
- [Canonical template](../_templates/document.md)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
