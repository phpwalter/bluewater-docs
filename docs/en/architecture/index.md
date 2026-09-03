<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../i18n/es/architecture/index.md) | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
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

## Architecture sections

| Section | Responsibility |
|---|---|
| [API](api/index.md) | Describe the OpenAPI contract exposed by implemented routes and schemas. |
| [Core](core/index.md) | Select, construct, boot, and extend an isolated application. |
| [Configuration](configuration/index.md) | Merge guarded defaults with type-compatible application overrides. |
| [Data](data/index.md) | Provide prepared PDO operations and transaction handling without an ORM. |
| [HTTP](http/index.md) | Route requests, compose middleware, validate input, dispatch handlers, and serialize responses. |
| [Runtime](runtime/index.md) | Define application isolation, deployment topology, and performance controls. |
| [Security](security/index.md) | Enforce trust boundaries, authentication, and fail-closed behavior. |
| [Testing](testing/index.md) | Verify framework behavior and application integration. |
| [Governance](governance/index.md) | Maintain shared terminology and architecture decision records. |

## Deliberate exclusions

Bluewater does not implement a service mesh, API gateway appliance, message broker, Kubernetes control plane, centralized identity server, ORM, migration engine, or distributed tracing platform. Those capabilities belong to applications or external infrastructure.

## 📚 Related Documents

- [System overview](core/index.md)
- [Application lifecycle](core/application-lifecycle.md)
- [Technical guides](../technical/index.md)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
