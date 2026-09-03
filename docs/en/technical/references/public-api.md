<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Public API Reference – Bluewater Framework

📄 **File:** `docs/en/technical/references/public-api.md`
📅 **Status:** Active
🏷️ **Tags:** technical, references, api
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Supported namespaces and principal extension contracts
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Applications depend on documented public contracts, not implementation details.*

---

## 📌 Purpose

This reference identifies the current public subsystem surface of Bluewater v8.

## Public subsystems

| Namespace | Principal types |
|---|---|
| `Bluewater` | `Host`, `Application`, `ApplicationBootstrap`, `ApplicationDefinition` |
| `Bluewater\Auth` | Authentication providers, middleware, manager, and `Identity` |
| `Bluewater\Config` | `Config`, `ConfigFactory`, and `IniConfigParser` |
| `Bluewater\Container` | PSR-11 `Container` and resolution exceptions |
| `Bluewater\Database` | `Database` and `PdoDatabase` |
| `Bluewater\Endpoint` | `Endpoint` and `EndpointDispatcher` |
| `Bluewater\Extension` | `Extension` and `ExtensionManager` |
| `Bluewater\Http` | Immutable `Request`, `Response`, and `PsrBridge` |
| `Bluewater\Middleware` | `Middleware`, `Pipeline`, adapters, attributes, and logging |
| `Bluewater\OpenApi` | `OpenApiGenerator` and `Summary` |
| `Bluewater\Routing` | `Router`, `Route`, `Path`, and `RouteNotFound` |
| `Bluewater\Runtime` | `RuntimeAdapter` and `FpmAdapter` |
| `Bluewater\Serialization` | `SerializerRegistry` |
| `Bluewater\Validation` | Validator, attributes, and `ValidationException` |

Future types under `Bluewater\Internal\...` are not part of the semantic-versioning compatibility contract.

## 📚 Related Documents

- [Core architecture](../development/architecture.md)
- [Usage](../usage/index.md)
- [Technical references](index.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
