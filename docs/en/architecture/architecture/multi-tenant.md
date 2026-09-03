### 📘 `docs/architecture/multi-tenant.md` — Multi-Tenant Architecture

# 🧩 Multi-Tenant Architecture – Bluewater Framework

📄 **File:** `docs/architecture/multi-tenant.md`  
📅 **Status:** Draft  
🏷️ **Tags:** tenants, isolation, architecture  
🔖 **Version:** 0.1  
🌍 **Scope:** Describe the multi-tenant capabilities of the Bluewater Framework, including resolution strategies, data isolation patterns, configuration models, file structure, and operational flow  
🤝 **Contributors:** – Developers and DevOps engineers implementing or supporting multi-tenant platform functionality  
👨‍💻 **Author:** Walter Torres  

---

## 📌 Purpose

This document defines how multi-tenancy is implemented within the Bluewater Framework. It explains how tenant identity is resolved, how data is isolated, and what optional configurations exist for supporting single- or multi-tenant deployments.

---

## 🏷️ What is Multi-Tenancy?

**Multi-tenancy** allows a single instance of an application to serve multiple customers (tenants), each with logically or physically isolated data and configurations.

Bluewater supports a **flexible multi-tenant model** that can be toggled on or off depending on the deployment use case.

---

## 🧭 Tenant Resolution Strategies

Tenants can be resolved using the following methods:

### 1. **Subdomain-Based Routing**
- Requests are routed based on the subdomain:
```

tenant1.api.domain.com → tenant1 context

```
- Requires DNS and reverse proxy configuration

### 2. **Header-Based Resolution**
- The API Gateway extracts a header:
```

X-Tenant-ID: tenant1

````
- More suitable for internal APIs or proxy-based routing

### 🔄 Resolution Pipeline

1. API Gateway intercepts request  
2. Auth service verifies token (optionally tenant-scoped)  
3. Tenant service confirms tenant context  
4. Request is routed to appropriate domain service with context attached  

---

## 🧱 Data Isolation Models

### 1. **Shared Database with Tenant Identifiers**
- All tenants share one DB instance
- Each record is tagged with a `tenant_id`
- Simple, fast, but relies heavily on app-level logic

### 2. **Schema-Per-Tenant**
- Each tenant gets its own schema within a shared DB
- Medium isolation, easier backup/restore

### 3. **Dedicated Databases (Future Support)**
- Each tenant has its own database instance
- High isolation, high complexity, reserved for advanced use cases

---

## ⚙️ Configuration and Optional Modes

Bluewater can run in:
- **Single-Tenant Mode**:
- Tenant resolution is skipped
- Ideal for small deployments
- **Multi-Tenant Mode**:
- Tenant resolution and isolation are enforced
- Configurable per environment or service

Set via environment variable:
```env
BLUEWATER_TENANCY_MODE=multi
````

---

## 🗂️ File Structure

Each tenant may have a custom directory under `/app/` for overrides or tenant-specific extensions. The structure typically looks like:

```txt
/app/
├── common/                   # Shared utilities/helpers
│   └── helpers/
├── clientA/
│   ├── Controllers/
│   ├── Middleware/
│   ├── config/
│   └── helpers/
└── clientB/
    └── ...
```

This layout allows isolated customization while leveraging common shared logic.
See [`Common README`](../app/common/README.md) for usage guidance

---

## 🧠 Responsibilities

| Layer          | Function                               |
|----------------|----------------------------------------|
| `Controllers/` | Request logic per tenant               |
| `Middleware/`  | Tenant-specific processing/auth        |
| `config/`      | Per-tenant settings (e.g., DB, keys)   |
| `helpers/`     | Utility functions scoped to the tenant |

---

## 🧰 Dispatch Flow (Planned)

1. Incoming request hits router
2. Tenant is resolved via subdomain/header/path
3. Config + routes are loaded from `/app/{tenant}/`
4. Auth middleware is applied dynamically
5. Response is returned via `Responder`

---

## 🔒 Security Considerations

* Ensure tenant ID is validated server-side
* Never trust tenant context solely from client headers
* Token scopes should optionally include tenant ID
* Avoid accidental data leakage across tenants by validating all queries

---

## 🔐 Security Strategy

Each tenant can define its own authentication driver in config:

```php
return [
  'auth' => [
    'driver' => 'jwt',
    'secret' => 'client-specific-key',
    'issuer' => 'clientA',
  ]
];
```

Later: Support for OAuth/mTLS per tenant under `/security/`

---

## 🧰 Dispatch Flow (Planned)

1. Incoming request hits router
2. Tenant is resolved via subdomain/header/path
3. Config + routes are loaded from `/app/{tenant}/`
4. Auth middleware is applied dynamically
5. Response is returned via `Responder`

---

## ⚠️ Risks & Considerations

| Risk                        | Mitigation                                   |
|-----------------------------|----------------------------------------------|
| Config bleed across clients | Strict directory isolation (`/app/{client}`) |
| Route conflicts             | Namespace routes by tenant or version        |
| Auth leakage                | Require driver selection per-tenant          |
| Code duplication            | Use `/app/common` and helpers                |

---

## 📚 Related Documents

* [Architectural Overview](overview.md)
* [Component Responsibilities](components.md)
* [Deployment Strategy](deployment.md)

---

## 🧭 Next Steps

* [ ] Build a `TenantResolver` interface + default middleware
* [ ] Add route grouping per tenant
* [ ] Auto-merge common + client config
* [ ] Document fallback behavior

---

## ⚠️ Developer Responsibility Disclaimer

The `/app/common/` directory is **owned and maintained entirely by you** — the developer or internal team responsible for application-level logic.

Bluewater Framework does **not** ship, maintain, or version anything inside `app/`, including `common/`. As such:

- 🔧 **You control its structure and behavior**
- 🧪 **You are responsible for testing its stability**
- 🔄 **You are responsible for refactoring or updating code inside it**

If breaking changes occur due to modifications within `common/`, they are not the responsibility of the Bluewater maintainers or framework updates.

> 💡 Treat `common/` like your own private shared library — maintain contracts, add tests, and avoid breaking downstream tenants.

---

> ### 🪶 **Bluewater Principle**  
> *Tenants should feel like first-class citizens — but never see each other.*

---
