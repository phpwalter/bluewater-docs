<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/http/index.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# HTTP – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/http/index.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, http, bluewater-v8
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Procesamiento de solicitudes y serialización de respuestas
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *El comportamiento HTTP permanece explícito desde la coincidencia de ruta hasta la emisión de la respuesta.*

---

## 📌 Propósito

Esta sección describe la canalización HTTP implementada por Bluewater y sus límites de validación.

## Contenido de la sección

| Documento | Cobertura |
|---|---|
| [Enrutamiento y despacho](routing-and-dispatch.md) | Descubrimiento y coincidencia de rutas, enlace de argumentos e invocación de manejadores. |
| [Middleware](middleware.md) | Composición de middleware global y de ruta. |
| [Serialización](serialization.md) | Solicitudes PSR-7, normalización de respuestas y serialización JSON. |
| [Validación](validation.md) | Validación de DTO de solicitud y respuestas de fallo. |

## 📚 Documentos relacionados

- [Índice de arquitectura](../index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
