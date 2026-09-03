<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/configuration/index.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Arquitectura de configuración – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/configuration/index.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, configuration, cache, validation
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Valores predeterminados del framework, sobrescrituras de aplicación, referencias y caché compilada
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *La herencia de configuración solo se permite cuando los tipos y la propiedad permanecen intactos.*

---

## 📌 Propósito

Este documento define cómo Bluewater construye una vista de configuración inmutable para una aplicación.

## Fuentes y precedencia

Los archivos `*.ini.php` y `*.session.php` propiedad del framework se cargan primero en orden léxico. Sus equivalentes propiedad de la aplicación se cargan después y sobrescriben recursivamente los valores coincidentes. Cuando faltan archivos de aplicación, se heredan los valores predeterminados del framework.

Las sobrescrituras de la aplicación deben conservar el tipo de hoja existente. `BW_VER` está bloqueado y una aplicación no puede agregarlo ni modificarlo. Los archivos de configuración son archivos PHP protegidos; su protección rechaza la carga directa fuera del contexto de arranque definido por Bluewater.

## Resolución de referencias

Los marcadores como `{APP_ROOT}`, `{CACHE_ROOT}`, `{BLUEWATER}`, `{SITE_ROOT}` y `{DS}` se resuelven después de la combinación. Las claves aplanadas exactas tienen precedencia. Una referencia por nombre de hoja solo se acepta cuando es única. Las referencias desconocidas, ambiguas y circulares fallan en lugar de usar silenciosamente un valor alternativo.

## Caché compilada

La lista ordenada de fuentes y el estado de los archivos producen una huella digital. Una caché vigente se carga como PHP. Una configuración obsoleta se analiza y valida por completo antes de que un cambio de nombre atómico reemplace `cache/config.php`; si la validación falla, la caché anterior permanece intacta.

## 📚 Documentos relacionados

- [Aislamiento de aplicaciones](../runtime/application-isolation.md)
- [Seguridad](../security/index.md)
- [Guía para desarrolladores de aplicaciones](../../technical/usage/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
