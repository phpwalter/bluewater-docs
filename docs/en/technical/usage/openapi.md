<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../../i18n/es/technical/usage/openapi.md) | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# OpenAPI – Bluewater Framework

📄 **File:** `docs/en/technical/usage/openapi.md`
📅 **Status:** Active
🏷️ **Tags:** technical, usage, openapi
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Generating OpenAPI 3.1 from routes and reflected types
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Executable routes remain the source for generated API descriptions.*

---

## 📌 Purpose

This guide explains OpenAPI generator registration, output, metadata, and current limitations.

## OpenAPI

Bluewater generates OpenAPI 3.1 metadata from discovered routes and application metadata.

Sources include:

- endpoint paths;
- HTTP methods;
- typed parameters;
- DTO definitions;
- return types;
- optional OpenAPI metadata attributes such as summaries.

The example application exposes generated metadata at:

```text
GET /openapi
```

Do not maintain a separate route manifest solely for OpenAPI.

## 📚 Related Documents

- [Routing](routing.md)
- [Validation](validation.md)
- [Responses](responses.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
