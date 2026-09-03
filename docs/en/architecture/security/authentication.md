<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Authentication Architecture – Bluewater Framework

📄 **File:** `docs/en/architecture/security/authentication.md`
📅 **Status:** Published
🏷️ **Tags:** architecture, authentication, api-key, jwt, oauth
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Credential-provider selection, validation, identity mapping, and denial
🤝 **Contributors:** Framework architects and maintainers
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *Authentication chooses one configured verifier and fails closed.*

---

## 📌 Purpose

This document describes Bluewater’s authentication providers and distinguishes authentication from authorization.

## Provider selection

`AuthManager` stores providers under trimmed lowercase strategy names. Duplicate names fail registration. Authentication selects exactly one named provider; it never tries a default or fallback provider. Unknown strategies raise an exception, while expected credential denial returns `null`.

## Built-in providers

| Provider | Enforced checks |
|---|---|
| API key | Configured header, non-empty key, constant-time comparison, configured identity mapping. |
| JWT | Bearer syntax, compact structure, base64url and JSON validity, exact HS256 algorithm, HMAC signature, required `exp` and `sub`, optional `nbf`, and configured issuer/audience. |
| OAuth bearer | Bearer syntax and an application-supplied introspector returning literal `active=true` plus non-blank `sub` or `client_id`. |

API keys and raw bearer tokens are not copied into the resulting `Identity`. Provider classes authenticate; they do not decide whether the identity may perform a domain action. Authorization belongs in application middleware or services.

## Current JWT boundary

The built-in JWT provider supports only shared-secret HS256. Public-key algorithms, JWKS retrieval, key rotation, replay stores, refresh tokens, and token issuance are not implemented by this provider.

## 📚 Related Documents

- [Security](index.md)
- [Middleware](../http/middleware.md)
- [Application developer guide](../../technical/usage/index.md)

---

This documentation is licensed under the [MIT License](../../../../LICENSE).

---

*Last updated: 2026-09-03*
