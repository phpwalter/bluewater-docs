<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Configuration Architecture – Bluewater Framework

📄 **File:** `docs/en/architecture/configuration.md`  
📅 **Status:** Published  
🏷️ **Tags:** architecture, configuration, cache, validation  
🔖 **Version:** 8.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Framework defaults, application overrides, references, and compiled cache  
🤝 **Contributors:** Framework architects and maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Configuration inheritance is allowed only when types and ownership remain intact.*

---

## 📌 Purpose

This document defines how Bluewater constructs an immutable configuration view for one application.

## Sources and precedence

Framework-owned `*.ini.php` and `*.session.php` files load first in lexical order. Application-owned counterparts load second and recursively override matching values. Missing application files inherit framework defaults.

Application overrides must preserve the existing leaf type. `BW_VER` is locked and cannot be added or changed by an application. Configuration files are guarded PHP files; loading them directly outside Bluewater’s defined bootstrap context is rejected by their guard.

## Reference resolution

Placeholders such as `{APP_ROOT}`, `{CACHE_ROOT}`, `{BLUEWATER}`, `{SITE_ROOT}`, and `{DS}` resolve after merge. Exact flattened keys take precedence. A leaf-name reference is accepted only when it is unique. Unknown, ambiguous, and circular references fail instead of falling back silently.

## Compiled cache

The ordered source list and file state produce a fingerprint. A current cache is loaded as PHP. A stale configuration is fully parsed and validated before an atomic rename replaces `cache/config.php`; validation failure leaves the prior cache untouched.

## 📚 Related Documents

- [Application isolation](application-isolation.md)
- [Security](security.md)
- [Application developer guide](../technical/application-developers.md)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
