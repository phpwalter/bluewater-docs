<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/usage/middleware.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Middleware de aplicaciones – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/usage/middleware.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, usage, middleware
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Middleware global, de directorio, clase y método
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *La política de solicitudes se ejecuta en un orden visible y determinista.*

---

## 📌 Propósito

Esta guía explica la creación, el registro, el ámbito y el orden del middleware, así como la integración con PSR-15.

## Middleware

Bluewater admite cuatro ámbitos efectivos de middleware.

### Middleware global

Regístrelo en `Bootstrap::boot()`.

Ejemplo:

```php
public function boot(Application $app): void
{
    $app->middleware()->add(RequestLoggingMiddleware::class);
}
```

Utilícelo para el comportamiento que se aplica a toda la aplicación.

Ejemplos:

- registro de solicitudes;
- CORS;
- trazabilidad;
- encabezados de seguridad globales.

### Middleware de directorio

Cree:

```text
Endpoints/admin/_middleware.php
```

que devuelve nombres de clases de middleware:

```php
<?php

return [
    AdminAuthenticationMiddleware::class,
];
```

Los endpoints ubicados bajo ese directorio heredan el middleware.

### Middleware de clase de endpoint

Utilice `#[UseMiddleware]` repetible en la clase de endpoint.

```php
use Bluewater\Middleware\UseMiddleware;

#[UseMiddleware(AppHeaderMiddleware::class)]
final class Users extends Endpoint
{
}
```

### Middleware de método de endpoint

Aplique middleware a un manejador HTTP:

```php
#[UseMiddleware(DeleteAuthorizationMiddleware::class)]
public function deleteById(int $id): Response
{
    // ...
}
```

## 📚 Documentos relacionados

- [Autenticación](authentication.md)
- [Enrutamiento](routing.md)
- [Uso](index.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
