### 📘 `docs/api/openapi.md` — OpenAPI Support

# 📡 OpenAPI Support – Bluewater Framework

📄 **File:** `docs/api/openapi.md`  
🧮 **Status:** ✍️ Draft  
🛫 **ETA:** 2025-06-27  
🔖 **Version:** 0.1  
📅 **Date:** {{DATE}}  
🏷️ **Tags:** api, openapi, specification  
🌍 **Scope:** Define how to document and expose tenant-specific APIs using OpenAPI v3.  
👥 **Contributors:** – API designers, client integrators, QA engineers  
👨‍💻 **Author:** Bluewater Team

---

> ### 🪶 **Bluewater Principle**
> *A fast API means nothing if no one knows how to use it.*

---

## 📌 Purpose

This document outlines how Bluewater APIs can be documented using **OpenAPI v3**, enabling:

- ✅ Developer visibility
- 🧪 Mock server/test generation
- 🔄 SDK generation
- ✅ Contract-driven development

---

## 🧭 Overview

Bluewater itself does not auto-generate OpenAPI docs — it encourages **explicit definition** and **tool-driven publishing**.

OpenAPI definitions are stored and served per client (multi-tenant compatible).

---

## 📂 File Location (Recommended)

```txt
/docs/
└── openapi/
    ├── base.yaml                # Shared base schema
    ├── clientA.yaml             # Full spec for Client A
    └── clientB.yaml             # ...
````

Optionally serve via HTTP:

```php
GET /docs/openapi/clientA.yaml
```

---

## 🛠️ Tools for OpenAPI Generation

| Tool                                                 | Usage                        |
|------------------------------------------------------|------------------------------|
| [Swagger UI](https://swagger.io/tools/swagger-ui/)   | Visual explorer in browser   |
| [Redoc](https://github.com/Redocly/redoc)            | Clean, readable API docs     |
| [Stoplight](https://stoplight.io/)                   | GUI + versioned spec editing |
| [OpenAPI Generator](https://openapi-generator.tech/) | Generate SDKs/test clients   |

---

## 🧪 Testing with OpenAPI

* 🧰 Validate schema before deploy
* ✅ Use `mockoon` or `prism` for local API mocking
* 🔁 Enable contract testing between services

---

## 🔐 Security Definition (Per Client)

Each OpenAPI spec can define auth type:

```yaml
components:
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
```

Or specify OAuth2 flow if supported by tenant.

---

## 🔄 Future Capabilities (Planned)

- 📦 `bin/bluewater openapi:validate` CLI validator
- 🛠 Auto-generation hooks for route introspection
- 🧭 Reverse proxy route to render Swagger/Redoc UI (e.g., `/docs/api/`)

---

## 🧭 Next Steps

- [ ] Establish required OpenAPI fields per module
- [ ] Provide validation schema and CLI integration
- [ ] Document Redoc/Swagger hosting patterns for production

---
