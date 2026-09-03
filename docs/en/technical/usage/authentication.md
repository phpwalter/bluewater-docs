<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../../i18n/es/technical/usage/authentication.md) | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Application Authentication – Bluewater Framework

📄 **File:** `docs/en/technical/usage/authentication.md`
📅 **Status:** Active
🏷️ **Tags:** technical, usage, authentication, security
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** API-key, JWT, and OAuth bearer provider configuration
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Authentication selects one provider and fails closed without granting authorization.*

---

## 📌 Purpose

This guide explains provider registration, protected endpoints, identity access, and security boundaries.

## Authentication

Authentication is middleware-driven. Endpoint business logic should not manually parse JWTs or API keys unless there is a very specific reason.

Bluewater provides initial support for:

- API keys;
- HS256 JWTs;
- OAuth bearer tokens using an application-provided introspector.

Register providers in `Bootstrap::register()` and attach the appropriate middleware globally, by directory, class, or method.

This keeps authentication policy separate from endpoint business logic.

## 📚 Related Documents

- [Middleware](middleware.md)
- [Application configuration](../setup/configuration.md)
- [Application testing](../testing/applications.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
