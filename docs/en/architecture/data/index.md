<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Data Access – Bluewater Framework

📄 **File:** `docs/en/architecture/data/index.md`
📅 **Status:** Published
🏷️ **Tags:** architecture, database, pdo, transactions
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Database contract, prepared operations, and transaction boundary
🤝 **Contributors:** Framework architects and maintainers
👨‍💻 **Author:** Bluewater Documentation Team

---

> ### 🪶 **Bluewater Principle**
> *The framework supplies a narrow data boundary and leaves persistence design to the application.*

---

## 📌 Purpose

This document defines the implemented database abstraction and its deliberate exclusions.

## Database contract

`Database` exposes `fetchOne()`, `fetchAll()`, `execute()`, and `transaction()`. `PdoDatabase` implements that contract with prepared statements and bound parameters. `connect()` creates a PDO connection with exception error mode, associative fetches, and native prepared statements unless callers explicitly override those options.

`fetchOne()` returns one associative row or `null`; `fetchAll()` returns a list of associative rows; `execute()` returns the affected-row count.

## Transactions

`transaction()` begins a transaction, invokes the callback once, commits on success, and rolls back when the callback throws while the connection remains in a transaction. The original exception is rethrown. Nested transaction semantics are not provided.

## Deliberate exclusions

Bluewater has no ORM, schema migration tool, query builder, repository generator, connection pool, read replica router, or tenant filter. Applications may bind another `Database` implementation or integrate an external persistence package.

## 📚 Related Documents

- [Dependency injection](../core/dependency-injection.md)
- [Application isolation](../runtime/application-isolation.md)
- [Security](../security/index.md)

---

This documentation is licensed under the [MIT License](../../../../LICENSE).

---

*Last updated: 2026-09-03*
