<!-- locale-guard:language-bar:start -->
**<img src="../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../i18n/es/about-bluewater.md) | <img src="../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# About Bluewater – Bluewater Framework

📄 **File:** `docs/en/about-bluewater.md`  
📅 **Status:** Published  
🏷️ **Tags:** overview, goals, boundaries  
🔖 **Version:** 8.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Framework purpose, capabilities, and deliberate exclusions  
🤝 **Contributors:** Framework maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Ordinary API development should be direct; exceptional behavior should remain explicit.*

---

## 📌 Purpose

This document introduces Bluewater Framework 8 and establishes the boundary between implemented framework behavior and application-owned integrations.

## What Bluewater provides

- Convention-based endpoint discovery without a route manifest.
- Per-application configuration, cache, logs, namespace, and endpoint isolation.
- A PSR-11 container with explicit bindings, instances, factories, and autowiring.
- Global, directory, class, and method middleware scopes.
- API-key, HS256 JWT, and application-introspected OAuth bearer authentication.
- DTO hydration and attribute-driven validation.
- JSON, XML, CSV, and text serialization with content negotiation.
- A small PDO database contract without an embedded ORM.
- OpenAPI 3.1 generation from discovered routes and reflected types.
- Runtime adapters, with PHP-FPM supplied as the initial adapter.

## What applications own

Business rules, persistent schemas, migrations, authorization policy, external identity integration, queues, caching platforms, observability backends, and infrastructure remain application responsibilities. Bluewater exposes explicit integration points rather than silently selecting those technologies.

## Compatibility target

Bluewater requires PHP 8.3 or newer. Continuous integration is configured for PHP 8.3 and PHP 8.4. Public `Bluewater\\...` APIs form the intended compatibility surface; future `Bluewater\\Internal\\...` APIs are excluded from that promise.

## 📚 Related Documents

- [System overview](architecture/core/index.md)
- [Architecture index](architecture/index.md)
- [Application developer guide](technical/usage/index.md)

---

This documentation is licensed under the [MIT License](../../LICENSE).

---

*Last updated: 2026-09-03*
