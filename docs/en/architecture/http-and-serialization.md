<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# HTTP and Serialization – Bluewater Framework

📄 **File:** `docs/en/architecture/http-and-serialization.md`  
📅 **Status:** Published  
🏷️ **Tags:** architecture, http, serialization, content-negotiation  
🔖 **Version:** 8.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Internal request and response values, representation selection, and PSR bridges  
🤝 **Contributors:** Framework architects and maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Transport values remain immutable while representation choices remain explicit.*

---

## 📌 Purpose

This document defines Bluewater’s HTTP value objects and response serialization behavior.

## Request and response values

`Request` is an immutable snapshot containing method, path, headers, query values, parsed or raw body, server values, and framework attributes. Header lookup is case-insensitive. `withAttributes()` returns a new request.

`Response` is an immutable status, header map, and encoded body. Factories create JSON, plain text, 204, and RFC 7807-compatible problem responses. The FPM adapter owns emission.

## Content negotiation

An endpoint may return a `Response` or a value to serialize. A response passes through unchanged. Otherwise, custom exact media-type serializers are checked first, followed by JSON or wildcard, XML, CSV, and text. JSON is the final fallback.

Objects normalize through their public properties. Applications must ensure those properties contain no secrets. XML and CSV accept only scalar-compatible leaf values. Unsupported values raise exceptions and reach the application error boundary.

The current `Accept` parser retains client order and strips parameters but does not rank media ranges by quality values.

## 📚 Related Documents

- [System overview](system-overview.md)
- [Security](security.md)
- [OpenAPI](openapi.md)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
