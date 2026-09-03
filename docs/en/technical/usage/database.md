<!-- locale-guard:language-bar:start -->
**<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English** | <img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español *(missing)* | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Database Access – Bluewater Framework

📄 **File:** `docs/en/technical/usage/database.md`
📅 **Status:** Active
🏷️ **Tags:** technical, usage, database, pdo
🔖 **Version:** 8.0.0
📅 **Date:** 2026-09-03
🌍 **Scope:** Prepared operations, transactions, and application repositories
🤝 **Contributors:** Bluewater framework maintainers
👨‍💻 **Author:** Bluewater Framework Team

---

> ### 🪶 **Bluewater Principle**
> *Persistence design belongs to applications behind a narrow replaceable contract.*

---

## 📌 Purpose

This guide explains Bluewater’s database interface, PDO implementation, and transaction callback.

## Database access

Bluewater core intentionally does not include an ORM.

It provides a small database contract and PDO-based implementation for:

- prepared statements;
- queries;
- transactions.

Applications may bind their own database abstraction or integrate an ORM through an explicit package/extension.

Typical application structure:

```text
Services/
├── UserRepository.php
└── DatabaseUserRepository.php
```

Application business logic should depend on repository/service interfaces rather than directly coupling every endpoint to PDO.

## 📚 Related Documents

- [Dependency injection](dependency-injection.md)
- [Application testing](../testing/applications.md)
- [Usage](index.md)

---

This published documentation is licensed under the [MIT License](../../../../LICENSE). Bluewater Framework source code is separately licensed under OSL-3.0.

---

*Last updated: 2026-09-03*
