<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/testing/applications.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Pruebas de aplicaciones – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/testing/applications.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, testing, applications
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Pruebas de endpoints de aplicaciones y ejecución del host de referencia
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Las pruebas de aplicaciones ejercitan el comportamiento público de Bluewater sin modificar el paquete del framework.*

---

## 📌 Propósito

Esta guía explica las pruebas propiedad de la aplicación y la ejecución local del ejemplo incluido.

## Pruebas del código de la aplicación

Las pruebas de la aplicación deben cubrir el comportamiento de negocio independientemente del servidor web siempre que sea posible.

Debido a que el núcleo de Bluewater utiliza objetos `Request` y `Response` de Bluewater, los endpoints de la aplicación pueden ejercitarse sin ejecutar Apache ni FPM.

Como mínimo, pruebe:

- comportamiento correcto de los endpoints;
- entrada DTO no válida y respuestas HTTP 422;
- éxito y fallo de autenticación;
- comportamiento del middleware;
- enlaces de base de datos y servicios;
- comportamiento de rutas personalizadas;
- sobrescrituras importantes de configuración.

Para una prueba de integración completa del host, inicie la aplicación mediante `Bluewater\Host` y emita solicitudes de Bluewater directamente.

## Ejecución de la aplicación de ejemplo

El repositorio del framework incluye:

```text
examples/host/app/app_1
```

Utilícela como implementación de referencia para la estructura de aplicaciones y los patrones compatibles.

Demuestra:

- carga dinámica de espacios de nombres;
- `Bootstrap.php`;
- sobrescrituras de configuración;
- SQLite/PDO;
- endpoints basados en archivos;
- DTO de solicitudes;
- validación;
- todos los ámbitos de middleware;
- autenticación mediante clave de API;
- autenticación JWT;
- introspección de OAuth;
- extensiones de la aplicación;
- generación de OpenAPI.

## 📚 Documentos relacionados

- [Pruebas](index.md)
- [Uso](../usage/index.md)
- [Despliegue](../deployment/index.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
