<!-- locale-guard:language-bar:start -->
[<img src="../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../en/about-bluewater.md) | **<img src="../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Acerca de Bluewater – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/about-bluewater.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** overview, goals, boundaries
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Propósito, capacidades y exclusiones deliberadas del framework
🤝 **Colaboradores:** Mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *El desarrollo habitual de API debe ser directo; el comportamiento excepcional debe permanecer explícito.*

---

## 📌 Propósito

Este documento presenta Bluewater Framework 8 y establece el límite entre el comportamiento implementado por el framework y las integraciones propiedad de la aplicación.

## Lo que proporciona Bluewater

- Descubrimiento de endpoints basado en convenciones sin un manifiesto de rutas.
- Aislamiento de configuración, caché, registros, espacio de nombres y endpoints por aplicación.
- Un contenedor PSR-11 con enlaces, instancias, fábricas y conexión automática explícitos.
- Ámbitos de middleware globales, de directorio, clase y método.
- Autenticación mediante clave de API, JWT HS256 y Bearer de OAuth inspeccionado por la aplicación.
- Hidratación de DTO y validación controlada por atributos.
- Serialización JSON, XML, CSV y de texto con negociación de contenido.
- Un contrato reducido de base de datos PDO sin un ORM integrado.
- Generación de OpenAPI 3.1 a partir de rutas descubiertas y tipos reflejados.
- Adaptadores de entorno de ejecución, con PHP-FPM como adaptador inicial.

## Responsabilidades de las aplicaciones

Las reglas de negocio, los esquemas persistentes, las migraciones, la política de autorización, la integración de identidades externas, las colas, las plataformas de caché, los sistemas de observabilidad y la infraestructura siguen siendo responsabilidad de las aplicaciones. Bluewater expone puntos de integración explícitos en lugar de seleccionar esas tecnologías silenciosamente.

## Objetivo de compatibilidad

Bluewater requiere PHP 8.3 o posterior. La integración continua está configurada para PHP 8.3 y PHP 8.4. Las API públicas `Bluewater\\...` constituyen la superficie de compatibilidad prevista; las futuras API `Bluewater\\Internal\\...` quedan excluidas de esa promesa.

## 📚 Documentos relacionados

- [Descripción general del sistema](architecture/core/index.md)
- [Índice de arquitectura](architecture/index.md)
- [Guía para desarrolladores de aplicaciones](technical/usage/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../LICENSE).

---

*Última actualización: 2026-09-03*
