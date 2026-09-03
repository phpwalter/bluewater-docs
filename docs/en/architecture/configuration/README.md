### 📘 `docs/configuration/README.md` — Configuration Overview

# ⚙️ Configuration System – Bluewater Framework

📄 **File:** `docs/configuration/README.md`  
🧮 **Status:** ✍️ Draft  
🛫 **ETA:** 2025-06-28  
🔖 **Version:** 0.1  
📅 **Date:** 2025-06-07  
🏷️ **Tags:** configuration, runtime, environment, tenants  
🌍 **Scope:** Describes the system-wide configuration strategy, layering model, runtime resolution, and per-tenant configuration handling in Bluewater.  
👥 **Contributors:** Architects, Core Developers, DevOps  
👨‍💻 **Author:** Walter Torres

---

## 📘 Overview

This document outlines Bluewater’s **configuration architecture**, focusing on clarity, runtime safety, and per-tenant adaptability. Configuration is central to modularity and is handled in a deterministic, cache-first model.

---

> ### 🪶 **Bluewater Principle**  
> *Environment configuration must be stateless, cacheable, and audit-friendly. No environment should ever run from raw INI or YAML at runtime.*

---

## 📂 Configuration Loading Lifecycle

1. **Build-time preparation** merges raw files (`*.ini.php`) per environment.
2. **Cache is compiled** into `config.cache.php`.
3. **Runtime loads only** the cache—fast, deterministic, and secure.

If cache is missing:
- `.ini.php` files are parsed
- Merged into memory
- Cache is re-generated

> ⚠️ Parsing of `.ini.php` files occurs only when the compiled cache is missing. Production must never depend on live parsing.

---

## 🗂️ File Format and Structure

- ✅ **Supported**: PHP files returning arrays (i.e., `return [...]`)
- ❌ **Unsupported**: YAML, JSON, XML — even with parsers installed

```php
// config.production.php
return [
  'env' => 'production',
  'db' => [...],
];
````

---

## 🧱 Directory Layout

```text
/config/
├── base/
│   └── app.ini.php
├── tenants/
│   ├── clientA.ini.php
│   └── clientB.ini.php
└── cache/
    └── config.cache.php
```

---

## 🔄 Multi-Tenant Support

Each tenant can have its own config file:

```php
return [
  'tenant' => 'clientA',
  'auth_driver' => 'oauth',
  'features' => ['beta', 'billing'],
];
```

These are merged with base config under namespaced keys.

---

## 🛠 CLI Utilities

Bluewater ships with a CLI tool:

```bash
bin/bluewater config:cache
```

This command:

* Loads all `.ini.php` files
* Validates structure
* Writes a single `config.cache.php` artifact

---

## 🔐 Security Design

* Only `.php` files are executed at runtime
* Configs are read-only in production
* Secrets (tokens, keys) are injected by:

    * Kubernetes secrets
    * Vault runtime mounts
    * `.env` overlays at container startup

---

## 🧩 Extensibility

Custom config loaders can hook into lifecycle events:

* `onBoot()` — modify config before it's cached
* `onReload()` — hot-swap modified config at runtime

---

## 📎 Related

* [`Config Class Specification`](./config-class-spec.md)
* [`Secrets`](secrets.md)
* [`Runtime Behavior`](runtime.md)

---

*Last updated: 2025-06-07*
