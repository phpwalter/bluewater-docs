<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Environment and File Reference – Bluewater Framework

📄 **File:** `docs/en/technical/references/environment-and-files.md`
📅 **Status:** Active
🏷️ **Tags:** technical, references, environment, files
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Runtime variables, configuration sources, and generated files
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Runtime identity and filesystem paths are explicit deployment inputs.*

---

## 📌 Purpose

This reference lists the environment variables and files that participate in application construction.

## Environment variables

| Variable | Meaning |
|---|---|
| `BLUEWATER_APP` | Required application directory identifier supplied by the front controller or process. |
| `BLUEWATER_APP_BASE` | Optional parent directory containing applications. |
| `BLUEWATER_ENV` | Optional runtime environment overriding configured `BW_ENV`. |

## Framework configuration

Framework defaults live under `config/` in guarded `BW.*.ini.php`, `Bluewater.ini.php`, and session files. Application overrides live under `<app>/config/` with corresponding `App.*` names.

## Generated application files

| File | Ownership |
|---|---|
| `<app>/cache/config.php` | Atomically compiled resolved configuration; applications must not edit it. |
| `<app>/cache/routes.php` | Atomically compiled route table and middleware chain; applications must not edit it. |
| `<app>/logs/application.log` | Default file logger output when logging is enabled. |

## 📚 Related Documents

- [Application configuration](../setup/configuration.md)
- [Host layout](../setup/host-layout.md)
- [Technical references](index.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
