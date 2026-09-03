<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../../i18n/es/technical/usage/dependency-injection.md) | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Application Dependency Injection – Bluewater Framework

📄 **File:** `docs/en/technical/usage/dependency-injection.md`
📅 **Status:** Active
🏷️ **Tags:** technical, usage, container, services
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Endpoint parameter binding and application service registration
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Dependencies remain explicit at handler and constructor boundaries.*

---

## 📌 Purpose

This guide explains how endpoint parameters and application services resolve through the container.

## Request parameters and dependency injection

Endpoint arguments are resolved automatically.

Resolution includes:

1. route parameters;
2. query-string parameters;
3. Bluewater `Request` injection;
4. DTO hydration from the request body;
5. registered/autowireable services from the DI container;
6. default parameter values.

Example:

```php
public function getById(
    int $id,
    UserRepository $users,
): UserDto {
    return $users->find($id);
}
```

`$id` comes from the route and `UserRepository` comes from the container.

## Registering application services

Use `Bootstrap::register()`.

Example:

```php
public function register(Application $app): void
{
    $app->services()->bind(
        UserRepository::class,
        DatabaseUserRepository::class,
    );
}
```

Concrete services with resolvable constructors may be autowired without explicit registration.

Use explicit bindings when:

- injecting an interface;
- replacing a Bluewater/default implementation;
- creating services requiring configuration or factories;
- choosing between multiple implementations.

## 📚 Related Documents

- [Routing](routing.md)
- [Validation](validation.md)
- [Container development](../development/dependency-injection.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
