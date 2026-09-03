<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/runtime/application-isolation.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Aislamiento de aplicaciones – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/runtime/application-isolation.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, multi-application, isolation
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Límites del sistema de archivos, espacio de nombres, configuración, caché y procesos
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *El código compartido del framework no debe implicar un estado compartido entre aplicaciones.*

---

## 📌 Propósito

Este documento explica cómo varias aplicaciones comparten una instalación de Composer mientras conservan estados independientes del entorno de ejecución.

## Modelo de aislamiento

Cada aplicación posee su directorio, espacio de nombres PHP, sobrescrituras de configuración, endpoints, caché, registros, clase de arranque, contenedor, canalización de middleware, enrutador y registro de extensiones. Las aplicaciones no descubren los endpoints de otras aplicaciones ni reutilizan sus contenedores de servicios.

```text
host/
├── app/app_1/{Bootstrap.php,config,Endpoints,cache,logs}
├── app/app_2/{Bootstrap.php,config,Endpoints,cache,logs}
├── public/app_1/index.php
├── public/app_2/index.php
└── vendor/bluewater/framework
```

## Límite de confianza

La identidad de la aplicación se proporciona mediante una configuración de proceso o servidor web de confianza. No debe seleccionarse a partir de datos de solicitud no confiables. Se recomienda un grupo PHP-FPM separado para cada aplicación porque también aísla el entorno del proceso y el estado de los trabajadores.

Bluewater valida el nombre de la aplicación antes de unirlo a la raíz de aplicaciones configurada. La validación del identificador no sustituye los permisos del sistema operativo; los despliegues deben seguir restringiendo la propiedad de los archivos y los directorios escribibles.

## 📚 Documentos relacionados

- [Configuración](../configuration/index.md)
- [Entorno de ejecución y despliegue](deployment.md)
- [Seguridad](../security/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
