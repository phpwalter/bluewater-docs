### 📘 `docs/api/versioning.md` — Stub Content

# 🔢 API Versioning – Bluewater Framework

📄 **File:** `docs/api/versioning.md`  
📅 **Status:** Stub  
🏷️ **Tags:** api, versioning, semver  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – Developers integrating with API  
👨‍💻 **Author:** Bluewater Team

---

## 📌 Purpose

This document defines how **API versioning** is handled in Bluewater projects to ensure backward compatibility, minimize breaking changes, and support multiple client implementations concurrently.

---

## 🔢 Versioning Strategies

Bluewater supports several versioning schemes depending on your use case:

| Method            | Example                      | Notes                            |
|-------------------|------------------------------|----------------------------------|
| URI path          | `/v1/users`                  | Most common and explicit         |
| Header-based      | `X-API-Version: 2`           | Clean URLs, configurable per client |
| Subdomain-based   | `v1.api.example.com`         | Used for large-scale deployments |
| Query param       | `/users?version=1.2`         | Less preferred                   |

---

## 🧭 Recommended Approach

Use **URI-based versioning** by default:

```

GET /v1/users

````

Route groups can be declared as:

```php
$router->group('/v1', function ($r) {
  $r->get('/users', UserController::class . '@index');
});
````

---

## 🔁 Version Lifecycle

| Stage        | Description                     |
| ------------ | ------------------------------- |
| `v1`         | Stable and in use               |
| `v2-beta`    | Preview version under testing   |
| `v0`         | Internal/testing only           |
| `deprecated` | Supported but no longer updated |

---

## 📚 Documentation Rules

Each version should maintain its own OpenAPI spec and documentation:

```
/docs/specs/v1/openapi.yaml
/docs/specs/v2/openapi.yaml
```

---

## 🧠 Notes

* ✅ Each version should be independently testable
* ✅ Breaking changes must trigger a major version bump
* ✅ Deprecated versions should remain for at least one full release cycle

---

## 🧭 Next Steps

* [ ] Add middleware for detecting requested version
* [ ] Auto-inject `X-API-Version` into responses
* [ ] Support default version fallback

---

> 🧠 A versioned API is a promise. Break it carefully, and document it completely.

```
