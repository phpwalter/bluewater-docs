<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/runtime/deployment.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Entorno de ejecución y despliegue – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/runtime/deployment.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, runtime, fpm, deployment
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Límite del adaptador del entorno de ejecución y selección de aplicaciones en producción
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *El núcleo es independiente del entorno de ejecución; los adaptadores controlan la E/S de transporte.*

---

## 📌 Propósito

Este documento define el límite PHP-FPM implementado y las responsabilidades de despliegue que corresponden a los operadores.

## Adaptador del entorno de ejecución

`RuntimeAdapter` tiene dos operaciones: crear una solicitud de Bluewater y emitir una respuesta de Bluewater. `FpmAdapter` es la implementación inicial. Lee las variables globales de PHP mediante `Request::fromGlobals()`, aplica el estado y los encabezados de la respuesta y escribe el cuerpo.

## Controlador frontal

El controlador frontal carga Composer, obtiene el identificador confiable de la aplicación de `BLUEWATER_APP`, crea un host y ejecuta el adaptador FPM. `BLUEWATER_APP_BASE` puede sobrescribir el directorio principal de aplicaciones, mientras que `BLUEWATER_ENV` puede sobrescribir el entorno configurado.

## Responsabilidades de producción

Los operadores son responsables de la terminación TLS, el enrutamiento del servidor web, la configuración de grupos FPM, los permisos de procesos, la inyección de secretos, el escalado, la supervisión de estado, la recopilación de registros, las copias de seguridad y los controles de red. Se recomienda un grupo FPM separado para cada aplicación. Bluewater no aprovisiona contenedores, recursos de Kubernetes, balanceadores de carga ni infraestructura en la nube.

## 📚 Documentos relacionados

- [Aislamiento de aplicaciones](application-isolation.md)
- [Seguridad](../security/index.md)
- [Guía para desarrolladores de aplicaciones](../../technical/usage/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
