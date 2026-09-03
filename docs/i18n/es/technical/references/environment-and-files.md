<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/references/environment-and-files.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Referencia de entorno y archivos – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/references/environment-and-files.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, references, environment, files
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Variables del entorno de ejecución, fuentes de configuración y archivos generados
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *La identidad del entorno de ejecución y las rutas del sistema de archivos son datos explícitos del despliegue.*

---

## 📌 Propósito

Esta referencia enumera las variables de entorno y los archivos que participan en la construcción de la aplicación.

## Variables de entorno

| Variable | Significado |
|---|---|
| `BLUEWATER_APP` | Identificador obligatorio del directorio de la aplicación proporcionado por el controlador frontal o el proceso. |
| `BLUEWATER_APP_BASE` | Directorio principal opcional que contiene las aplicaciones. |
| `BLUEWATER_ENV` | Entorno de ejecución opcional que sobrescribe el valor configurado de `BW_ENV`. |

## Configuración del framework

Los valores predeterminados del framework se encuentran en `config/`, dentro de archivos protegidos `BW.*.ini.php`, `Bluewater.ini.php` y archivos de sesión. Las sobrescrituras de la aplicación se encuentran en `<app>/config/` con los nombres `App.*` correspondientes.

## Archivos generados de la aplicación

| Archivo | Propiedad |
|---|---|
| `<app>/cache/config.php` | Configuración resuelta y compilada atómicamente; las aplicaciones no deben editarla. |
| `<app>/cache/routes.php` | Tabla de rutas y cadena de middleware compiladas atómicamente; las aplicaciones no deben editarlas. |
| `<app>/logs/application.log` | Salida predeterminada del registrador de archivos cuando el registro está habilitado. |

## 📚 Documentos relacionados

- [Configuración de la aplicación](../setup/configuration.md)
- [Estructura del host](../setup/host-layout.md)
- [Referencias técnicas](index.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
