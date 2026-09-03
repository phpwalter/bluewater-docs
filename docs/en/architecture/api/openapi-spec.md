### 📘 `docs/api/openapi-spec.md` — Stub Content

# 📄 OpenAPI Specification – Bluewater Framework

📄 **File:** `docs/api/openapi-spec.md`  
📅 **Status:** Stub  
🏷️ **Tags:** api, specification, openapi  
🔖 **Version:** 1.0  
📦 **Scope:** 📦 Contributors – API maintainers and technical writers  
👨‍💻 **Author:** Bluewater Team

---

This document explains how Bluewater defines, generates, and uses OpenAPI specs for tenant APIs.

---

## 🛠️ Generation

Use the CLI tool:

```bash
bin/bluewater openapi:generate clientA
````

Options:

* `--all` — generate specs for all tenants
* `--output=path` — write output to a specific file

---

## 📁 Output Location

```txt
/docs/openapi/clientA.yaml
```

> Each tenant should maintain its own OpenAPI YAML.

---

## 🔌 Integration Options

* Swagger UI
* Redoc
* Stoplight
* Mock servers
* SDK generation tools (e.g., OpenAPI Generator)

---

## 🔐 Security Annotations

OpenAPI responses can be extended to include JWT or OAuth flow info per tenant.

---

---

## 📊 Specification Components – Status Overview

| Component                     | Status         | Notes                               |
|-------------------------------|----------------|-------------------------------------|
| CLI Command                   | ✅ Complete     | `openapi:generate` command live     |
| Per-Tenant Spec Generation    | ✅ Complete     | Each client has isolated YAML       |
| Output Directory              | ✅ Complete     | `/docs/openapi/` per tenant         |
| OpenAPI Format (v3)           | ✅ Complete     | JSON/YAML output supported          |
| Spec Validation (Lint)        | 🔄 In Progress | To be added in CLI pipeline         |
| UI Integration (Swagger)      | 📝 Planned     | Optional: Redoc, Swagger UI support |
| SDK Generation Support        | 📝 Planned     | Future: openapi-generator, etc.     |
| Auth Flow Schemas (JWT/OAuth) | 📝 Planned     | Based on enabled middleware         |
