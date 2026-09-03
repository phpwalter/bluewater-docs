<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../../i18n/es/technical/development/routing.md) | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Routing Development – Bluewater Framework

📄 **File:** `docs/en/technical/development/routing.md`
📅 **Status:** Active
🏷️ **Tags:** technical, development, routing
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Changing discovery, conflict detection, caching, and matching
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Routing changes remain deterministic and conflict-intolerant.*

---

## 📌 Purpose

This guide defines the required invariants and tests for changes to route discovery and matching.

## Routing development

Routing is a primary Bluewater differentiator and should be treated as high-risk framework code.

The developer-facing promise is:

```text
create endpoint file
        ↓
no route manifest
        ↓
route becomes available automatically
```

The runtime implementation may compile and cache routing metadata internally, but application developers never maintain that cache or manifest.

Route changes should test at minimum:

- static routes;
- dynamic routes;
- static-route precedence;
- route-shape conflicts;
- handler-name conventions;
- `#[Path]` overrides;
- route parameter/signature validation;
- endpoint file additions;
- endpoint file modifications;
- endpoint file deletions;
- cache invalidation;
- directory middleware inheritance;
- class middleware;
- method middleware.

Normal convention examples:

```php
public function get(): array
```

maps to:

```text
GET /users
```

for `Endpoints/users.php`.

```php
public function getById(int $id): array
```

maps to:

```text
GET /users/{id}
```

Exceptional routes should use `#[Path]` rather than expanding the naming convention indefinitely.

## 📚 Related Documents

- [Using routes](../usage/routing.md)
- [Core architecture](architecture.md)
- [Framework testing](../testing/framework.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
