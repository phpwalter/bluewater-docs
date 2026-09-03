### 📄 `docs/meta/troubleshooting.md`

# 🧯 Troubleshooting – Bluewater Framework

📄 **File:** `docs/meta/troubleshooting.md`  
📅 **Status:** Stub  
🏷️ **Tags:** troubleshooting, debugging, common issues  
🔖 **Version:** 1.0  
📦 **Scope:** 🧰 Developer-Facing – Internal & External  
👨‍🔧 **Maintainer:** Bluewater Core Team

---

## 📘 OVERVIEW

This document outlines common issues developers may encounter while working with the Bluewater Framework and provides clear resolutions and debugging tips.

---

## 🛠️ General Debugging Tips

- Run `bin/bluewater config:dump` to confirm environment configuration
- Use a [PSR-3](https://www.php-fig.org/psr/psr-3/) logger for runtime error tracking
- Enable verbose error output in development (`.env -> DEBUG=true`)
- Log request/response data with middleware during integration testing

---

## 🚨 Common Issues & Fixes

| Issue                          | Probable Cause                    | Resolution                             |
|--------------------------------|-----------------------------------|----------------------------------------|
| Framework not booting          | Missing `.env` or misconfigured   | Check `.env`, fallback defaults        |
| 404s on valid routes           | Route not cached or misregistered | Run `bin/bluewater cache:routes`       |
| CORS errors                    | Missing headers middleware        | Add `CORS` middleware globally         |
| Environment config not loading | Improper `.env` scope             | Check dotenv library path, permissions |
| Composer autoloading fails     | Cache outdated                    | Run `composer dump-autoload`           |

---

## 🧪 Testing Misbehavior

- Use `bin/bluewater route:list` to confirm active routes
- Review `/cache/` contents for corrupted entries
- Clear stale runtime state with `bin/bluewater cache:clear`

---

## 🔗 Related Docs

- [`docs/meta/performance.md`](performance.md)
- [`docs/deployment/environments.md`](../deployment/environments.md)
- [`docs/testing/testing.md`](../testing/testing.md)
- [`docs/integrations/logging.md`](../integrations/logging.md)

---

💬 Need more help? [Open a GitHub issue](https://github.com/BluewaterMVC/bluewater-docs/issues)

---
