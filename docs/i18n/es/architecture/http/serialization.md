<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/http/serialization.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# HTTP y serialización – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/http/serialization.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, http, serialization, content-negotiation
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Valores internos de solicitud y respuesta, selección de representación y puentes PSR
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *Los valores de transporte permanecen inmutables y las opciones de representación permanecen explícitas.*

---

## 📌 Propósito

Este documento define los objetos de valor HTTP de Bluewater y el comportamiento de serialización de respuestas.

## Valores de solicitud y respuesta

`Request` es una instantánea inmutable que contiene el método, la ruta, los encabezados, los valores de consulta, el cuerpo analizado o sin procesar, los valores del servidor y los atributos del framework. La búsqueda de encabezados no distingue entre mayúsculas y minúsculas. `withAttributes()` devuelve una solicitud nueva.

`Response` contiene de forma inmutable un estado, un mapa de encabezados y un cuerpo codificado. Las fábricas crean respuestas JSON, de texto sin formato, 204 y de problemas compatibles con RFC 7807. El adaptador FPM controla la emisión.

## Negociación de contenido

Un endpoint puede devolver una `Response` o un valor para serializar. Una respuesta pasa sin cambios. En caso contrario, primero se comprueban los serializadores personalizados de tipos de medios exactos, seguidos de JSON o comodín, XML, CSV y texto. JSON es la alternativa final.

Los objetos se normalizan mediante sus propiedades públicas. Las aplicaciones deben asegurarse de que esas propiedades no contengan secretos. XML y CSV solo aceptan valores de hoja compatibles con escalares. Los valores no compatibles generan excepciones y llegan al límite de errores de la aplicación.

El analizador actual de `Accept` conserva el orden del cliente y elimina los parámetros, pero no clasifica los intervalos de medios según valores de calidad.

## 📚 Documentos relacionados

- [Descripción general del sistema](../core/index.md)
- [Seguridad](../security/index.md)
- [OpenAPI](../api/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
