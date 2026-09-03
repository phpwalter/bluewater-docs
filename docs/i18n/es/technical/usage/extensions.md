<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/usage/extensions.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Extensiones de aplicaciones – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/usage/extensions.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, usage, extensions
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Registro explícito y ciclo de vida de extensiones en dos fases
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Los paquetes se integran mediante enlaces declarados del ciclo de vida en lugar de un descubrimiento oculto.*

---

## 📌 Propósito

Esta guía explica cómo las integraciones coordinadas de aplicaciones registran servicios y el comportamiento de arranque.

## Extensiones

Las capacidades reutilizables de las aplicaciones pueden empaquetarse como paquetes de Composer y registrarse explícitamente.

Una extensión de Bluewater implementa:

```text
Bluewater\Extension\Extension
```

Las extensiones pueden registrar servicios como:

- servicios;
- middleware;
- serializadores;
- validadores;
- proveedores de autenticación;
- componentes OpenAPI;
- controladores de bases de datos.

El registro de extensiones es explícito. Bluewater no utiliza el descubrimiento automático oculto de paquetes de Composer.

Las extensiones reutilizables normales no deben agregar endpoints de aplicación silenciosamente.

## 📚 Documentos relacionados

- [Uso](index.md)
- [Middleware](middleware.md)
- [Arquitectura del núcleo](../development/architecture.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
