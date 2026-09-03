<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../../i18n/es/technical/development/contributing.md) | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Contribution Workflow – Bluewater Framework

📄 **File:** `docs/en/technical/development/contributing.md`
📅 **Status:** Active
🏷️ **Tags:** technical, development, contributing, ci
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Branching, validation, review, and compatibility expectations
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *A change is complete only when implementation, tests, examples, and documentation agree.*

---

## 📌 Purpose

This guide defines the required workflow for contributing to Bluewater core.

## Contribution workflow

Recommended workflow:

```text
main
 ↓
feature/fix branch
 ↓
edit src/
 ↓
edit config/ when defaults change
 ↓
add unit tests
 ↓
update app_1 integration coverage when needed
 ↓
run targeted tests
 ↓
composer check
 ↓
push
 ↓
pull request
 ↓
PHP 8.3 + PHP 8.4 CI
 ↓
review
 ↓
merge
```

Do not merge a framework change merely because it is syntactically valid. Core changes must preserve Bluewater's primary goals: small surface area, predictable behavior, automatic file-based endpoint discovery, high request-path efficiency, explicit extension points, and straightforward debugging.

## 📚 Related Documents

- [Core development](index.md)
- [Framework testing](../testing/framework.md)
- [Technical index](../index.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
