<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../../i18n/es/technical/setup/index.md) | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Setup – Bluewater Framework

📄 **File:** `docs/en/technical/setup/index.md`
📅 **Status:** Active
🏷️ **Tags:** technical, setup, requirements
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Requirements and installation
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *A valid runtime and explicit host boundary come before application code.*

---

## 📌 Purpose

This guide defines the supported runtime and installs Bluewater into a host project.

## Requirements

- PHP 8.3 or newer
- Composer 2
- A supported web/runtime environment such as PHP-FPM behind Apache or Nginx

## Installing Bluewater in a host project

In the host project:

```bash
composer require bluewater/framework
```

For local framework development, a Composer path repository may be used instead.

The host's Composer installation owns Bluewater and shared third-party packages. Application-specific PHP classes do not need to be added to the host `composer.json` autoload section because Bluewater dynamically registers the active application's namespace at runtime.

## 📚 Related Documents

- [Host layout](host-layout.md)
- [Configuration](configuration.md)
- [Technical index](../index.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
