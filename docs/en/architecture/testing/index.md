<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Testing Architecture – Bluewater Framework

📄 **File:** `docs/en/architecture/testing/index.md`
📅 **Status:** Published
🏷️ **Tags:** architecture, testing, phpunit, quality
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Automated verification layers and required quality gates
🤝 **Contributors:** Framework architects and maintainers
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Framework behavior is trusted only when tests exercise its public contract.*

---

## 📌 Purpose

This document describes the current Bluewater v8 test organization and the checks required for framework changes.

## Test layers

Unit and focused subsystem tests cover authentication, configuration, the container, logging, routing, and validation. `tests/Integration/App1Test.php` boots and exercises the reference application to verify that public subsystems work together from an application developer’s perspective.

## Quality command

The framework’s Composer `check` script runs syntax validation, PSR-12 style checks, PHPStan analysis, and PHPUnit. CI executes the suite on PHP 8.3 and PHP 8.4.

```bash
composer install
composer check
```

Changes to an application-facing behavior should update focused tests and the reference application when an end-to-end contract is affected. Documentation examples must remain consistent with the tested public API.

## Environment note

The documentation build validates links and structure independently. PHP verification still requires a PHP 8.3+ environment with Composer and the extensions declared by the framework.

## 📚 Related Documents

- [Core developer guide](../../technical/development/index.md)
- [Routing and dispatch](../http/routing-and-dispatch.md)
- [Security](../security/index.md)

---

This documentation is licensed under the [MIT License](../../../../LICENSE).

---

*Last updated: 2026-09-03*
