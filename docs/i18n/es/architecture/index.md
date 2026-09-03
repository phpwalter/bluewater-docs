<!-- locale-guard:language-bar:start -->
[<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../en/architecture/index.md) | **<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Arquitectura – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/index.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, index, bluewater-v8
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Subsistemas implementados y límites de sus responsabilidades
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *La arquitectura describe lo que el framework aplica actualmente.*

---

## 📌 Propósito

Este índice organiza la arquitectura implementada de Bluewater v8 y reemplaza los antiguos árboles de páginas duplicadas, provisionales y aspiracionales.

## Secciones de arquitectura

| Sección | Responsabilidad |
|---|---|
| [API](api/index.md) | Describe el contrato OpenAPI expuesto por las rutas y los esquemas implementados. |
| [Núcleo](core/index.md) | Selecciona, construye, inicia y amplía una aplicación aislada. |
| [Configuración](configuration/index.md) | Combina valores predeterminados protegidos con sobrescrituras de aplicación de tipos compatibles. |
| [Datos](data/index.md) | Proporciona operaciones PDO preparadas y gestión de transacciones sin un ORM. |
| [HTTP](http/index.md) | Enruta solicitudes, compone middleware, valida entradas, despacha manejadores y serializa respuestas. |
| [Entorno de ejecución](runtime/index.md) | Define el aislamiento de aplicaciones, la topología de despliegue y los controles de rendimiento. |
| [Seguridad](security/index.md) | Aplica límites de confianza, autenticación y comportamiento de cierre seguro. |
| [Pruebas](testing/index.md) | Verifica el comportamiento del framework y la integración de aplicaciones. |
| [Gobernanza](governance/index.md) | Mantiene terminología compartida y registros de decisiones de arquitectura. |

## Exclusiones deliberadas

Bluewater no implementa una malla de servicios, un dispositivo de puerta de enlace de API, un agente de mensajes, un plano de control de Kubernetes, un servidor de identidad centralizado, un ORM, un motor de migraciones ni una plataforma de trazabilidad distribuida. Esas capacidades corresponden a las aplicaciones o a la infraestructura externa.

## 📚 Documentos relacionados

- [Descripción general del sistema](core/index.md)
- [Ciclo de vida de la aplicación](core/application-lifecycle.md)
- [Guías técnicas](../technical/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../LICENSE).

---

*Última actualización: 2026-09-03*
