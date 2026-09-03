<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/testing/framework.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Pruebas del framework – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/testing/framework.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, testing, phpunit, phpstan, phpcs
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Validación unitaria, de integración, estática, con hosts externos y de solicitudes de incorporación
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Los cambios del núcleo superan todos los controles de calidad antes de la revisión.*

---

## 📌 Propósito

Esta guía define el contrato completo de validación para los cambios del framework Bluewater.

## Pruebas unitarias

Las pruebas deben reflejar el subsistema del framework cuando sea posible.

Ejemplos:

```text
src/Config/ConfigFactory.php
    → tests/Config/ConfigFactoryTest.php

src/Routing/Router.php
    → tests/Routing/RouterTest.php

src/Container/Container.php
    → tests/Container/ContainerTest.php
```

Ejecute el conjunto completo de PHPUnit con:

```bash
vendor/bin/phpunit
```

Ejecute un archivo de prueba durante el desarrollo:

```bash
vendor/bin/phpunit tests/Routing/RouterTest.php
```

Ejecute una sola prueba por nombre:

```bash
vendor/bin/phpunit --filter testMethodsDeriveFileBasedRoutesWithoutManifest
```

## Pruebas de integración con `app_1`

`examples/host/app/app_1` es la aplicación de referencia y el recurso de integración del framework.

Actualmente ejercita:

- carga dinámica del espacio de nombres de la aplicación;
- ciclo de vida requerido de `Bootstrap`;
- sobrescrituras de configuración de la aplicación;
- integración con SQLite/PDO;
- endpoints de estado y usuarios;
- validación de DTO;
- middleware global;
- middleware de directorio;
- middleware de clase;
- middleware de método;
- autenticación mediante clave de API;
- autenticación JWT;
- introspección de OAuth;
- extensiones explícitas de la aplicación;
- OpenAPI generado.

Un cambio del framework que afecte el comportamiento normal de la aplicación normalmente debe agregar o actualizar una prueba de integración que utilice esta aplicación.

El principio es:

> Las pruebas unitarias demuestran el subsistema. `app_1` demuestra el framework.

## Validación obligatoria antes de una solicitud de incorporación

Ejecute:

```bash
composer check
```

El proyecto también admite:

```bash
composer validate --strict
vendor/bin/phpunit
```

`composer check` es el control mínimo de aceptación local antes de enviar un cambio del framework.

Actualmente, GitHub Actions valida Bluewater en:

```text
PHP 8.3
PHP 8.4
```

La integración continua realiza la validación de Composer, la instalación de dependencias, las comprobaciones de sintaxis y el conjunto de PHPUnit.

## Pruebas con aplicaciones externas durante el desarrollo del framework

Para realizar pruebas de compatibilidad más profundas, utilice otro proyecto local de Composer con un repositorio de ruta.

Ejemplo de espacio de trabajo:

```text
development/
├── bluewater-framework/
└── customer-api-host/
```

En el `composer.json` del host externo:

```json
{
    "repositories": [
        {
            "type": "path",
            "url": "../bluewater-framework",
            "options": {
                "symlink": true
            }
        }
    ],
    "require": {
        "bluewater/framework": "@dev"
    }
}
```

A continuación, ejecute:

```bash
composer update bluewater/framework
```

La aplicación utilizará la copia de trabajo local del framework mediante Composer, lo que permite probar aplicaciones reales sin copiar el código fuente de Bluewater en la aplicación.

## 📚 Documentos relacionados

- [Pruebas](index.md)
- [Flujo de contribución](../development/contributing.md)
- [Desarrollo del núcleo](../development/index.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
