### 🧰 `docs/core/middleware.md` — Stub Content

# 🧰 Middleware – Bluewater Core Module

📄 **File:** `docs/core/middleware.md`  
📅 **Status:** Published  
🏷️ **Tags:** `core`, `middleware`, `psr-15`, `lifecycle` , `security`, `routing` 
🔖 **Version:** 1.0  
📦 **Scope:** 📦 Contributors – Middleware developers and backend integrators  
👨‍💻 **Author:** Bluewater Team

---

## 🧩 Overview

Middleware in Bluewater follows the [PSR-15](https://www.php-fig.org/psr/psr-15/) standard for HTTP server request handlers. Middleware enables composable, layered processing of HTTP requests and responses.

Each middleware component can:
- Pre-process requests (e.g. authentication, validation)
- Short-circuit execution (e.g. block access)
- Post-process responses (e.g. add headers, log)

---

## 🧪 Middleware Pipeline

Requests are passed through a stack of middleware defined in the route or global middleware registration. Middleware are executed in order, with control passed down the stack until a response is returned.

```php
public function __invoke(ServerRequestInterface $request, RequestHandlerInterface $handler): ResponseInterface
{
    // Before handler
    $user = $this->auth->check($request);

    if (!$user) {
        return new JsonResponse(['error' => 'Unauthorized'], 401);
    }

    // Continue to next middleware or controller
    $response = $handler->handle($request);

    // After handler
    return $response->withHeader('X-App-Version', '1.0.0');
}
````

---

## 🧷 Registration

Middleware is typically registered:

* **Globally** via `app/config/middleware.php`
* **Per-route** using the route definition DSL

```php
Route::get('/api/users', [UserController::class, 'index'])
     ->middleware([AuthMiddleware::class, RateLimitMiddleware::class]);
```

---

## 🔐 Security Middleware

Common use cases:

* **Authentication**: JWT, OAuth
* **Rate limiting**: Redis-based token buckets
* **CORS**: Add cross-origin headers
* **Input sanitization**: Validate before hitting the controller

---

## 🧪 Testing Middleware

Middleware can be tested in isolation using mocks for `ServerRequestInterface` and `RequestHandlerInterface`.

---

## 📦 PSR Compatibility

| PSR                                           | Description                     |
|-----------------------------------------------|---------------------------------|
| [PSR-7](https://www.php-fig.org/psr/psr-7/)   | HTTP Message Interfaces         |
| [PSR-15](https://www.php-fig.org/psr/psr-15/) | HTTP Server Middleware Standard |

---

## ✅ Summary

Bluewater middleware empowers precise control over request handling with minimal boilerplate. Middleware can be global, route-specific, or dynamically injected — making it an essential pattern in the framework.

---

## 🔗 Related Docs

* [Dispatcher](dispatcher.md)
* [Auth Modules](../security/auth-modules.md)
* [Testing Middleware](../testing/testing.md)
