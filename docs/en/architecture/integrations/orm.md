# 🧮 ORM Integration – Bluewater

📄 **File:** `docs/integrations/orm.md`  
📅 **Status:** Stub  
🏷️ **Tags:** integrations, orm, doctrine, eloquent  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – Backend Developers  
👨‍💻 **Author:** Bluewater Team

---

## Overview

Bluewater does not enforce a specific database abstraction. Developers are free to use raw PDO, lightweight query builders, or full-featured ORMs. This guide covers how to integrate common tools like Doctrine or Eloquent.

---

## 🧩 Recommended ORMs

| Tool                                     | Description                                 |
|------------------------------------------|---------------------------------------------|
| [Doctrine ORM](https://www.doctrine-project.org/projects/orm.html) | Enterprise-grade ORM with annotations, mapping, migrations |
| [Eloquent ORM](https://laravel.com/docs/eloquent) | Active Record ORM from Laravel, can be used standalone     |
| [Atlas ORM](https://atlasphp.io/)        | Data-mapper style, lightweight alternative  |
| Raw [PDO](https://www.php.net/manual/en/book.pdo.php) | Use native PHP DB access for simplicity     |

---

## 📦 Composer Packages

```bash
composer require doctrine/orm
composer require illuminate/database
````

---

## 🏗️ Usage Patterns

You may place DB logic in:

* `app/Models/` (recommended)
* `app/Services/` for abstraction layers
* Inject DB manager or ORM into middleware/controllers

---

## 🧪 Example (PDO)

```php
$pdo = new PDO("mysql:host=localhost;dbname=bluewater", "user", "pass");
$stmt = $pdo->prepare("SELECT * FROM users WHERE email = ?");
$stmt->execute([$email]);
$user = $stmt->fetch();
```

---

## ⚖️ Choosing Between ORM & PDO

| Feature        | PDO      | Doctrine / Eloquent |
| -------------- | -------- | ------------------- |
| Performance    | ✅ Fast   | ⚠️ Slight overhead  |
| Migrations     | ❌ Manual | ✅ Built-in tools    |
| Relationships  | ❌ Manual | ✅ Defined in model  |
| Learning Curve | Low      | Medium-High         |

---

## 🔐 Security Tips

* Always use parameterized queries
* Validate schema versions on deploys
* Never expose ORM debug output in production

---

## 🔗 Related

* [`docs/config/config.md`](../core/config.md)
* [Doctrine ORM Docs](https://www.doctrine-project.org/projects/orm.html)
* [Eloquent Standalone Guide](https://tinkerwell.app/docs/standalone-eloquent)

---
