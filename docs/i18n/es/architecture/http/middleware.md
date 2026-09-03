<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/http/middleware.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Arquitectura de middleware – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/http/middleware.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, middleware, psr-15
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Ámbitos, orden, resolución e interoperabilidad del middleware
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *La política de solicitudes pertenece a una canalización ordenada, no a la lógica de negocio del endpoint.*

---

## 📌 Propósito

Este documento define el contrato de middleware síncrono de Bluewater y su orden efectivo de ejecución.

## Ámbitos efectivos

El middleware se compone en el siguiente orden:

1. Middleware global de la aplicación agregado durante el arranque.
2. Middleware de directorio heredado de archivos `_middleware.php`.
3. Atributos repetibles `#[UseMiddleware]` de la clase de endpoint.
4. Atributos repetibles `#[UseMiddleware]` del método de endpoint.

La primera entrada es el middleware más externo y recibe primero la solicitud. Cada middleware debe devolver una `Response` de Bluewater o delegar al siguiente invocable proporcionado.

## Resolución

Las instancias de middleware pueden registrarse directamente. Las entradas con cadenas de clase se resuelven mediante el contenedor de la aplicación para cada solicitud manejada. La canalización no captura los fallos de resolución ni las excepciones del middleware; la aplicación los convierte en una respuesta de problema 500.

## Límite PSR-15

`Psr15Adapter` convierte una solicitud de Bluewater a PSR-7, invoca un manejador PSR-15 y vuelve a convertir la respuesta PSR. Esto proporciona interoperabilidad sin convertir los tipos PSR en la API habitual orientada a la aplicación.

## 📚 Documentos relacionados

- [Enrutamiento y despacho](routing-and-dispatch.md)
- [Inyección de dependencias](../core/dependency-injection.md)
- [Autenticación](../security/authentication.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
