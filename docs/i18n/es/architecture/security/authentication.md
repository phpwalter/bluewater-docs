<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/security/authentication.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Arquitectura de autenticación – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/security/authentication.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, authentication, api-key, jwt, oauth
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Selección y validación del proveedor de credenciales, asignación de identidad y denegación
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *La autenticación elige un verificador configurado y aplica un cierre seguro ante fallos.*

---

## 📌 Propósito

Este documento describe los proveedores de autenticación de Bluewater y distingue la autenticación de la autorización.

## Selección del proveedor

`AuthManager` almacena proveedores bajo nombres de estrategia recortados y en minúsculas. Los nombres duplicados hacen fallar el registro. La autenticación selecciona exactamente un proveedor con nombre; nunca intenta usar un proveedor predeterminado o alternativo. Las estrategias desconocidas generan una excepción, mientras que la denegación esperada de credenciales devuelve `null`.

## Proveedores integrados

| Proveedor | Comprobaciones aplicadas |
|---|---|
| Clave de API | Encabezado configurado, clave no vacía, comparación en tiempo constante y asignación de identidad configurada. |
| JWT | Sintaxis Bearer, estructura compacta, validez de base64url y JSON, algoritmo HS256 exacto, firma HMAC, `exp` y `sub` obligatorios, `nbf` opcional y emisor/audiencia configurados. |
| Bearer de OAuth | Sintaxis Bearer y un introspector proporcionado por la aplicación que devuelve literalmente `active=true` junto con `sub` o `client_id` no vacíos. |

Las claves de API y los tokens Bearer sin procesar no se copian en la `Identity` resultante. Las clases proveedoras autentican; no deciden si la identidad puede realizar una acción de dominio. La autorización pertenece al middleware o a los servicios de la aplicación.

## Límite actual de JWT

El proveedor JWT integrado solo admite HS256 con secreto compartido. Este proveedor no implementa algoritmos de clave pública, obtención de JWKS, rotación de claves, almacenes contra repetición, tokens de actualización ni emisión de tokens.

## 📚 Documentos relacionados

- [Seguridad](index.md)
- [Middleware](../http/middleware.md)
- [Guía para desarrolladores de aplicaciones](../../technical/usage/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
