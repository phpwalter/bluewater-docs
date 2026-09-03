### 🚀 `docs/guides/getting-started.md`

# 🚀 Getting Started – Bluewater Framework

📄 **File:** `docs/guides/getting-started.md`  
📅 **Status:** Stub  
🏷️ **Tags:** setup, installation, cli, first steps  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – New developers and adopters  
👨‍💻 **Author:** Bluewater Team

---

## 📌 Purpose

This guide will walk you through installing and launching your first **Bluewater** project — from initial Composer setup to serving your first API response.

---

## 🧰 Prerequisites

| Requirement | Minimum Version                |
|-------------|--------------------------------|
| PHP         | 8.2                            |
| Composer    | 2.x                            |
| Web Server  | NGINX / Apache                 |
| OS          | Linux / Mac / WSL2 recommended |

---

## 📦 Installation

```bash
composer create-project bluewater/framework my-api
cd my-api
cp .env.example .env
````

Customize your `.env` file as needed.

---

## 🌐 Run the API Server

For quick local testing:

```bash
php -S localhost:8000 -t public
```

Then open:
📡 [http://localhost:8000/ping](http://localhost:8000/ping)

You should receive a default JSON response from the example `PingController`.

---

## 🧠 Directory Overview

```txt
my-api/
├── app/              # Your API logic (controllers, config, etc.)
├── public/           # Entry point (index.php)
├── bin/              # CLI tools
├── cache/            # Writable cache/runtime directory
├── vendor/           # Composer dependencies
├── .env              # Environment config
└── README.md
```

---

## 🔧 First Custom Route (Example)

Edit: `app/Controllers/HelloController.php`

```php
<?php

namespace App\Controllers;

class HelloController {
  public function index() {
    return ['message' => 'Hello, Bluewater!'];
  }
}
```

Define the route in `routes/api.php`:

```php
$router->get('/hello', [HelloController::class, 'index']);
```

Now visit:
📡 [http://localhost:8000/hello](http://localhost:8000/hello)

---

## 📘 What’s Next?

* Explore the CLI: `bin/bluewater route:list`
* Review your `app/config/` settings
* Check `/docs/guides/project-layout.md`
* Review `/docs/core/` to understand the internals

---

🧠 *Bluewater is designed to be lightweight and intuitive. If you can write functions, you can build scalable APIs.*
