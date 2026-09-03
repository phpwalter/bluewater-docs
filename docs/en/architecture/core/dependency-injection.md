<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Dependency Injection – Bluewater Framework

📄 **File:** `docs/en/architecture/core/dependency-injection.md`
📅 **Status:** Published
🏷️ **Tags:** architecture, container, psr-11, services
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Service registration, resolution, autowiring, and failure behavior
🤝 **Contributors:** Framework architects and maintainers
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Dependencies are explicit even when their construction is automatic.*

---

## 📌 Purpose

This document describes the PSR-11 container used by each Bluewater application.

## Registration forms

The container accepts retained object instances, interface-to-class bindings, callable factories, and autowiring of concrete classes. Duplicate registration replaces the previous definition only where the registration API explicitly permits it.

## Resolution

Constructor parameters with registered or concrete class types are resolved recursively. Defaults may satisfy unresolved optional parameters. Interfaces require explicit bindings. Circular construction, unresolvable scalar parameters, missing classes, and invalid factory results fail with container exceptions.

The container is application-scoped. Framework services such as configuration, router, middleware pipeline, dispatcher, and extension manager are installed during application construction. Application services are normally registered in `Bootstrap::register()`.

## Boundary

Autowiring constructs dependencies; it does not perform domain validation, choose between ambiguous implementations, or discover third-party packages automatically.

## 📚 Related Documents

- [Application lifecycle](application-lifecycle.md)
- [Extensions](extensions.md)
- [Core developer guide](../../technical/development/index.md)

---

This documentation is licensed under the [MIT License](../../../../LICENSE).

---

*Last updated: 2026-09-03*
