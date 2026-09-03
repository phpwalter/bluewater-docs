<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/setup/host-layout.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Estructura del host – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/setup/host-layout.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, setup, filesystem, namespace
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Instalación compartida del framework y directorios aislados de aplicaciones
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Los paquetes compartidos nunca implican un estado compartido entre aplicaciones.*

---

## 📌 Propósito

Esta guía define la estructura recomendada del sistema de archivos y el límite del espacio de nombres para una o más aplicaciones.

## Estructura del host

Un host de Bluewater puede servir varias aplicaciones aisladas mientras comparte una instalación física de Composer del framework y las dependencias comunes.

Estructura recomendada:

```text
host/
├── app/
│   ├── app_1/
│   │   ├── Bootstrap.php
│   │   ├── config/
│   │   ├── Endpoints/
│   │   ├── DTO/
│   │   ├── Middleware/
│   │   ├── Services/
│   │   ├── Extensions/
│   │   ├── cache/
│   │   └── logs/
│   ├── app_2/
│   └── app_3/
├── public/
│   ├── app_1/index.php
│   ├── app_2/index.php
│   └── app_3/index.php
├── vendor/
│   └── bluewater/framework/
└── composer.json
```

Cada aplicación tiene su propio espacio de nombres, configuración, endpoints, caché y registros. Las aplicaciones no comparten endpoints implícitamente.

## Estructura requerida de la aplicación

Como mínimo, cada aplicación necesita:

```text
app/app_1/
├── Bootstrap.php
├── config/
├── Endpoints/
├── cache/
└── logs/
```

Bluewater puede crear automáticamente `cache/` y `logs/` si no existen y se puede escribir en su ubicación. Una estructura requerida de aplicación ausente o no válida provoca un fallo explícito durante el arranque.

## Espacio de nombres de la aplicación

Cada aplicación tiene su propio espacio de nombres.

Ejemplo:

```text
app_1
```

podría utilizar:

```text
Apps\App1
```

Bluewater asigna dinámicamente ese espacio de nombres al directorio de la aplicación activa durante la ejecución. Agregar una aplicación nueva no requiere `composer dump-autoload` para las clases de la aplicación.

Una clase de endpoint típica se resuelve como:

```text
Apps\App1\Endpoints\Users
```

desde:

```text
app/app_1/Endpoints/users.php
```

## 📚 Documentos relacionados

- [Configuración inicial](index.md)
- [Configuración](configuration.md)
- [Despliegue](../deployment/index.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
