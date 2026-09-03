<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../../i18n/es/architecture/http/index.md) | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# HTTP – Bluewater Framework

📄 **File:** `docs/en/architecture/http/index.md`
📅 **Status:** Published
🏷️ **Tags:** architecture, http, bluewater-v8
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Request processing and response serialization
🤝 **Contributors:** Framework architects and maintainers
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *HTTP behavior stays explicit from route match through response emission.*

---

## 📌 Purpose

This section describes Bluewater's implemented HTTP pipeline and its validation boundaries.

## Section contents

| Document | Coverage |
|---|---|
| [Routing and dispatch](routing-and-dispatch.md) | Route discovery, matching, argument binding, and handler invocation. |
| [Middleware](middleware.md) | Global and route middleware composition. |
| [Serialization](serialization.md) | PSR-7 requests, response normalization, and JSON serialization. |
| [Validation](validation.md) | Request DTO validation and failure responses. |

## 📚 Related Documents

- [Architecture index](../index.md)

---

This documentation is licensed under the [MIT License](../../../../LICENSE).

---

*Last updated: 2026-09-03*
