### 📄 `/docs/index.md`

📅 **Last Updated:** {{DATE}}
🔖 **Version:** 1.0
📦 **Scope:** 📚 Global Documentation Index for Bluewater
🏷️ **Tags:** index, toc, navigation, structure

---

# 🌊 Bluewater Framework — Architecture Documentation Index

Welcome to the **official Bluewater Docs Hub**.
This index links to all internal framework documentation grouped by domain and feature. Use this to navigate across architecture, APIs, security, integration, and contributor guides.

---

## 🧠 Architecture & Design

* [`architecture.md`](./architecture/system-overview.md) – Design principles and layout
* [`multi-tenant.md`](architecture/multi-tenant.md) – Per-client directory strategy
* [`structure.md`](architecture/structure.md) – File layout and modular boundaries
* [`specifications.md`](architecture/specifications.md) – Feature and technical specs
* [`release.md`](architecture/release.md) – Versioning and lifecycle
* [`roadmap.md`](architecture/roadmap.md) – Timeline and progress tracking

---

## 📦 Core Modules

* [`core-modules.md`](core/core-modules.md) – High-level overview of framework components
* [`router.md`](core/router.md) – Route resolution and matching
* [`dispatcher.md`](core/dispatcher.md) – Middleware dispatcher engine
* [`responder.md`](core/responder.md) – JSON response handler
* [`middleware.md`](core/middleware.md) – Global and client-specific middleware
* [`logger.md`](core/logger.md) – PSR-3 logging abstraction
* [`config.md`](core/config.md) – Config loader and runtime environment

---

## 🛠️ CLI & Developer Tooling

* [`cli-tooling.md`](cli/cli-tooling.md) – Available CLI commands
* [`docs-guides.md`](guides/docs-guides.md) – Internal contributor help and examples

---

## 📡 API

* [`openapi.md`](api/openapi.md) – OpenAPI integration setup
* [`openapi-spec.md`](api/openapi-spec.md) – Sample schema and docs
* [`rate-limiting.md`](api/rate-limiting.md) – Endpoint rate limiting strategies
* [`spec-format.md`](api/spec-format.md) – JSON and error formatting
* [`versioning.md`](api/versioning.md) – API lifecycle and versioning support

---

## 🔐 Security

* [`auth-modules.md`](security/auth-modules.md) – Supported authentication systems
* [`jwt.md`](security/jwt.md) – JSON Web Tokens
* [`oauth.md`](security/oauth.md) – OAuth 2.0 plugin design
* [`nextgen.md`](security/nextgen.md) – Future security models (mTLS, key rotation)

---

## 🧪 Testing & Quality

* [`testing.md`](testing/testing.md) – Overview of test architecture
* [`unit-testing.md`](testing/unit-testing.md) – Test logic in isolation
* [`integration-testing.md`](testing/integration-testing.md) – Full-stack functional tests
* [`mocking.md`](testing/mocking.md) – Mocking patterns and utilities

---

## 🚀 Deployment

* [`deployment.md`](deployment/deployment-guide.md) – Hosting requirements and strategy
* [`build-process.md`](deployment/build-process.md) – Building and packaging
* [`config-management.md`](deployment/config-management.md) – Config formats and merging
* [`environments.md`](deployment/environments.md) – `.env` usage and environment switching

---

## 🔌 Integrations

* [`auth.md`](integrations/auth.md)
* [`cache.md`](integrations/cache.md)
* [`monitoring.md`](integrations/monitoring.md)
* [`queues.md`](integrations/queues.md)
* [`cdn.md`](integrations/cdn.md)
* [`emails.md`](integrations/emails.md)
* [`file-storage.md`](integrations/file-storage.md)
* [`notifications.md`](integrations/notifications.md)
* [`openapi-tools.md`](integrations/openapi-tools.md)
* [`orm.md`](integrations/orm.md)
* [`payment.md`](integrations/payment.md)
* [`rate-limit.md`](integrations/rate-limit.md)
* [`search.md`](integrations/search.md)
* [`tracing.md`](integrations/tracing.md)
* [`webhooks.md`](integrations/webhooks.md)

---

## 📘 Guides & Help

* [`getting-started.md`](guides/getting-started.md)
* [`project-layout.md`](guides/project-layout.md)
* [`usage-examples.md`](guides/usage-examples.md)
* [`faq.md`](meta/faq.md)
* [`troubleshooting.md`](meta/troubleshooting.md)
* [`upgrading.md`](meta/upgrading.md)
* [`extending.md`](meta/extending.md)

---

## 🧾 Metadata & Site

* [`_toc.md`](./meta/_toc.md)
* [`index.md`](./meta/index.md) ← You are here
* [`license.md`](./meta/license.md)
* [`CONTRIBUTING.md`](../CONTRIBUTING.md)

---

📘 *This index is generated and manually maintained. For additions, update `_toc.md` or the docs builder.*
Want this as a GitHub Pages view? Visit:
🌐 [`https://bluewatermvc.github.io/bluewater-docs`](https://bluewatermvc.github.io/bluewater-docs)

---
