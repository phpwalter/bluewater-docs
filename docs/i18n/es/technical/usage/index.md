<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/usage/index.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Uso de aplicaciones – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/usage/index.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, usage, applications
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Arranque de aplicaciones y flujo de desarrollo habitual
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *El comportamiento de la aplicación utiliza contratos públicos y permanece fuera del código del proveedor.*

---

## 📌 Propósito

Esta guía establece el ciclo de vida de la aplicación y las reglas de trabajo utilizadas en las guías de uso específicas para cada tarea.

## Ciclo de vida del arranque

Cada aplicación debe definir una clase `Bootstrap` que implemente `Bluewater\ApplicationBootstrap`.

Ejemplo:

```php
<?php

declare(strict_types=1);

namespace Apps\App1;

use Bluewater\Application;
use Bluewater\ApplicationBootstrap;

final class Bootstrap implements ApplicationBootstrap
{
    public function register(Application $app): void
    {
        // Registrar servicios, enlaces y proveedores de autenticación,
        // serializadores, extensiones, implementaciones de bases de datos, etc.
    }

    public function boot(Application $app): void
    {
        // Registrar middleware global y realizar la inicialización final.
    }
}
```

Utilice `register()` para las definiciones y la conexión de servicios. Utilice `boot()` para la inicialización que dependa de la aplicación o el contenedor configurados.

No coloque lógica de aplicación específica de solicitudes en `Bootstrap`; corresponde al middleware o a los endpoints.

## Flujo de desarrollo de aplicaciones

Un cambio normal de la aplicación debe ser directo:

```text
create/edit endpoint, DTO, service, middleware or config
        ↓
run application tests
        ↓
exercise relevant route locally
        ↓
commit
        ↓
deploy
```

No se regenera un manifiesto de rutas después de agregar un endpoint.

No se agrega el espacio de nombres de la aplicación a Composer cada vez que se crea una clase nueva.

No se modifica Bluewater bajo `vendor/`.

No se crean subclases de componentes internos del framework para reemplazar servicios del núcleo, salvo que la API designe explícitamente un punto de herencia.

## Reglas prácticas

Mantenga claros estos límites:

```text
vendor/bluewater/framework
    = immutable framework package

app/app_1
    = application-owned code

app/app_1/cache
    = generated application runtime metadata

app/app_1/logs
    = application runtime logs
```

Prefiera enlaces de DI y extensiones explícitos en lugar de modificaciones improvisadas del framework. Prefiera middleware para la política de solicitudes. Prefiera DTO para entradas estructuradas. Prefiera interfaces de servicios o repositorios para el comportamiento de negocio. Permita que la convención de archivos defina las rutas habituales y utilice atributos solo cuando agreguen metadatos significativos o resuelvan necesidades excepcionales de enrutamiento.

## Guías de tareas

Utilice los documentos específicos de este directorio para el enrutamiento, la inyección de dependencias, la validación, las respuestas, el middleware, la autenticación, el acceso a bases de datos, las extensiones, OpenAPI y los registros.

## 📚 Documentos relacionados

- [Enrutamiento](routing.md)
- [Inyección de dependencias](dependency-injection.md)
- [Índice técnico](../index.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
