<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/usage/authentication.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Autenticación de aplicaciones – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/usage/authentication.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, usage, authentication, security
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Configuración de proveedores de clave de API, JWT y Bearer de OAuth
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *La autenticación selecciona un proveedor y aplica un cierre seguro sin conceder autorización.*

---

## 📌 Propósito

Esta guía explica el registro de proveedores, los endpoints protegidos, el acceso a la identidad y los límites de seguridad.

## Autenticación

La autenticación se controla mediante middleware. La lógica de negocio de los endpoints no debe analizar manualmente JWT ni claves de API, salvo que exista una razón muy específica.

Bluewater proporciona compatibilidad inicial con:

- claves de API;
- JWT HS256;
- tokens Bearer de OAuth mediante un introspector proporcionado por la aplicación.

Registre los proveedores en `Bootstrap::register()` y adjunte el middleware correspondiente de forma global, por directorio, clase o método.

Esto mantiene la política de autenticación separada de la lógica de negocio de los endpoints.

## 📚 Documentos relacionados

- [Middleware](middleware.md)
- [Configuración de la aplicación](../setup/configuration.md)
- [Pruebas de aplicaciones](../testing/applications.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
