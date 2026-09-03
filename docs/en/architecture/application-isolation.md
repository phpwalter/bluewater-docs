<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Application Isolation – Bluewater Framework

📄 **File:** `docs/en/architecture/application-isolation.md`  
📅 **Status:** Published  
🏷️ **Tags:** architecture, multi-application, isolation  
🔖 **Version:** 8.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Filesystem, namespace, configuration, cache, and process boundaries  
🤝 **Contributors:** Framework architects and maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Shared framework code must not imply shared application state.*

---

## 📌 Purpose

This document explains how multiple applications share one Composer installation while retaining independent runtime state.

## Isolation model

Each application owns its directory, PHP namespace, configuration overrides, endpoints, cache, logs, bootstrap class, container, middleware pipeline, router, and extension registry. Applications do not discover one another’s endpoints or reuse one another’s service container.

```text
host/
├── app/app_1/{Bootstrap.php,config,Endpoints,cache,logs}
├── app/app_2/{Bootstrap.php,config,Endpoints,cache,logs}
├── public/app_1/index.php
├── public/app_2/index.php
└── vendor/bluewater/framework
```

## Trust boundary

Application identity is supplied by trusted process or web-server configuration. It must not be selected from untrusted request data. A separate PHP-FPM pool per application is recommended because it also isolates process environment and worker state.

Bluewater validates the application name before joining it to the configured application root. Validating the identifier does not replace operating-system permissions; deployments must still restrict file ownership and writable directories.

## 📚 Related Documents

- [Configuration](configuration.md)
- [Runtime and deployment](runtime-and-deployment.md)
- [Security](security.md)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
