<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Runtime and Deployment – Bluewater Framework

📄 **File:** `docs/en/architecture/runtime-and-deployment.md`  
📅 **Status:** Published  
🏷️ **Tags:** architecture, runtime, fpm, deployment  
🔖 **Version:** 8.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Runtime adapter boundary and production application selection  
🤝 **Contributors:** Framework architects and maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *The kernel is runtime-neutral; adapters own transport I/O.*

---

## 📌 Purpose

This document defines the implemented PHP-FPM boundary and the deployment responsibilities left to operators.

## Runtime adapter

`RuntimeAdapter` has two operations: create one Bluewater request and emit one Bluewater response. `FpmAdapter` is the initial implementation. It reads PHP globals through `Request::fromGlobals()`, applies the response status and headers, and writes the body.

## Front controller

The front controller loads Composer, obtains the trusted application identifier from `BLUEWATER_APP`, creates a host, and runs the FPM adapter. `BLUEWATER_APP_BASE` may override the parent application directory, while `BLUEWATER_ENV` may override the configured environment.

## Production responsibilities

Operators own TLS termination, web-server routing, FPM pool configuration, process permissions, secrets injection, scaling, health supervision, log collection, backups, and network controls. A separate FPM pool per application is recommended. Bluewater does not provision containers, Kubernetes resources, load balancers, or cloud infrastructure.

## 📚 Related Documents

- [Application isolation](application-isolation.md)
- [Security](security.md)
- [Application developer guide](../technical/application-developers.md)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
