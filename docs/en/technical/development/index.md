<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../../i18n/es/technical/development/index.md) | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Core Development – Bluewater Framework

📄 **File:** `docs/en/technical/development/index.md`
📅 **Status:** Active
🏷️ **Tags:** technical, development, repository
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Framework development requirements and repository ownership
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Framework work preserves the application-facing contract.*

---

## 📌 Purpose

This guide establishes the environment and repository boundaries for Bluewater core development.

## Development requirements

- PHP 8.3 or newer
- Composer 2
- Git
- PDO SQLite for integration tests
- SimpleXML for XML serialization tests

Clone the repository and install dependencies:

```bash
git clone https://github.com/phpwalter/bluewater-framework.git
cd bluewater-framework
composer install
```

During development, work on a feature branch rather than directly on `main`:

```bash
git switch main
git pull
git switch -c feature/my-change
```

Until the initial Bluewater 8 implementation is merged, use the implementation branch:

```bash
git switch build/bluewater-v8
composer install
```

## Repository layout

```text
bluewater-framework/
├── src/                 # Framework source
├── config/              # Bluewater default configuration
├── tests/               # Unit and integration tests
├── examples/
│   └── host/
│       ├── app/
│       │   └── app_1/   # Reference application
│       └── public/
│           └── app_1/   # Reference front controller
├── composer.json
├── phpunit.xml.dist
└── README.md
```

The main ownership rule is simple:

```text
src/ + config/ + tests/ = Bluewater framework
examples/host/app/app_1 = application-level reference implementation
```

Do not implement framework behavior inside `app_1`. `app_1` exists to prove that the framework behaves correctly from an application developer's point of view.

## 📚 Related Documents

- [Core architecture](architecture.md)
- [Contribution workflow](contributing.md)
- [Testing](../testing/framework.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
