# 🔐 Authentication Integration – Bluewater

📄 **File:** `docs/integrations/auth.md`  
📅 **Status:** Stub  
🏷️ **Tags:** integrations, auth, jwt, oauth  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – Developers & API Consumers  
👨‍💻 **Author:** Bluewater Team

---

## Overview

Bluewater provides no built-in authentication logic but supports integration with modular auth mechanisms via middleware. This allows developers to use **JWT**, **OAuth2**, or any token-based system suitable for machine-to-machine APIs.

---

## 🔓 Supported Auth Mechanisms

| Type    | Use Case                             | Tool Examples                           |
|---------|--------------------------------------|-----------------------------------------|
| JWT     | Stateless API access                 | `lcobucci/jwt`, `firebase/php-jwt`      |
| OAuth2  | External identity brokers, SSO       | `league/oauth2-server`, `oauth2-client` |
| HMAC    | Internal token signatures for APIs   | Manual signature validation             |
| API Key | Basic static token with header check | Custom middleware                       |

---

## 🛠️ Integration Approach

1. Create **auth middleware** under `app/Middleware/`
2. Inspect and validate `Authorization` headers
3. Inject verified user/session context into request

---

## 📜 Sample JWT Middleware

```php
public function __invoke(ServerRequestInterface $req, RequestHandlerInterface $handler): ResponseInterface {
    $token = $req->getHeaderLine('Authorization');
    if (!$this->verifyToken($token)) {
        return new JsonResponse(['error' => 'Unauthorized'], 401);
    }
    return $handler->handle($req);
}
````

---

## 🧪 Libraries to Explore

```bash
composer require firebase/php-jwt
composer require lcobucci/jwt
composer require league/oauth2-server
```

---

## 🔐 Best Practices

* Validate expiration (`exp`), subject (`sub`), and issuer (`iss`) claims
* Store signing keys securely in `.env`
* Rotate secrets periodically

---

## 🔗 Related

* [`docs/security/jwt.md`](../security/jwt.md)
* [`docs/security/oauth.md`](../security/oauth.md)
* [`docs/security/nextgen.md`](../security/nextgen.md)
* [PSR-15 Middleware](https://www.php-fig.org/psr/psr-15/)
* [OAuth2 PHP Docs](https://oauth2.thephpleague.com/)

---

```
