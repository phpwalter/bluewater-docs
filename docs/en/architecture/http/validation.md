<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | [<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español](../../../i18n/es/architecture/http/validation.md) | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Validation Architecture – Bluewater Framework

📄 **File:** `docs/en/architecture/http/validation.md`
📅 **Status:** Published
🏷️ **Tags:** architecture, validation, dto, attributes
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** DTO hydration, validation attributes, errors, and limitations
🤝 **Contributors:** Framework architects and maintainers
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Validation rejects malformed application input before domain work begins.*

---

## 📌 Purpose

This document describes how endpoint request bodies become DTOs and how validation failures are represented.

## Hydration

An array request body may hydrate a class whose namespace contains `\DTO\`. Constructor parameters are populated by matching string keys. Unknown keys are ignored. Missing constructor parameters without defaults produce field errors before construction.

## Built-in constraints

- `#[Required]` rejects absent, null, blank-string, and empty-array values.
- `#[Email]` validates a non-empty value as an email address.
- `#[MinLength(n)]` enforces the configured minimum character length.

Validation is enabled by the `features.VALIDATION` configuration value. A `ValidationException` contains a stable field-to-message-list map. During endpoint dispatch it becomes HTTP 422 JSON with `error: validation_failed` and `fields`.

## Boundary

DTO validation is input-contract validation. It does not authenticate callers, authorize actions, validate cross-record business policy, or persist values. Domain invariants must still be enforced by application services.

## 📚 Related Documents

- [Routing and dispatch](routing-and-dispatch.md)
- [Security](../security/index.md)
- [Application developer guide](../../technical/usage/index.md)

---

This documentation is licensed under the [MIT License](../../../../LICENSE).

---

*Last updated: 2026-09-03*
