<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Security Architecture – Bluewater Framework

📄 **File:** `docs/en/architecture/security/index.md`
📅 **Status:** Published
🏷️ **Tags:** architecture, security, trust-boundaries, fail-closed
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Implemented security controls, caller responsibilities, and known limits
🤝 **Contributors:** Framework architects and maintainers
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Unknown credentials, routes, configuration, and application identities fail closed.*

---

## 📌 Purpose

This document records security behavior verified in Bluewater v8 and avoids claiming protections the framework does not implement.

## Implemented controls

- Application identifiers are restricted before filesystem paths are composed.
- Route conflicts and invalid placeholder contracts fail discovery.
- Configuration rejects locked-key changes, type changes, ambiguous references, and cycles.
- API-key comparisons use `hash_equals()` and do not expose keys in identities.
- JWT verification accepts only configured HS256, validates signature and temporal claims, and optionally enforces exact issuer and audience.
- OAuth bearer authentication requires an application introspector to report literal active status and an identity.
- Production problem responses omit exception messages.
- PDO connections default to native prepared statements and exception error mode.

## Application obligations

Applications must implement authorization, secret storage and rotation, CSRF protection where cookies are used, CORS policy, request-size limits, rate limiting, audit persistence, tenant enforcement, output-data classification, database least privilege, and infrastructure security. Authentication alone never grants domain permission.

## Known limits

The built-in JWT provider uses a shared secret and does not retrieve JWKS or manage rotation. Request JSON parsing currently maps malformed JSON to `null`. Object serialization exposes public properties. Development responses may include exception details and must never be enabled in production.

## 📚 Related Documents

- [Authentication](authentication.md)
- [Configuration](../configuration/index.md)
- [Data access](../data/index.md)

---

This documentation is licensed under the [MIT License](../../../../LICENSE).

---

*Last updated: 2026-09-03*
