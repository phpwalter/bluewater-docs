<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/setup/configuration.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Configuración de la aplicación – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/setup/configuration.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, setup, configuration
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Selección de aplicaciones, sobrescrituras, referencias, cachés y controles de funcionalidades
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Las sobrescrituras heredan deliberadamente y fallan cuando infringen la propiedad del framework.*

---

## 📌 Propósito

Esta guía explica cómo los operadores seleccionan una aplicación y cómo las aplicaciones sobrescriben la configuración protegida del framework.

## Selección de la aplicación

El servidor web o el grupo PHP-FPM selecciona la aplicación externamente.

Variables de entorno habituales:

```text
BLUEWATER_APP=app_1
BLUEWATER_ENV=production
BLUEWATER_APP_BASE=/var/www/bluewater-host/app
```

Utilice un grupo FPM separado para cada aplicación cuando sea posible. Esto proporciona a cada aplicación una configuración aislada en el nivel de proceso, mientras todas pueden compartir el mismo árbol físico `vendor/`.

El controlador frontal debe permanecer genérico.

Ejemplo:

```php
<?php

declare(strict_types=1);

use Bluewater\Host;
use Bluewater\Runtime\FpmAdapter;

require dirname(__DIR__, 3) . '/vendor/autoload.php';

$appName = getenv('BLUEWATER_APP');
if (!is_string($appName) || $appName === '') {
    throw new RuntimeException('BLUEWATER_APP must be configured by the runtime.');
}

Host::fromEnvironment()
    ->application($appName)
    ->run(new FpmAdapter());
```

## Configuración

Los valores predeterminados del framework Bluewater se instalan en:

```text
vendor/bluewater/framework/config/
```

No los modifique.

Las sobrescrituras de la aplicación se ubican en:

```text
app/app_1/config/
```

Ejemplos:

```text
App.ini.php
App.db.ini.php
App.logging.ini.php
```

Bluewater carga primero los valores predeterminados y después las sobrescrituras de la aplicación.

No necesita copiar todos los archivos de configuración del núcleo en la aplicación. Cree únicamente las sobrescrituras que necesite.

Ejemplo:

```ini
<?php
exit;
?>
[database]
DRIVER = sqlite
DATABASE = "{APP_ROOT}/data/app.sqlite"
```

El encabezado PHP protegido forma parte de la convención de archivos de configuración de Bluewater.

## Referencias de configuración

Los valores de configuración pueden hacer referencia a otros valores aprobados.

Ejemplos:

```ini
LOG_PATH = "{APP_ROOT}/logs"
CACHE_FILE = "{CACHE_ROOT}/example.php"
```

Los marcadores heredados compatibles del entorno de ejecución incluyen:

```text
{APP_ROOT}
{CACHE_ROOT}
{BLUEWATER}
{SITE_ROOT}
{DS}
```

Las referencias desconocidas y circulares provocan un fallo explícito durante el arranque.

## Identidad inmutable del framework

Las aplicaciones no pueden sobrescribir identidades bloqueadas del framework como:

```text
BW_VER
```

Si una aplicación intenta modificar una opción bloqueada, Bluewater hace fallar el arranque en lugar de ignorarla silenciosamente.

## Caché de configuración

La configuración efectiva combinada se compila en:

```text
app/app_1/cache/config.php
```

No edite este archivo.

Bluewater lo regenera cuando cambia la configuración fuente.

## Costo de funcionalidades y desactivación de servicios

Bluewater está diseñado para que los servicios opcionales no impongan trabajo de inicio cuando están deshabilitados.

Por ejemplo, una aplicación que no utilice OpenAPI ni integración con bases de datos no debe inicializar esos servicios innecesariamente.

Mantenga deliberados y mínimos los registros de arranque de la aplicación.

## 📚 Documentos relacionados

- [Estructura del host](host-layout.md)
- [Referencia de entorno y archivos](../references/environment-and-files.md)
- [Componentes internos de configuración](../development/configuration.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
