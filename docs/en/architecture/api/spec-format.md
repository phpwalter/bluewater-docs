### 📘 `docs/api/spec-format.md` — Stub Content

# 📘 API Spec Format – Bluewater Framework

📄 **File:** `docs/api/spec-format.md`  
📅 **Status:** Stub  
🏷️ **Tags:** api, format, standards  
🔖 **Version:** 1.0  
📦 **Scope:** 📦 Contributors – Technical authors and doc maintainers  
👨‍💻 **Author:** Bluewater Team

---


## 📌 Purpose

This document outlines the structure, format, and conventions used when generating or maintaining API specifications in Bluewater. It ensures consistency across all services and clients consuming the API.

---

## 🔍 Format Overview

Bluewater uses the **OpenAPI v3** specification (formerly Swagger) as the standard format for documenting RESTful APIs.

### File Format

- YAML (`.yaml`) is the preferred format for readability and diffs.
- JSON is supported, typically for tooling compatibility.

---

## 🧱 File Layout

```yaml
openapi: 3.0.3
info:
  title: Example API
  version: 1.0.0
  description: A sample API spec for a Bluewater-based service
paths:
  /ping:
    get:
      summary: Health check
      responses:
        '200':
          description: OK
````

---

## 🧑‍💻 Best Practices

* ✅ Use meaningful `operationId`s for all endpoints
* ✅ Group routes by functional area using `tags`
* ✅ Include request/response examples
* ✅ Use `$ref` for reusable schemas (in `/components`)
* ❌ Avoid inline definitions unless trivial

---

## 🧰 Tools

| Tool                    | Use Case                       |
| ----------------------- | ------------------------------ |
| `swagger-ui`            | Render OpenAPI spec in browser |
| `redoc`                 | Developer-friendly API docs    |
| `openapi-generator-cli` | Generate SDKs, servers         |

---

## 🗃️ File Location

Specs should be stored at:

```
/docs/specs/{client}/{version}/openapi.yaml
```

Or for a mono-repo:

```
/app/{client}/docs/openapi.yaml
```

---

## 🧭 Next Steps

* [ ] Generate starter OpenAPI files using CLI
* [ ] Create GitHub Action to validate specs on push
* [ ] Add links from each API doc to its endpoint spec

---

> 🧠 API specs aren't just for docs — they’re contracts. Keep them versioned, validated, and alive.

```
