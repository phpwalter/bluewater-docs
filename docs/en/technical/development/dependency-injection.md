<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Dependency Injection Development – Bluewater Framework

📄 **File:** `docs/en/technical/development/dependency-injection.md`
📅 **Status:** Active
🏷️ **Tags:** technical, development, container, psr-11
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Changing service registration, resolution, and autowiring
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Automatic construction never guesses between ambiguous dependencies.*

---

## 📌 Purpose

This guide defines the development contract for Bluewater’s PSR-11 container.

## Dependency injection development

Bluewater uses a hybrid DI model:

- explicitly registered services;
- interface-to-class bindings;
- callable factories;
- constructor autowiring for concrete classes where possible.

Do not introduce hidden service discovery. Replacement implementations must be registered explicitly.

When adding a replaceable framework facility, prefer:

```php
interface Cache
{
    public function get(string $key): mixed;
}
```

with a default implementation:

```php
final class FileCache implements Cache
{
}
```

An application can then replace it explicitly through the container.

## 📚 Related Documents

- [Using dependency injection](../usage/dependency-injection.md)
- [Core architecture](architecture.md)
- [Framework testing](../testing/framework.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
