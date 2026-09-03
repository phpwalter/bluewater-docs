<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# OpenAPI Generation – Bluewater Framework

📄 **File:** `docs/en/architecture/openapi.md`  
📅 **Status:** Published  
🏷️ **Tags:** architecture, openapi, reflection, api-contract  
🔖 **Version:** 8.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** OpenAPI 3.1 derivation from discovered routes and reflected PHP types  
🤝 **Contributors:** Framework architects and maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Generated contracts should follow executable routes, not a second route manifest.*

---

## 📌 Purpose

This document describes the OpenAPI information Bluewater derives and the limits of the current generator.

## Generated information

`OpenApiGenerator` reads the router’s already discovered route list. It derives paths, HTTP operations, path and query parameters, DTO request bodies, reflected DTO schemas, summaries supplied by `#[Summary]`, and basic 200 and 422 responses. Generation performs no route discovery, endpoint execution, network I/O, or file writes.

The output declares OpenAPI `3.1.0`. For a fixed route list and reflected source, generation follows deterministic route iteration and property declaration order.

## Current limitations

The generator does not yet model security schemes, arbitrary status codes, headers, examples, polymorphism, PHP union types, detailed problem schemas, external references, or version negotiation. Schema identity uses the DTO short class name; the first class with a duplicate short name wins. These constraints must be addressed before treating the generated document as a complete external contract.

## 📚 Related Documents

- [Routing and dispatch](routing-and-dispatch.md)
- [Validation](validation.md)
- [HTTP and serialization](http-and-serialization.md)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
