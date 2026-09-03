<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Responses and Content Negotiation – Bluewater Framework

📄 **File:** `docs/en/technical/usage/responses.md`
📅 **Status:** Active
🏷️ **Tags:** technical, usage, responses, serialization
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Response values, media types, and custom serializers
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Representation selection is explicit and keeps transport output immutable.*

---

## 📌 Purpose

This guide explains supported endpoint return values and negotiated response serialization.

## Returning responses

Endpoint handlers may return:

- `Bluewater\Http\Response`;
- arrays;
- DTOs/objects;
- scalars;
- collections.

Bluewater converts normal return values through the serializer registry.

Example:

```php
public function get(): array
{
    return ['status' => 'ok'];
}
```

For explicit responses:

```php
use Bluewater\Http\Response;

return Response::json(['created' => true], 201);
```

## Content negotiation

Bluewater uses request headers, especially `Accept`, to select a response serializer.

Built-in formats include:

```text
application/json
application/xml
text/csv
text/*
```

Application-specific serializers can be registered through Bluewater's serializer extension surface.

JSON should generally remain the default API format.

## 📚 Related Documents

- [Routing](routing.md)
- [OpenAPI](openapi.md)
- [Application testing](../testing/applications.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
