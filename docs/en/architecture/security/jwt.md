### 📄 `docs/security/jwt.md`

# 🔐 JWT Authentication – Bluewater Framework

📄 **File:** `docs/security/jwt.md`  
📅 **Status:** Stub  
🏷️ **Tags:** security, jwt, tokens, middleware  
🔖 **Version:** 1.0  
📦 **Scope:** 🔐 Security – API Developers  
👨‍💻 **Maintainer:** Bluewater Core Team

---

## 📘 OVERVIEW

JSON Web Tokens (JWT) provide a stateless, scalable mechanism for authenticating API clients in Bluewater. This document covers how JWT works, how to integrate it, and how to configure it for single or multi-tenant usage.

---

## 🛠️ Key Features

- Stateless verification (no session persistence)
- Encoded in standard compact JWT format
- Signature-based tamper prevention (HMAC or RSA)
- Tenant-specific secrets and issuers

---

## 📦 Configuration Example

```php
return [
  'auth' => [
    'driver'  => 'jwt',
    'issuer'  => 'bluewater-client',
    'secret'  => env('JWT_SECRET'),
    'ttl'     => 3600
  ]
];
````

---

## 📄 Token Structure

A JWT has 3 parts:

```text
header.payload.signature
```

### Example Payload:

```json
{
  "sub": "user-123",
  "iat": 1686024382,
  "exp": 1686027982,
  "scope": "read:users"
}
```

---

## 🔐 Middleware Usage

The Bluewater JWT middleware:

* Extracts `Authorization: Bearer` tokens
* Validates signature + expiry
* Injects payload into the request context

Use via your middleware stack or route grouping.

---

## 🧪 Testing Strategy

* Use mock tokens with known secrets
* Validate payload extraction via unit tests
* Test token expiration and refresh logic

---

## ⚠️ Considerations

| Risk              | Mitigation                                    |
| ----------------- | --------------------------------------------- |
| Token tampering   | Use strong secrets and HMAC SHA-256 or better |
| Secret exposure   | Use `.env` or config vaults                   |
| Expiry handling   | Build a refresh system if required            |
| Scope enforcement | Implement a permission system if needed       |

---

## 🔗 Related

* [`auth-modules.md`](auth-modules.md)
* [`middleware.md`](../core/middleware.md)
* [JWT Spec (RFC 7519)](https://datatracker.ietf.org/doc/html/rfc7519)
* [JWT.io Debugger](https://jwt.io/)

---

📎 *JWT is secure, fast, and perfect for stateless APIs — just don’t forget to rotate your keys.*

---
