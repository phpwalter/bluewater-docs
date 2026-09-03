### 📄 `docs/guides/project-layout.md`

# 🧱 Project Layout – Bluewater Framework

📄 **File:** `docs/guides/project-layout.md`  
📅 **Status:** Stub  
🏷️ **Tags:** structure, layout, folders, conventions  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – Contributors and adopters  
👨‍💻 **Author:** Bluewater Team

---

## 📌 Purpose

This document explains the **directory structure** and **layout conventions** of a Bluewater-based project. It’s designed to help new contributors and teams quickly understand how the framework organizes code and runtime artifacts.

---

## 🗂️ Top-Level Structure

```txt
my-api/
├── app/              # Application-specific logic (controllers, middleware, config)
├── bin/              # CLI tool entry points (e.g. bluewater)
├── cache/            # Writable runtime artifacts (compiled routes, logs, etc.)
├── docs/             # Markdown documentation for contributors and integrators
├── public/           # Web server root (index.php)
├── vendor/           # Composer dependencies (including Bluewater core)
├── composer.json     # Composer metadata
├── .env              # Environment-specific settings
└── README.md         # Project overview
````

---

## 📁 app/

This folder contains tenant-specific and common application code.

```txt
app/
├── common/           # Shared logic (optional)
├── clientA/          # Client-specific modules
│   ├── Controllers/
│   ├── Middleware/
│   ├── config/
│   └── helpers/
└── clientB/
    └── ...
```

Each client is treated as an isolated unit. Bluewater dynamically resolves tenants.

---

## 📁 public/

This is the **web root**, often configured as the document root in NGINX or Apache.

* `index.php`: the single entry point that boots the framework

---

## 📁 bin/

Contains developer CLI tools:

```txt
bin/
└── bluewater         # Executable CLI tool (symlink to vendor/bluewater/framework/bin/)
```

---

## 📁 cache/

A writable directory used at runtime:

* Cached route maps
* Merged configuration
* Precompiled middleware

> 💡 Make sure this directory is writable by your PHP process.

---

## 🔍 PSR-4 Autoloading

Most source files are namespaced according to PSR-4:

* `App\Controllers\` maps to `app/clientX/Controllers/`
* `Bluewater\Router\` maps to `vendor/bluewater/framework/src/Bluewater/Router`

---

## 🧠 Summary

Bluewater’s layout encourages:

* **Isolation**: per-client logic avoids accidental overlap
* **Composability**: separate core from app from tooling
* **Transparency**: no magic — everything lives in predictable places

---

🧠 *A clean layout is the first step to scalable architecture.*
