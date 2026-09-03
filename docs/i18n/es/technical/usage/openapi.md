<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/usage/openapi.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# OpenAPI – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/usage/openapi.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, usage, openapi
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Generación de OpenAPI 3.1 a partir de rutas y tipos reflejados
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Las rutas ejecutables siguen siendo la fuente de las descripciones de API generadas.*

---

## 📌 Propósito

Esta guía explica el registro del generador OpenAPI, su salida, los metadatos y las limitaciones actuales.

## OpenAPI

Bluewater genera metadatos OpenAPI 3.1 a partir de las rutas descubiertas y los metadatos de la aplicación.

Las fuentes incluyen:

- rutas de endpoints;
- métodos HTTP;
- parámetros con tipos;
- definiciones de DTO;
- tipos de retorno;
- atributos opcionales de metadatos OpenAPI, como resúmenes.

La aplicación de ejemplo expone los metadatos generados en:

```text
GET /openapi
```

No mantenga un manifiesto de rutas independiente únicamente para OpenAPI.

## 📚 Documentos relacionados

- [Enrutamiento](routing.md)
- [Validación](validation.md)
- [Respuestas](responses.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
