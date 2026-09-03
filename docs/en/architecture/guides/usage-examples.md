### 📄 `docs/guides/usage-examples.md`

# 🧪 Usage Examples – Bluewater Framework

📄 **File:** `docs/guides/usage-examples.md`  
📅 **Status:** Stub  
🏷️ **Tags:** examples, demos, usage, sample  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – Developers and contributors  
👨‍💻 **Author:** Bluewater Team

---

## 📌 Purpose

This guide contains **real-world usage examples** of Bluewater components. It helps developers learn by doing — with minimal boilerplate and maximum clarity.

Each example highlights one part of the system in isolation.

---

## ✨ Hello World Endpoint

Create a simple `HelloController` under your client:

```php
// app/clientA/Controllers/HelloController.php

namespace App\ClientA\Controllers;

class HelloController {
  public function index() {
    return ['message' => 'Hello, Bluewater!'];
  }
}
````

Register a route in your tenant’s router config:

```php
$router->get('/hello', [HelloController::class, 'index']);
```

📡 Visit: `http://localhost:8000/hello`

---

## 🔐 Adding Simple Auth Middleware

```php
// app/clientA/Middleware/TokenCheck.php

namespace App\ClientA\Middleware;

use Psr\Http\Message\ServerRequestInterface;
use Psr\Http\Message\ResponseInterface;

class TokenCheck {
  public function __invoke(ServerRequestInterface $request, callable $next): ResponseInterface {
    $token = $request->getHeaderLine('X-Auth-Token');
    if ($token !== getenv('API_TOKEN')) {
      return new \Bluewater\Responder\JsonResponse(['error' => 'Unauthorized'], 401);
    }
    return $next($request);
  }
}
```

Apply it in your route or globally.

---

## 🧪 JSON Response Formatting

Use Bluewater's `Responder` utility:

```php
return $responder->json([
  'data' => [...],
  'meta' => ['status' => 200]
]);
```

Customizable output structure via config.

---

## 🧵 Chaining Middleware

```php
$router->group('/v1', function($group) {
  $group->use(new AuthMiddleware());
  $group->get('/profile', [ProfileController::class, 'show']);
});
```

Middleware execution is PSR-15 compatible and runs in sequence.

---

## 📦 CLI Utilities

List all routes:

```bash
bin/bluewater route:list
```

Clear cache:

```bash
bin/bluewater cache:clear
```

Export merged config:

```bash
bin/bluewater config:dump
```

---

## 🧠 More Examples Coming Soon

* [ ] File upload handler
* [ ] OAuth client token flow
* [ ] Per-client config loading
* [ ] Middleware composition with error handling

---

🧠 *Examples should teach patterns, not just syntax.*
