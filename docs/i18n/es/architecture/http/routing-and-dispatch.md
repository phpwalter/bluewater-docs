<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/http/routing-and-dispatch.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Enrutamiento y despacho – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/http/routing-and-dispatch.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, routing, endpoints, dispatch
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Descubrimiento de endpoints, compilación y coincidencia de rutas y enlace de argumentos
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *Las rutas comunes son convenciones; las rutas excepcionales son declaraciones.*

---

## 📌 Propósito

Este documento define cómo los archivos de endpoint se convierten en rutas y cómo las rutas coincidentes invocan el código de la aplicación.

## Descubrimiento de rutas

Los archivos PHP de endpoints se recorren en orden léxico. Los métodos públicos no estáticos declarados por la clase de endpoint se consideran manejadores cuando sus nombres comienzan con un verbo HTTP compatible. Un archivo llamado `Endpoints/users.php` con `get()` y `getById(int $id)` produce `GET /users` y `GET /users/{id}`.

`#[Path]` agrega una ruta explícita cuando la convención de nombres no es suficiente. Los nombres de los marcadores deben coincidir con los parámetros del manejador. Las rutas canónicamente equivalentes, como `/users/{id}` y `/users/{name}`, entran en conflicto para el mismo verbo y hacen fallar el descubrimiento.

## Precedencia determinista y almacenamiento en caché

Las rutas estáticas se ordenan antes que las dinámicas; las rutas más largas se ordenan antes que las más cortas cuando tienen la misma cantidad de segmentos dinámicos. Los archivos de endpoint y los `_middleware.php` heredados contribuyen a la huella digital de la caché de rutas. Una caché coincidente se carga directamente; las rutas obsoletas se reconstruyen y escriben de forma atómica.

## Enlace de parámetros

El despachador resuelve los parámetros del manejador en este orden:

1. Inyección de `Request` de Bluewater.
2. Parámetros de ruta capturados.
3. Valores de la cadena de consulta.
4. Hidratación del DTO de la aplicación desde un cuerpo de solicitud en forma de arreglo.
5. Servicios del contenedor.
6. Valores predeterminados declarados.

Las conversiones escalares compatibles fallan cuando un valor no puede representarse como el tipo entero, flotante, booleano o cadena declarado. Los fallos de validación de DTO devuelven HTTP 422. Otros fallos de enlace o del manejador llegan al límite de errores de la aplicación.

## 📚 Documentos relacionados

- [Middleware](middleware.md)
- [Inyección de dependencias](../core/dependency-injection.md)
- [Validación](validation.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
