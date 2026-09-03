# 🧩 Extending Bluewater Framework

📄 **File:** `docs/meta/extending.md`  
📅 **Status:** Stub  
🏷️ **Tags:** extension, architecture, customization  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – Developers & Integrators  
👨‍💻 **Author:** Bluewater Team

---

## 📘 OVERVIEW

This guide explains how to extend or override core components of the Bluewater framework without modifying the source code. All components follow PSR standards and are designed for full customizability through Composer and modular architecture.

---

Confirmed 🧠💻 — here's the updated **Extensible Modules** table for `docs/meta/extending.md`, with:

✅ GitHub Pages–friendly relative links
✅ External PSR spec links for relevant components

---

### 🔧 Extensible Modules

| Component                           | Method                                                                        | Notes                                |
|-------------------------------------|-------------------------------------------------------------------------------|--------------------------------------|
| [Router](../core/router.md)         | Custom [PSR-7](https://www.php-fig.org/psr/psr-7/) route maps                 | Swap via service config              |
| [Logger](../core/logger.md)         | [PSR-3](https://www.php-fig.org/psr/psr-3/) compatible implementation         | Monolog, stderr, or custom stream    |
| [Config](../core/config.md)         | Inject config loaders                                                         | Use `.env`, YAML, or external source |
| [Auth](../modules/auth.md)          | JWT, OAuth, or plugin drivers                                                 | Driver model per tenant              |
| [Middleware](../core/middleware.md) | Add or replace [PSR-15](https://www.php-fig.org/psr/psr-15/) middleware stack | Modular pipeline                     |
| [Responder](../core/responder.md)   | Override response formatters                                                  | JSON, XML, or custom formatter       |

---

## 🧰 Tools & Conventions

- Composer `replace` or `autoload` rules  
- Service registries or interfaces  
- Keep all custom code in `/app/common/` or per-tenant

---

## 🧠 Best Practices

- Avoid modifying code in `vendor/` or `framework/src/`
- Favor PSR compliance and dependency injection
- Use namespaces to avoid collisions

---

> *Extend smart. Swap clean. Bluewater makes it composable.*

---
