<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/core/extensions.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Arquitectura de extensiones – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/core/extensions.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, extensions, lifecycle, integration
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Registro explícito de extensiones y devoluciones de llamada del ciclo de vida
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *El comportamiento de integración se registra deliberadamente; los paquetes no se inician por sí mismos.*

---

## 📌 Propósito

Este documento define cómo las aplicaciones agregan comportamiento coordinado sin modificar los componentes internos del framework.

## Contrato

Una extensión implementa `Extension::register(Application)` y `Extension::boot(Application)`. Las aplicaciones agregan una instancia de extensión o un nombre de clase a `ExtensionManager` antes de que finalice el arranque.

Durante el arranque de la aplicación, cada extensión se registra en orden de inserción después del enlace `register()` de la aplicación. A continuación se descubren las rutas, las extensiones se inician en el mismo orden y el enlace `boot()` de la aplicación se ejecuta al final.

Las extensiones indicadas por nombre de clase se resuelven mediante el contenedor de la aplicación. El administrador verifica que el objeto resuelto implemente `Extension`; los registros no válidos fallan. No existe descubrimiento automático de Composer, exploración implícita de paquetes ni un orden de arranque oculto.

Las extensiones coordinan los enlaces de servicios y la inicialización. El comportamiento por solicitud pertenece al middleware y el comportamiento de negocio pertenece a los servicios de la aplicación.

## 📚 Documentos relacionados

- [Ciclo de vida de la aplicación](application-lifecycle.md)
- [Inyección de dependencias](dependency-injection.md)
- [Middleware](../http/middleware.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
