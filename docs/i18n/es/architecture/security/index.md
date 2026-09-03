<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/security/index.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Arquitectura de seguridad – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/security/index.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, security, trust-boundaries, fail-closed
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Controles de seguridad implementados, responsabilidades del llamador y límites conocidos
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *Las credenciales, rutas, configuraciones e identidades de aplicación desconocidas provocan un cierre seguro.*

---

## 📌 Propósito

Este documento registra el comportamiento de seguridad verificado en Bluewater v8 y evita atribuir protecciones que el framework no implementa.

## Controles implementados

- Los identificadores de aplicación se restringen antes de componer rutas del sistema de archivos.
- Los conflictos de rutas y los contratos de marcadores no válidos hacen fallar el descubrimiento.
- La configuración rechaza cambios en claves bloqueadas, cambios de tipo, referencias ambiguas y ciclos.
- Las comparaciones de claves de API utilizan `hash_equals()` y no exponen las claves en las identidades.
- La verificación JWT solo acepta el HS256 configurado, valida la firma y las declaraciones temporales y, opcionalmente, exige un emisor y una audiencia exactos.
- La autenticación Bearer de OAuth exige que un introspector de la aplicación informe un estado activo literal y una identidad.
- Las respuestas de problemas en producción omiten los mensajes de excepción.
- Las conexiones PDO utilizan de forma predeterminada sentencias preparadas nativas y el modo de error por excepciones.

## Obligaciones de la aplicación

Las aplicaciones deben implementar autorización, almacenamiento y rotación de secretos, protección CSRF cuando se utilicen cookies, política CORS, límites de tamaño de solicitudes, limitación de frecuencia, persistencia de auditoría, cumplimiento del aislamiento de inquilinos, clasificación de datos de salida, privilegio mínimo en la base de datos y seguridad de infraestructura. La autenticación por sí sola nunca concede permisos de dominio.

## Límites conocidos

El proveedor JWT integrado utiliza un secreto compartido y no obtiene JWKS ni gestiona la rotación. Actualmente, el análisis del JSON de una solicitud convierte un JSON mal formado en `null`. La serialización de objetos expone las propiedades públicas. Las respuestas de desarrollo pueden incluir detalles de excepciones y nunca deben habilitarse en producción.

## 📚 Documentos relacionados

- [Autenticación](authentication.md)
- [Configuración](../configuration/index.md)
- [Acceso a datos](../data/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
