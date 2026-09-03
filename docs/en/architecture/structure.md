# 🧱 Project Structure – Bluewater Framework

📄 **File:** `docs/architecture/structure.md`  
📅 **Status:** Published  
🏷️ **Tags:** structure, folders, layout, psr  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – External developers and integrators  
👨‍💻 **Author:** Bluewater Team

---


## 📌 Purpose

This document describes the **directory layout** and **responsibilities** of all files and folders in a Bluewater-based project.

Understanding this structure ensures:

- Clear separation between framework and application code  
- Easy multi-tenant development  
- Predictable config, cache, and boot behavior  

---

## 🧱 Top-Level Structure

```txt
bluewater-project/
├── app/               # Application logic (multi-tenant supported)
├── bin/               # Project CLI (symlink to vendor)
├── cache/             # Writable runtime cache
├── public/            # Web server entry point
├── vendor/            # Composer-managed packages (includes Bluewater)
├── .env               # Environment-specific overrides
├── composer.json      # Autoload, dependencies, CLI entry
├── README.md          # Project overview
└── docs/              # Architecture, spec, roadmap, etc.
````

---

## 📁 Application Directory

```txt
/app/
├── common/                  # Shared helpers (not tenant-specific)
├── clientA/
│   ├── Controllers/
│   ├── Middleware/
│   ├── config/
│   └── helpers/
└── clientB/
    └── ...
```

Each client is fully isolated. This avoids:

* Route conflicts
* Config bleed
* Authentication confusion

Each client can have:

* Its own routes
* Its own auth strategy
* Its own OpenAPI spec

---

## 🔐 Config Files

```txt
/app/clientA/config/
  ├── routes.php
  ├── auth.php
  ├── middleware.php
  └── services.php
```

All configs are merged in the following order:

1. `.env` (env overrides)
2. `/app/common/config/` (shared)
3. `/app/clientX/config/` (tenant-specific)

---

## 🧰 CLI Tools

```txt
/bin/bluewater           # Symlink to vendor/bin/bluewater
/vendor/bin/bluewater    # Executable CLI defined by framework
```

All CLI commands (e.g. `route:list`, `config:dump`, `openapi:generate`) are available under `bin/bluewater`.

---

## 🔄 Framework Source

```txt
/vendor/bluewater/framework/
└── src/Bluewater/
    ├── Router/
    ├── Dispatcher/
    ├── Middleware/
    ├── Security/
    ├── Logger/
    └── Responder/
```

This is the **read-only**, PSR-4 autoloaded core of the framework.

🚫 You **should not** modify anything under `vendor/` directly.

---

## 📂 `cache/` Directory

```txt
/cache/
├── routes.compiled.php
├── config.merged.php
└── logs/
```

* Writable by PHP
* Cleared using: `bin/bluewater cache:clear`

---

## 🔎 File Ownership Rules

| Area      | Ownership    | Editable? | Notes                                  |
|-----------|--------------|-----------|----------------------------------------|
| `vendor/` | Composer/pkg | ❌ No      | Never edit directly                    |
| `app/`    | You          | ✅ Yes     | All business logic lives here          |
| `bin/`    | Symlink      | ❌ No      | Use `vendor/bin` for CLI               |
| `docs/`   | You          | ✅ Yes     | Architecture, specs, roadmap           |
| `.env`    | You          | ✅ Yes     | Never commit to Git (use .env.example) |

---

## 🧭 Best Practices

* ✅ Use one directory per client
* ✅ Create a `README.md` inside each client folder to describe its config
* ✅ Share utilities via `app/common/helpers/`
* ✅ Document custom commands and config loading logic
* ✅ Avoid touching anything in `vendor/` — extend via your `app/` layer

---

## 🔗 Related Documents

- [📘 Architecture Overview]../architecture/system-overview.md
- [🗺️ Roadmap & Phases](roadmap.md)
- [🧪 Testing & QA](../testing/testing.md)
- [📄 Deployment Guide](../deployment/deployment-guide.md)

---

🧠 *Structure is clarity. Clarity is speed.*

````
