<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/api/index.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Generación de OpenAPI – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/api/index.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, openapi, reflection, api-contract
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Derivación de OpenAPI 3.1 a partir de rutas descubiertas y tipos PHP reflejados
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *Los contratos generados deben seguir las rutas ejecutables, no un segundo manifiesto de rutas.*

---

## 📌 Propósito

Este documento describe la información de OpenAPI que Bluewater deriva y los límites del generador actual.

## Información generada

`OpenApiGenerator` lee la lista de rutas ya descubiertas por el enrutador. Deriva rutas, operaciones HTTP, parámetros de ruta y consulta, cuerpos de solicitud DTO, esquemas DTO reflejados, resúmenes proporcionados mediante `#[Summary]` y respuestas básicas 200 y 422. La generación no descubre rutas, no ejecuta endpoints, no realiza E/S de red ni escribe archivos.

La salida declara OpenAPI `3.1.0`. Para una lista de rutas y un código fuente reflejado fijos, la generación sigue un orden determinista de iteración de rutas y declaración de propiedades.

## Limitaciones actuales

El generador todavía no modela esquemas de seguridad, códigos de estado arbitrarios, encabezados, ejemplos, polimorfismo, tipos de unión de PHP, esquemas detallados de problemas, referencias externas ni negociación de versiones. La identidad del esquema usa el nombre corto de la clase DTO; prevalece la primera clase que tenga un nombre corto duplicado. Estas restricciones deben resolverse antes de considerar el documento generado como un contrato externo completo.

## 📚 Documentos relacionados

- [Enrutamiento y despacho](../http/routing-and-dispatch.md)
- [Validación](../http/validation.md)
- [HTTP y serialización](../http/serialization.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
