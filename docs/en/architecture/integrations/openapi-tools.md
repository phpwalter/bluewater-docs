# 🧰 OpenAPI Tooling – Bluewater

📄 **File:** `docs/integrations/openapi-tools.md`  
📅 **Status:** Stub  
🏷️ **Tags:** integrations, openapi, docs, generators  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – Documentation & Dev Tooling  
👨‍💻 **Author:** Bluewater Team

---

## Overview

Bluewater supports OpenAPI v3 specification output for your REST APIs. This doc outlines tooling to generate, validate, serve, and visualize your API specs.

---

## 🎯 Goals

- 🧪 Ensure accurate, versioned documentation
- 🔄 Keep documentation synced with code
- 🌐 Enable client generation & API testing

---

## 🧰 Recommended Tools

| Tool                                                  | Description                                     |
|-------------------------------------------------------|-------------------------------------------------|
| [swagger-php](https://github.com/zircote/swagger-php) | Generate OpenAPI annotations from PHP docblocks |
| [redoc](https://github.com/Redocly/redoc)             | Static HTML visualizer for OpenAPI specs        |
| [swagger-ui](https://swagger.io/tools/swagger-ui/)    | Interactive browser-based UI                    |
| [Speccy](https://github.com/wework/speccy)            | Validate/spec-check OpenAPI YAML/JSON           |
| [Stoplight Studio](https://stoplight.io/studio/)      | Visual spec editing & mocking                   |

---

## 🔨 Workflow Example

1. Use `swagger-php` annotations in `Controllers/`
2. Run generator CLI to create `openapi.json` or `openapi.yaml`
3. Serve via route `/docs/api` or from static file

---

## 📦 Installation

```bash
composer require zircote/swagger-php
````

Generate docs:

```bash
./vendor/bin/openapi --output docs/api.json ./app/Controllers
```

---

## 🌐 Serve Interactive Docs (Optional)

Embed Swagger UI or Redoc in a static route:

```php
$app->get('/docs', function () {
    return new HtmlResponse(file_get_contents(__DIR__.'/../static/redoc.html'));
});
```

---

## 🔗 Related

* [`docs/openapi-spec.md`](../api/openapi-spec.md)
* [OpenAPI Spec v3](https://spec.openapis.org/oas/v3.0.3)
* [Swagger-PHP GitHub](https://github.com/zircote/swagger-php)

---

```
