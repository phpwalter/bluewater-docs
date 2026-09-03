<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../../i18n/es/technical/usage/middleware.md) | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Application Middleware – Bluewater Framework

📄 **File:** `docs/en/technical/usage/middleware.md`
📅 **Status:** Active
🏷️ **Tags:** technical, usage, middleware
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Global, directory, class, and method middleware
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Request policy executes in a visible and deterministic order.*

---

## 📌 Purpose

This guide explains middleware creation, registration, scope, ordering, and PSR-15 integration.

## Middleware

Bluewater supports four effective middleware scopes.

### Global middleware

Register in `Bootstrap::boot()`.

Example:

```php
public function boot(Application $app): void
{
    $app->middleware()->add(RequestLoggingMiddleware::class);
}
```

Use for behavior that applies to the entire application.

Examples:

- request logging;
- CORS;
- tracing;
- global security headers.

### Directory middleware

Create:

```text
Endpoints/admin/_middleware.php
```

returning middleware class names:

```php
<?php

return [
    AdminAuthenticationMiddleware::class,
];
```

Endpoints below that directory inherit the middleware.

### Endpoint-class middleware

Use repeatable `#[UseMiddleware]` on the endpoint class.

```php
use Bluewater\Middleware\UseMiddleware;

#[UseMiddleware(AppHeaderMiddleware::class)]
final class Users extends Endpoint
{
}
```

### Endpoint-method middleware

Apply middleware to one HTTP handler:

```php
#[UseMiddleware(DeleteAuthorizationMiddleware::class)]
public function deleteById(int $id): Response
{
    // ...
}
```

## 📚 Related Documents

- [Authentication](authentication.md)
- [Routing](routing.md)
- [Usage](index.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
