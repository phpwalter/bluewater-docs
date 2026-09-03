### 📘 `docs/release.md` — Stub Content

# 🚀 Release & Versioning – Bluewater Framework

📄 **File:** `docs/architecture/release.md`  
📅 **Status:** Stub  
🏷️ **Tags:** release, lifecycle, tagging  
🔖 **Version:** 1.0  
📦 **Scope:** 📦 Contributors – Project maintainers and release engineers  
👨‍💻 **Author:** Bluewater Team

---


## 📌 Purpose

This document outlines the process for preparing, verifying, and publishing official Bluewater framework releases.

Goals:

- ✅ Ensure stability and traceability
- 🏷️ Enforce consistent versioning
- 🔒 Lock interfaces before release

---

## 🗂️ Release Types

| Type        | Tag Format     | Notes                          |
|-------------|----------------|--------------------------------|
| Stable      | `v1.0.0`       | Production-ready release       |
| Patch       | `v1.0.1`       | Bugfix or internal improvement |
| Minor       | `v1.1.0`       | Backward-compatible features   |
| Major       | `v2.0.0`       | Breaking changes               |
| Pre-Release | `v1.0.0-beta1` | Preview for feedback/testing   |

Based on [SemVer](https://semver.org/)

---

## ✅ Release Checklist

Before tagging any release:

- [ ] All tests passing
- [ ] Manual CLI check (list routes, dump config)
- [ ] OpenAPI specs generated for all tenants
- [ ] `README.md` updated with latest features
- [ ] Docs synced under `/docs/`
- [ ] `composer.json` version/tag updated (if required)
- [ ] Run `composer validate`
- [ ] Run `composer dump-autoload -o`

---

## 🏷️ Tagging a Release (Git)

```bash
git tag v1.0.0 -m "🎉 Initial public release"
git push origin v1.0.0
````

---

## 📦 Publishing to Packagist

1. Ensure `composer.json` has:

   * `"name": "bluewater/framework"`
   * `"version": "1.0.0"` (or omit and use Git tags)
2. Push to GitHub
3. Submit repo to [packagist.org](https://packagist.org/packages/submit)
4. Confirm `vendor/` excludes and autoloads are correct

---

## 🧪 Post-Release Testing

* [ ] Run install in clean directory:

  ```bash
  composer create-project bluewater/bluewater test-api
  ```
* [ ] Validate:

  * `/app/` is generated
  * CLI tools function correctly
  * Routes + config load for one sample tenant

---

## 🔄 Patch Workflow

For hotfixes or internal patches:

```bash
git checkout main
git pull
# Make patch
git commit -am "🐛 Fix: Responder handles null bodies"
git tag v1.0.1
git push --tags
```

---

## 🧭 Next Steps

* [ ] Define GitHub Actions workflow for release validation
* [ ] Add `bin/bluewater release:prepare` tool
* [ ] Auto-generate CHANGELOG from commit history

---

🧠 *Release early. Release often. But always release clean.*

````
