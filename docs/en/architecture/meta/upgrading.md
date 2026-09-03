### 📄 `docs/meta/upgrading.md`

# 🧱 Upgrading – Bluewater Framework

📄 **File:** `docs/meta/upgrading.md`  
📅 **Status:** Stub  
🏷️ **Tags:** upgrading, migration, versions  
🔖 **Version:** 1.0  
📦 **Scope:** 🛠️ Developer-Facing – Maintainers & Contributors  
👨‍🔧 **Maintainer:** Bluewater Core Team

---

## 📘 OVERVIEW

This document provides upgrade instructions between Bluewater versions, including semantic versioning guidance, changelog links, and backward-compatibility notes.

---

## 🔢 Versioning Strategy

Bluewater follows **[Semantic Versioning](https://semver.org)**:

- **MAJOR** – Incompatible API changes
- **MINOR** – Backward-compatible features
- **PATCH** – Bug fixes only

---

## 🔁 Upgrade Process

| Step | Task                                        | Notes                                |
|------|---------------------------------------------|--------------------------------------|
| 1    | Backup your project & config                | Always before a major upgrade        |
| 2    | Review [`CHANGELOG.md`](../../CHANGELOG.md) | Check for breaking changes           |
| 3    | Update `composer.json` version              | Use `^1.1` or specific semver target |
| 4    | Run `composer update`                       | Use `--with-dependencies` if needed  |
| 5    | Run CLI tests                               | `bin/bluewater route:list` etc.      |
| 6    | Rebuild cache                               | `bin/bluewater cache:clear`          |

---

## 🔐 Auth Upgrades

Auth module changes may require config changes per tenant. Check:
- `app/clientA/config/auth.php`
- `src/Security/*` for new drivers

---

## 📁 File Structure Changes

New versions may add directories under:
- `/app/common/`
- `/vendor/bluewater/framework/`

You **should not modify** `vendor` code directly — extend via your app.

---

## 🧠 Tips for Smooth Migrations

- Use **Git** to track config and custom overrides
- Keep custom logic in `app/`, not `vendor/`
- Compare sample app from new version (`composer create-project`)

---

## 🔗 Resources

- [`CONTRIBUTING.md`](../../CONTRIBUTING.md)
- [`docs/meta/troubleshooting.md`](troubleshooting.md)
- [`docs/meta/performance.md`](performance.md)

---

📌 Always test in staging before pushing to production.

---
