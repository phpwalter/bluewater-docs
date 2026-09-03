### 🛠️ `docs/cli/cli-tooling.md` — Stub Content

# 🛠️ Bluewater CLI Tooling – Developer Notes

# 🛠️ CLI Tooling – Bluewater Framework

📄 **File:** `docs/cli/cli-tooling.md`  
📅 **Status:** Published  
🏷️ **Tags:** cli, commands, tools, dev  
🔖 **Version:** 1.0  
📦 **Scope:** 📦 Contributors – Developers and maintainers using CLI tools  
👨‍💻 **Author:** Bluewater Team

---

## 🔧 Overview

The Bluewater CLI is a developer-facing tool for runtime operations, diagnostics, and scaffolding. It is installed with the starter project and exposed via:

```bash
bin/bluewater → vendor/bin/bluewater
````

This command points to the script shipped in the framework package:

```txt
/vendor/bluewater/framework/bin/bluewater
```

---

## 🧱 Architecture Goals

* ✅ Minimal dependencies
* ✅ Fast startup time
* ✅ Self-contained, no Symfony Console or external packages
* ✅ Cross-platform (Linux, macOS, Windows)
* ✅ Easy to extend via Composer autoloading

---

## 📜 Core Commands (v1.0)

| Command       | Purpose                                    |
|---------------|--------------------------------------------|
| `route:list`  | List registered routes                     |
| `cache:clear` | Delete runtime route/config cache          |
| `config:dump` | Output merged configuration for inspection |

---

## 🧪 Testing Strategy

* All commands should:

  * Run with `php bin/bluewater` on all platforms
  * Exit cleanly (0 status code)
  * Handle missing files gracefully
* Commands are tested manually and via `phpunit` test cases in `/tests/CLI/`

---

## 🧭 Roadmap

| Phase                             | Status        |
|-----------------------------------|---------------|
| Manual flag parsing               | ✅ Implemented |
| Command registration system       | 🕐 TBD        |
| Command auto-discovery            | 🕐 TBD        |
| Unit testing CLI commands         | 🕐 TBD        |
| Custom command support (userland) | 🕐 TBD        |

---

## 📎 Notes

* Users may write custom commands in `/app/cli/`
* Future versions may support `bluewater make:controller` and similar utilities
* Avoid heavy CLI frameworks unless needed — startup time is critical

---

## 📂 File Locations

```txt
project/
├── bin/
│   └── bluewater → ../vendor/bin/bluewater
├── vendor/bluewater/framework/bin/bluewater
├── tests/CLI/
│   └── RouteListTest.php
```

---

## 🔚 Summary

The CLI in Bluewater is intentionally simple, scriptable, and fast. Over time, it will support more developer automation, but without bloating the framework.

> Track all changes to the CLI tool here as new commands and capabilities evolve.

```
