<!-- locale-guard:language-bar:start -->
**<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Technical Guides – Bluewater Framework

📄 **File:** `docs/en/technical/index.md`  
📅 **Status:** Published  
🏷️ **Tags:** technical, index, source-ownership  
🔖 **Version:** 8.0.0  
📅 **Date:** 2026-09-03  
🌍 **Scope:** Published application and core developer guidance  
🤝 **Contributors:** Framework and documentation maintainers  
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Technical guidance originates beside the implementation it describes.*

---

## 📌 Purpose

This index publishes technical guides owned by `bluewater-framework/build/bluewater-v8`. Publication copies are synchronized only after the framework source documents are updated.

## Available guides

- The [Application Developer Guide](application-developers.md) covers installation, host layout, endpoints, middleware, authentication, data access, and deployment.
- The [Core Developer Guide](core-developers.md) covers framework boundaries, subsystem development, quality gates, compatibility, and contribution workflow.

## Synchronization

From the documentation repository with a sibling framework checkout:

```bash
python tools/sync-framework-docs.py ../bluewater-framework
```

The synchronization tool adapts repository-relative metadata and license links while preserving framework-owned technical content.

## 📚 Related Documents

- [Architecture index](../architecture/index.md)
- [Documentation contribution guide](../contribute/documentation.md)
- [Bluewater Framework repository](https://github.com/phpwalter/bluewater-framework)

---

This documentation is licensed under the [MIT License](../../../LICENSE).

---

*Last updated: 2026-09-03*
