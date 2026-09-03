<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Application Extensions – Bluewater Framework

📄 **File:** `docs/en/technical/usage/extensions.md`
📅 **Status:** Active
🏷️ **Tags:** technical, usage, extensions
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Explicit registration and two-phase extension lifecycle
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Packages integrate through declared lifecycle hooks rather than hidden discovery.*

---

## 📌 Purpose

This guide explains how coordinated application integrations register services and boot behavior.

## Extensions

Reusable application capabilities may be packaged as Composer packages and registered explicitly.

A Bluewater extension implements:

```text
Bluewater\Extension\Extension
```

Extensions can register facilities such as:

- services;
- middleware;
- serializers;
- validators;
- authentication providers;
- OpenAPI components;
- database drivers.

Extension registration is explicit. Bluewater does not use hidden Composer package auto-discovery.

Normal reusable extensions should not silently add application endpoints.

## 📚 Related Documents

- [Usage](index.md)
- [Middleware](middleware.md)
- [Core architecture](../development/architecture.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
