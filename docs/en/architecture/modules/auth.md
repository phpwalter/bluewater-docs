### 📄 `docs/modules/auth.md`

# 🔐 Authentication Module – Bluewater Framework

📄 **File:** `docs/modules/auth.md`  
📅 **Status:** Stub  
🏷️ **Tags:** auth, jwt, oauth2, middleware  
🔖 **Version:** 1.0  
📦 **Scope:** 🧰 Developer-Facing – Internal & External  
👨‍💻 **Maintainer:** Bluewater Core Team

---

## 📘 OVERVIEW

This module defines how authentication is implemented and extended in Bluewater, including supported methods like JWT and OAuth2. Bluewater treats authentication as a plug-in middleware layer that can be tenant-specific.

---

## 🔐 Supported Drivers

| Driver    | Description                       | File Path            |
|-----------|-----------------------------------|----------------------|
| `jwt`     | JSON Web Token Auth               | `/security/jwt/`     |
| `oauth`   | OAuth2 client credentials flow    | `/security/oauth/`   |
| `nextgen` | Future/pluggable security systems | `/security/nextgen/` |

Each tenant config defines its own driver:

```php
return [
  'auth' => [
    'driver' => 'jwt',
    'secret' => 'client-key',
    'issuer' => 'clientA',
  ]
];
````

---

## 🧩 Middleware Integration

Authentication is handled via PSR-15 middleware injected per tenant or globally. Example:

```php
$app->middleware([
  new \Bluewater\Security\Jwt\JwtMiddleware($config)
]);
```

---

## 🔧 Extending Auth Modules

To create a custom auth module:

1. Implement `AuthInterface`
2. Register the new driver in the tenant config
3. Create a middleware to invoke and validate tokens

---

## 🧪 Testing Auth Flows

* Stub JWT headers for test calls
* Validate token decoding with invalid signatures
* Use mock user providers for isolated tests

---

## 🔗 Related Docs

* [`jwt.md`](../security/jwt.md)
* [`oauth.md`](../security/oauth.md)
* [`testing.md`](../testing/testing.md)
* [`multi-tenant.md`](../architecture/multi-tenant.md)

---

🔐 *Security should be explicit, testable, and replaceable.*

---
