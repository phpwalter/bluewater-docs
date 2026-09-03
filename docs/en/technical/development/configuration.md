<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Configuration Development – Bluewater Framework

📄 **File:** `docs/en/technical/development/configuration.md`
📅 **Status:** Active
🏷️ **Tags:** technical, development, configuration
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Changing default configuration and merge behavior
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Configuration changes preserve type, ownership, and deterministic resolution.*

---

## 📌 Purpose

This guide defines the engineering rules for changing Bluewater configuration behavior.

## Configuration development

Bluewater-owned defaults live under `config/`.

Examples:

```text
config/Bluewater.ini.php
config/BW.db.ini.php
config/BW.logging.ini.php
config/BW.session.php
```

Application overrides belong in the application, not in the framework package:

```text
app/app_1/config/App.ini.php
app/app_1/config/App.db.ini.php
app/app_1/config/App.logging.ini.php
```

Configuration behavior follows these rules:

- Bluewater defaults load first;
- application config overrides permitted values;
- `BW_VER` is locked;
- override types must match Bluewater's defined type;
- unresolved references fail bootstrap;
- circular references fail bootstrap;
- effective config is compiled into the active application's cache directory;
- Bluewater never writes generated data into its own package directory.

Legacy placeholders such as `{APP_ROOT}`, `{CACHE_ROOT}`, `{BLUEWATER}`, `{SITE_ROOT}`, and `{DS}` are supported as compatibility vocabulary without making framework internals depend on global PHP constants.

When adding new framework configuration, define a safe default in the corresponding `BW.*` file and add tests covering both the default and application override behavior.

## 📚 Related Documents

- [Application configuration](../setup/configuration.md)
- [Core architecture](architecture.md)
- [Framework testing](../testing/framework.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
