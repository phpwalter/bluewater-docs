
### 📘 `docs/testing/testing.md` — Testing Strategy

# 🧪 Testing Strategy – Bluewater Framework

📄 **File:** `docs/testing/testing.md`  
🧮 **Status:** ✍️ Draft  
🛫 **ETA:** 2025-06-27  
🔖 **Version:** 0.1  
📅 **Date:** 2025-06-06  
🏷️ **Tags:** testing, quality, phpunit, automation  
🌍 **Scope:** Define how testing is designed, structured, and executed across the Bluewater PHP framework—including philosophy, tooling, CI integration, and code coverage targets.  
👥 **Contributors:** – QA team, developers, and CI maintainers  
👨‍💻 **Author:** Walter Torres

---

## 📘 Overview

This document provides a top-level overview of **testing philosophy, tooling, and coverage strategy** for the Bluewater PHP framework.  

Testing is fundamental to framework quality and enforced via local dev routines and CI/CD automation.

---

> ### 🪶 **Bluewater Principle**  
> *Tests must be as predictable, maintainable, and modular as the code they protect.*

---

## 🧪 Testing Layers

| Layer            | Purpose                                 | Tools       |
|------------------|-----------------------------------------|-------------|
| Unit             | Test isolated logic                     | PHPUnit     |
| Integration      | Validate multiple components in sync    | PHPUnit     |
| Functional       | Simulate framework behavior (CLI/API)   | PHPUnit     |
| End-to-End (opt) | Full lifecycle (optional, not included) | Cypress etc |

---

## 🛠️ Testing Tools

- ✅ [PHPUnit](https://phpunit.de/) – primary test runner  
- ✅ [Mockery](https://github.com/mockery/mockery) – mock object framework  
- 🔍 [Psalm](https://psalm.dev/) – optional static analysis  
- 🔄 [GitHub Actions](https://github.com/features/actions) – CI/CD runner (planned)  
- 📦 Composer-based test suite orchestration

---

## 📂 Directory Layout

```txt
/tests/
├── Unit/           # Class-by-class test coverage
├── Integration/    # Multi-service and I/O validation
├── Functional/     # Framework-level scenarios
├── Helpers/        # Custom test utilities
└── bootstrap.php   # Environment prep
````

---

## 🎯 Test Coverage Goals

| Target Layer   | Coverage Expectation |
| -------------- | -------------------- |
| Framework Core | 95–100%              |
| CLI Commands   | ≥90%                 |
| Middleware     | 100% for critical    |
| Router Layer   | 100% (all map paths) |
| Sample Tenant  | ≥80% recommended     |

---

## 🧬 Best Practices

* Group tests by layer and feature.
* Keep mocks lean and reflective of real contracts.
* Favor expressive test names: `testShouldRejectEmptyToken()` > `testInvalid()`.
* Ensure test isolation—no shared state between cases.

---

## 🔁 CI & Git Hooks (Planned)

* Add pre-commit hooks for running basic unit test sets.
* Deploy GitHub Actions for push-based test gates.
* Validate coverage thresholds as part of the pipeline.

---

## 📎 Related References

* [`unit-testing.md`](unit-testing.md) – Deeper dive into core logic testing
* [`mocking.md`](mocking.md) – Approaches for test isolation
* [`integration-testing.md`](integration-testing.md) – Sample contracts
* [PHPUnit Manual](https://phpunit.readthedocs.io/)
* [PSR-12 Coding Style](https://www.php-fig.org/psr/psr-12/)

---
