<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/usage/responses.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Respuestas y negociación de contenido – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/usage/responses.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, usage, responses, serialization
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Valores de respuesta, tipos de medios y serializadores personalizados
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *La selección de representación es explícita y mantiene inmutable la salida de transporte.*

---

## 📌 Propósito

Esta guía explica los valores de retorno compatibles de los endpoints y la serialización negociada de respuestas.

## Devolución de respuestas

Los manejadores de endpoints pueden devolver:

- `Bluewater\Http\Response`;
- arreglos;
- DTO u objetos;
- escalares;
- colecciones.

Bluewater convierte los valores de retorno normales mediante el registro de serializadores.

Ejemplo:

```php
public function get(): array
{
    return ['status' => 'ok'];
}
```

Para respuestas explícitas:

```php
use Bluewater\Http\Response;

return Response::json(['created' => true], 201);
```

## Negociación de contenido

Bluewater utiliza los encabezados de la solicitud, especialmente `Accept`, para seleccionar un serializador de respuestas.

Los formatos integrados incluyen:

```text
application/json
application/xml
text/csv
text/*
```

Los serializadores específicos de la aplicación pueden registrarse mediante la superficie de extensión de serializadores de Bluewater.

JSON normalmente debe seguir siendo el formato predeterminado de la API.

## 📚 Documentos relacionados

- [Enrutamiento](routing.md)
- [OpenAPI](openapi.md)
- [Pruebas de aplicaciones](../testing/applications.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
