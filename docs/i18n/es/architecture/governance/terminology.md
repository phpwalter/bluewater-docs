<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/governance/terminology.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Terminología – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/governance/terminology.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, glossary, terminology
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Términos canónicos utilizados en toda la documentación de Bluewater
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *Un vocabulario compartido evita que los límites de arquitectura se vuelvan ambiguos.*

---

## 📌 Propósito

Este glosario define términos cuyo significado preciso es importante al mantener o integrar Bluewater v8.

## Términos

| Término | Significado |
|---|---|
| Aplicación | Una API de Bluewater aislada con su propia raíz, espacio de nombres, configuración, endpoints, caché, registros y contenedor. |
| Host | Fábrica que localiza, valida, construye e inicia aplicaciones con nombre. |
| Endpoint | Clase de aplicación descubierta a partir de un archivo de endpoint que contiene métodos manejadores HTTP. |
| Ruta | Asignación compilada e inmutable de un método HTTP y una ruta a un método de endpoint y una cadena de middleware. |
| Manejador | Método público de un endpoint cuyo nombre o atributos definen una operación HTTP. |
| Middleware de directorio | Middleware heredado de archivos `_middleware.php` a lo largo de la ruta de directorios de un endpoint. |
| DTO | Objeto de transferencia de datos de la aplicación hidratado a partir del cuerpo de una solicitud en forma de arreglo. |
| Extensión | Integración explícita de aplicación en dos fases que implementa devoluciones de llamada de registro y arranque. |
| Adaptador del entorno de ejecución | Límite que crea solicitudes de Bluewater y emite respuestas de Bluewater. |
| Identidad | Sujeto autenticado inmutable, declaraciones y ámbitos únicos normalizados. |
| Respuesta de problema | Respuesta JSON compatible con RFC 7807 utilizada para los límites de errores del framework. |
| Caché compilada | Representación PHP local de la aplicación para rutas o configuración validadas. |

## 📚 Documentos relacionados

- [Índice de arquitectura](../index.md)
- [Descripción general del sistema](../core/index.md)
- [Guía para desarrolladores de aplicaciones](../../technical/usage/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
