<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Architecture – Bluewater Framework

📄 **File:** `docs/en/architecture/index.md`  
📅 **Status:** Published  
🏷️ **Tags:** architecture, index, bluewater-v8  
🔖 **Version:** 8.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Implemented subsystems and their responsibility boundaries  
🤝 **Contributors:** Framework architects and maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *The architecture describes what the framework enforces today.*

---

## 📌 Purpose

This index organizes the implemented Bluewater v8 architecture and replaces the former duplicate, placeholder, and aspirational page trees.

## Architecture inventory

| Area | Responsibility |
|---|---|
| Host and application | Select, validate, construct, and boot an isolated application. |
| Configuration | Merge guarded framework defaults with type-compatible application overrides. |
| Routing | Discover endpoint files, reject conflicts, compile caches, and match requests. |
| Dispatch | Bind request data and services, validate DTOs, invoke handlers, and serialize results. |
| Middleware | Compose global and route-specific request policies in deterministic order. |
| Authentication | Select one named credential provider and produce an immutable identity or denial. |
| Data access | Expose prepared PDO operations and transaction handling without an ORM. |
| Interoperability | Provide PSR-3, PSR-7, PSR-11, and PSR-15 integration boundaries. |

## Deliberate exclusions

Bluewater does not implement a service mesh, API gateway appliance, message broker, Kubernetes control plane, centralized identity server, ORM, migration engine, or distributed tracing platform. Those capabilities belong to applications or external infrastructure.

## 📚 Related Documents

- [System overview](system-overview.md)
- [Application lifecycle](application-lifecycle.md)
- [Technical guides](../technical/index.md)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
