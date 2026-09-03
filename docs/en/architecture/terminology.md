<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Terminology – Bluewater Framework

📄 **File:** `docs/en/architecture/terminology.md`  
📅 **Status:** Published  
🏷️ **Tags:** architecture, glossary, terminology  
🔖 **Version:** 8.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Canonical terms used throughout Bluewater documentation  
🤝 **Contributors:** Framework architects and maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Shared vocabulary prevents architectural boundaries from becoming ambiguous.*

---

## 📌 Purpose

This glossary defines terms whose precise meaning matters when maintaining or integrating Bluewater v8.

## Terms

| Term | Meaning |
|---|---|
| Application | One isolated Bluewater API with its own root, namespace, configuration, endpoints, cache, logs, and container. |
| Host | Factory that locates, validates, constructs, and boots named applications. |
| Endpoint | Application class discovered from an endpoint file and containing HTTP handler methods. |
| Route | Immutable compiled mapping of HTTP method and path to one endpoint method and middleware chain. |
| Handler | A public endpoint method whose name or attributes define an HTTP operation. |
| Directory middleware | Middleware inherited from `_middleware.php` files along an endpoint directory path. |
| DTO | Application data-transfer object hydrated from an array request body. |
| Extension | Explicit two-phase application integration implementing register and boot callbacks. |
| Runtime adapter | Boundary that creates Bluewater requests and emits Bluewater responses. |
| Identity | Immutable authenticated subject, claims, and normalized unique scopes. |
| Problem response | RFC 7807-compatible JSON response used for framework error boundaries. |
| Compiled cache | Application-local PHP representation of validated routes or configuration. |

## 📚 Related Documents

- [Architecture index](index.md)
- [System overview](system-overview.md)
- [Application developer guide](../technical/application-developers.md)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
