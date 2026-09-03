<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/usage/validation.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# DTO y validación – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/usage/validation.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, usage, dto, validation
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Hidratación de DTO de solicitudes y validación mediante atributos
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *La entrada mal formada se rechaza antes de que se ejecuten los servicios de la aplicación.*

---

## 📌 Propósito

Esta guía explica la construcción de DTO, los atributos de validación integrados y las respuestas HTTP 422.

## DTO y validación

Utilice DTO con tipos para los datos de las solicitudes cuando sea posible.

Ejemplo:

```php
namespace Apps\App1\DTO;

use Bluewater\Validation\Email;
use Bluewater\Validation\MinLength;
use Bluewater\Validation\Required;

final readonly class CreateUserRequest
{
    public function __construct(
        #[Required, Email]
        public string $email,

        #[Required, MinLength(2)]
        public string $name,
    ) {}
}
```

A continuación, utilice el DTO directamente en el endpoint:

```php
public function post(
    CreateUserRequest $request,
    UserRepository $users,
): UserDto {
    return $users->create($request);
}
```

Bluewater hidrata y valida el DTO automáticamente.

Los fallos de validación devuelven HTTP 422 con errores en el nivel de campo.

## 📚 Documentos relacionados

- [Inyección de dependencias](dependency-injection.md)
- [Respuestas](responses.md)
- [Pruebas de aplicaciones](../testing/applications.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
