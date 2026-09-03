<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/usage/routing.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Endpoints y enrutamiento – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/usage/routing.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, usage, endpoints, routing
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Endpoints basados en archivos, nombres de manejadores, rutas, conflictos y cachés
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Agregar un endpoint habitual requiere un archivo, no un segundo manifiesto de rutas.*

---

## 📌 Propósito

Esta guía explica cómo los archivos y métodos de endpoints de la aplicación producen rutas deterministas.

## Creación de endpoints

Bluewater utiliza el descubrimiento de endpoints basado en archivos. No es necesario mantener un manifiesto de rutas.

Cree:

```text
app/app_1/Endpoints/users.php
```

Ejemplo:

```php
<?php

declare(strict_types=1);

namespace Apps\App1\Endpoints;

use Bluewater\Endpoint\Endpoint;

final class Users extends Endpoint
{
    public function get(): array
    {
        return [
            ['id' => 1, 'name' => 'Ada'],
        ];
    }

    public function getById(int $id): array
    {
        return [
            'id' => $id,
            'name' => 'Ada',
        ];
    }
}
```

Bluewater deriva:

```text
GET /users
GET /users/{id}
```

No se requiere registro de rutas, manifiesto generado ni paso de compilación manual.

## Nombres de manejadores HTTP

Los manejadores normales utilizan convenciones de verbos HTTP:

```text
get
post
put
patch
delete
options
head
```

Ejemplos:

```php
public function get(): array
public function post(CreateUserRequest $request): UserDto
public function deleteById(int $id): Response
```

Los parámetros de rutas dinámicas pueden derivarse de nombres de manejadores `By...`.

Ejemplo:

```php
public function getByAccountIdAndUserId(
    int $accountId,
    int $userId,
): array
```

puede derivar una forma de ruta con los parámetros dinámicos correspondientes.

## Rutas excepcionales con `#[Path]`

No fuerce URL complejas en nombres de métodos cada vez más complicados.

Utilice `#[Path]` cuando la convención no sea suficiente.

Ejemplo:

```php
use Bluewater\Routing\Path;

#[Path('/{id}/permissions')]
public function getPermissions(int $id): array
{
    return ['user_id' => $id, 'permissions' => []];
}
```

Para `users.php`, esto produce:

```text
GET /users/{id}/permissions
```

Bluewater valida durante el descubrimiento que los marcadores de ruta coincidan con los parámetros del método.

## Conflictos de rutas

Los conflictos de rutas provocan un fallo explícito.

Por ejemplo, las siguientes se consideran la misma forma de ruta:

```text
/users/{id}
/users/{name}
```

Si ambas se registran para el mismo método HTTP, el inicio o el descubrimiento de la aplicación falla en lugar de elegir una silenciosamente.

Las rutas estáticas tienen precedencia sobre las rutas dinámicas.

## Caché automática de rutas

Bluewater compila automáticamente las rutas descubiertas en el directorio de caché de la aplicación activa.

Ejemplo:

```text
app/app_1/cache/routes.php
```

No edite este archivo.

Cuando cambian archivos de endpoints o de middleware de directorio heredado, Bluewater detecta el cambio y reconstruye atómicamente la caché de rutas.

Agregar un archivo de endpoint es suficiente para que esté disponible; no se requiere ningún comando de compilación del desarrollador.

## 📚 Documentos relacionados

- [Uso](index.md)
- [Inyección de dependencias](dependency-injection.md)
- [Desarrollo del enrutamiento](../development/routing.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
