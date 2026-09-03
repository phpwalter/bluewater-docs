<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# DTOs and Validation – Bluewater Framework

📄 **File:** `docs/en/technical/usage/validation.md`
📅 **Status:** Active
🏷️ **Tags:** technical, usage, dto, validation
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Request DTO hydration and attribute validation
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Malformed input is rejected before application services execute.*

---

## 📌 Purpose

This guide explains DTO construction, built-in validation attributes, and HTTP 422 responses.

## DTOs and validation

Use typed DTOs for request data when practical.

Example:

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

Then use the DTO directly in the endpoint:

```php
public function post(
    CreateUserRequest $request,
    UserRepository $users,
): UserDto {
    return $users->create($request);
}
```

Bluewater hydrates and validates the DTO automatically.

Validation failures return HTTP 422 with field-level errors.

## 📚 Related Documents

- [Dependency injection](dependency-injection.md)
- [Responses](responses.md)
- [Application testing](../testing/applications.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
