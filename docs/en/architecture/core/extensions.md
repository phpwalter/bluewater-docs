<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../../i18n/es/architecture/core/extensions.md) | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Extension Architecture – Bluewater Framework

📄 **File:** `docs/en/architecture/core/extensions.md`
📅 **Status:** Published
🏷️ **Tags:** architecture, extensions, lifecycle, integration
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Explicit extension registration and lifecycle callbacks
🤝 **Contributors:** Framework architects and maintainers
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Integration behavior is registered deliberately; packages do not boot themselves.*

---

## 📌 Purpose

This document defines how applications add coordinated behavior without modifying framework internals.

## Contract

An extension implements `Extension::register(Application)` and `Extension::boot(Application)`. Applications add an extension instance or class name to `ExtensionManager` before boot completes.

During application boot, every extension is registered in insertion order after the application’s `register()` hook. Routes are then discovered, extensions boot in the same order, and the application’s `boot()` hook runs last.

Class-name extensions resolve through the application container. The manager verifies the resolved object implements `Extension`; invalid registrations fail. There is no Composer auto-discovery, implicit package scanning, or hidden boot order.

Extensions coordinate service bindings and initialization. Per-request behavior belongs in middleware, and business behavior belongs in application services.

## 📚 Related Documents

- [Application lifecycle](application-lifecycle.md)
- [Dependency injection](dependency-injection.md)
- [Middleware](../http/middleware.md)

---

This documentation is licensed under the [MIT License](../../../../LICENSE).

---

*Last updated: 2026-09-03*
