### ⚙️ `docs/core/config.md` — Stub Content

# ⚙️ Config – Bluewater Core Module

📄 **File:** `docs/core/config.md`  
📅 **Status:** Published  
🏷️ **Tags:** core, config, env, psr-11  
🔖 **Version:** 1.0  
📦 **Scope:** 📦 Contributors – Configuration managers and extension developers  
👨‍💻 **Author:** Bluewater Team

---


The Config module handles loading and merging **environment-based configuration** from `.env` files, client-specific config files, and framework defaults.

---

## 🧩 Responsibilities

- Load environment variables from `.env`
- Merge config arrays from `/app/[client]/config/`
- Make config available via DI or global utility
- Allow per-client and per-environment overrides

---

## 🗂️ Configuration Layers

1. **`.env`** — Global environment overrides  
2. **`app/common/config/*.php`** — Shared default configs  
3. **`app/clientX/config/*.php`** — Client-specific overrides

---

## 📁 Files

```txt
src/
└── Bluewater/
    └── Core/
        └── Config/
            ├── ConfigLoader.php
            └── DotenvParser.php
````

---

## 🧪 Testing

* Check merging behavior across layers
* Validate `.env` parsing edge cases
* Test missing keys and fallback logic

See [testing.md](../testing/testing.md)

---

## 🧬 Sample Usage

```php
$config = Config::get('auth.jwt.secret');
// → resolves through all layers with fallback
```

---

## 🔗 Related

* [Architecture Spec](../architecture/architecture.md)
* [Deployment Guide](../deployment/deployment-guide.md)
* [Router](router.md)

---

📎 Tags: `core`, `config`, `env`, `override`, `multiclient`

```
