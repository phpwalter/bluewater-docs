<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Routing and Dispatch – Bluewater Framework

📄 **File:** `docs/en/architecture/routing-and-dispatch.md`  
📅 **Status:** Published  
🏷️ **Tags:** architecture, routing, endpoints, dispatch  
🔖 **Version:** 8.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Endpoint discovery, route compilation, matching, and argument binding  
🤝 **Contributors:** Framework architects and maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Common routes are conventions; exceptional routes are declarations.*

---

## 📌 Purpose

This document defines how endpoint files become routes and how matched routes invoke application code.

## Route discovery

Endpoint PHP files are traversed in lexical order. Public non-static methods declared by the endpoint class are considered handlers when their names begin with a supported HTTP verb. A file named `Endpoints/users.php` with `get()` and `getById(int $id)` produces `GET /users` and `GET /users/{id}`.

`#[Path]` appends an explicit path when the naming convention is insufficient. Placeholder names must match handler parameters. Canonically equivalent paths such as `/users/{id}` and `/users/{name}` conflict for the same verb and fail discovery.

## Deterministic precedence and caching

Static routes sort before dynamic routes; longer paths sort before shorter paths when their dynamic count is equal. Endpoint and inherited `_middleware.php` files contribute to the route-cache fingerprint. A matching cache is loaded directly; stale routes are rebuilt and written atomically.

## Parameter binding

The dispatcher resolves handler parameters in this order:

1. Bluewater `Request` injection.
2. Captured route parameters.
3. Query-string values.
4. Application DTO hydration from an array request body.
5. Container services.
6. Declared default values.

Supported scalar conversions fail when a value cannot be represented as the declared integer, float, boolean, or string type. DTO validation failures return HTTP 422. Other binding or handler failures reach the application error boundary.

## 📚 Related Documents

- [Middleware](middleware.md)
- [Dependency injection](dependency-injection.md)
- [Validation](validation.md)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
