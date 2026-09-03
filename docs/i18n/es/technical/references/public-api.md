<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/references/public-api.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Referencia de la API pública – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/references/public-api.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, references, api
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Espacios de nombres compatibles y contratos principales de extensión
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Las aplicaciones dependen de contratos públicos documentados, no de detalles de implementación.*

---

## 📌 Propósito

Esta referencia identifica la superficie pública actual de los subsistemas de Bluewater v8.

## Subsistemas públicos

| Espacio de nombres | Tipos principales |
|---|---|
| `Bluewater` | `Host`, `Application`, `ApplicationBootstrap`, `ApplicationDefinition` |
| `Bluewater\Auth` | Proveedores de autenticación, middleware, administrador e `Identity` |
| `Bluewater\Config` | `Config`, `ConfigFactory` e `IniConfigParser` |
| `Bluewater\Container` | `Container` PSR-11 y excepciones de resolución |
| `Bluewater\Database` | `Database` y `PdoDatabase` |
| `Bluewater\Endpoint` | `Endpoint` y `EndpointDispatcher` |
| `Bluewater\Extension` | `Extension` y `ExtensionManager` |
| `Bluewater\Http` | `Request`, `Response` y `PsrBridge` inmutables |
| `Bluewater\Middleware` | `Middleware`, `Pipeline`, adaptadores, atributos y registro |
| `Bluewater\OpenApi` | `OpenApiGenerator` y `Summary` |
| `Bluewater\Routing` | `Router`, `Route`, `Path` y `RouteNotFound` |
| `Bluewater\Runtime` | `RuntimeAdapter` y `FpmAdapter` |
| `Bluewater\Serialization` | `SerializerRegistry` |
| `Bluewater\Validation` | Validador, atributos y `ValidationException` |

Los tipos futuros bajo `Bluewater\Internal\...` no forman parte del contrato de compatibilidad de versiones semánticas.

## 📚 Documentos relacionados

- [Arquitectura del núcleo](../development/architecture.md)
- [Uso](../usage/index.md)
- [Referencias técnicas](index.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
