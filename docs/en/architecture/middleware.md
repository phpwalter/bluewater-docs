<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Middleware Architecture – Bluewater Framework

📄 **File:** `docs/en/architecture/middleware.md`  
📅 **Status:** Published  
🏷️ **Tags:** architecture, middleware, psr-15  
🔖 **Version:** 8.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Middleware scopes, ordering, resolution, and interoperability  
🤝 **Contributors:** Framework architects and maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Request policy belongs in an ordered pipeline, not inside endpoint business logic.*

---

## 📌 Purpose

This document defines Bluewater’s synchronous middleware contract and effective execution order.

## Effective scopes

Middleware is composed in the following order:

1. Global application middleware added during bootstrap.
2. Directory middleware inherited from `_middleware.php` files.
3. Repeatable endpoint-class `#[UseMiddleware]` attributes.
4. Repeatable endpoint-method `#[UseMiddleware]` attributes.

The first entry is the outermost middleware and receives the request first. Each middleware must return a Bluewater `Response` or delegate to the supplied next callable.

## Resolution

Middleware instances may be registered directly. Class-string entries resolve through the application container for each handled request. Resolution failures and middleware exceptions are not caught by the pipeline; the application converts them to a 500 problem response.

## PSR-15 boundary

`Psr15Adapter` converts a Bluewater request to PSR-7, invokes a PSR-15 handler, then converts the PSR response back. This provides interoperability without making PSR types the normal application-facing API.

## 📚 Related Documents

- [Routing and dispatch](routing-and-dispatch.md)
- [Dependency injection](dependency-injection.md)
- [Authentication](authentication.md)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
