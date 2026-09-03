### 📄 `docs/security/oauth.md`

# 🔐 OAuth2 Support – Bluewater Framework

📄 **File:** `docs/security/oauth.md`  
📅 **Status:** Stub  
🏷️ **Tags:** oauth, security, authentication, middleware  
🔖 **Version:** 1.0  
📦 **Scope:** 🔐 Security – API Consumers & Providers  
👨‍💻 **Maintainer:** Bluewater Core Team

---

## 📘 OVERVIEW

OAuth2 is a widely adopted protocol for **delegated authorization**, often used to allow applications to access user resources without sharing credentials. Bluewater supports OAuth2 via pluggable middleware that integrates with third-party providers or internal auth servers.

This module is intended for **machine-to-machine** and **tenant-scoped** client authentication.

---

## 🔧 Integration Modes

| Mode                    | Use Case                         | Notes                                |
|-------------------------|----------------------------------|--------------------------------------|
| Client Credentials Flow | Server-to-server communication   | Ideal for API-only apps (no UI)      |
| Token Introspection     | Validate access tokens remotely  | Requires endpoint from auth provider |
| OAuth Proxy             | Reverse proxy handles auth logic | Bluewater receives verified tokens   |

---

## ⚙️ Example Config (Per-Tenant)

```php
return [
  'auth' => [
    'driver'     => 'oauth',
    'provider'   => 'auth0', // or 'internal'
    'client_id'  => env('OAUTH_CLIENT_ID'),
    'client_secret' => env('OAUTH_CLIENT_SECRET'),
    'token_url'  => 'https://example.com/oauth/token',
    'introspect_url' => 'https://example.com/oauth/introspect'
  ]
];
````

---

## 🧩 Middleware Behavior

* Extracts `Authorization: Bearer` token
* Validates format and forwards to introspection endpoint
* On success: injects verified user context into request
* On failure: returns standardized 401/403 error payloads

---

## 📚 Libraries & Standards

* [league/oauth2-client](https://oauth2-client.thephpleague.com/)
* [RFC 6749](https://datatracker.ietf.org/doc/html/rfc6749)
* [RFC 7662 - Introspection](https://datatracker.ietf.org/doc/html/rfc7662)

---

## ⚠️ Considerations

| Issue                | Strategy                                      |
| -------------------- | --------------------------------------------- |
| Token validation     | Use short-lived tokens and introspection      |
| Key rotation         | Integrate JWKS endpoint if supported          |
| Per-tenant providers | Use scoped config per `/app/{tenant}/config/` |
| Network latency      | Cache token introspection results             |

---

## 🔄 Transition Strategy

Want to start with JWT and upgrade to OAuth later?

✅ Design the system to abstract authentication through the Bluewater `AuthManager`, and route requests through middleware defined by `driver`.

---

## 🔗 Related

* [`jwt.md`](jwt.md)
* [`auth-modules.md`](auth-modules.md)
* [`middleware.md`](../core/middleware.md)

---

📎 *OAuth gives your API third-party power with first-party control.*

---
