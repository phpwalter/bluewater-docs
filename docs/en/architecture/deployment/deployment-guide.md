# 🚀 Deployment Overview – Bluewater Framework

📄 **File:** `docs/deployment/deployment-guide.md`  
📅 **Status:** Published  
🏷️ **Tags:** deployment, hosting, production, devops  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – DevOps engineers, sysadmins, deployers  
👨‍💻 **Author:** Bluewater Team

---


This document outlines the supported deployment environments, setup checklist, and best practices for hosting Bluewater in production and staging environments.

---

## 🧾 Requirements

| Component            | Description                                |
|----------------------|--------------------------------------------|
| PHP Runtime          | PHP 8.2+ with FPM                          |
| Web Server           | NGINX (preferred) or Apache w/ mod_rewrite |
| Composer             | Required for initial install + autoloading |
| Writable Directories | `/cache/`, `/logs/`, and `/storage/`       |
| Environment Config   | `.env` file at project root                |

---

## 📁 Directory Structure Expectations

```txt
bluewater-project/
├── app/
├── public/             ← Web root
│   └── index.php
├── vendor/
├── .env
└── cache/              ← Must be writable
````

---

## 🌐 Web Server Setup

### 🔹 NGINX Example

```nginx
server {
    listen 80;
    server_name api.myapp.com;

    root /var/www/bluewater/public;

    index index.php;

    location / {
        try_files $uri $uri/ /index.php$is_args$args;
    }

    location ~ \.php$ {
        include fastcgi_params;
        fastcgi_pass unix:/run/php/php8.2-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
    }

    location ~ /\.env {
        deny all;
    }
}
```

---

### 🔹 Apache (Fallback)

Ensure `.htaccess` exists in `public/`:

```apache
<IfModule mod_rewrite.c>
    RewriteEngine On
    RewriteCond %{REQUEST_FILENAME} !-f
    RewriteRule ^ index.php [QSA,L]
</IfModule>
```

---

## 🛠️ Deployment Checklist

✅ Use `composer install --no-dev --optimize-autoloader`
✅ Run `bin/bluewater cache:clear` after deploy
✅ Verify `cache/` and `logs/` are writable
✅ Set environment variables or `.env` file
✅ Point web root to `/public/`, never to `/`
✅ Configure reverse proxy for TLS (e.g., nginx + Certbot)

---

## 📦 Docker & Containers

> Dockerfile, NGINX config, and runtime presets coming in `deployment/docker/`

---

## 🔒 Security Notes

* Use HTTPS with TLS 1.2+
* Do not expose `.env`, `/vendor/`, or `/app/` publicly
* Use JWT/OAuth middleware for all production APIs
* Consider rate-limiting, IP allowlists, or throttling

---

## 🧠 Deployment Philosophy

> "A good deployment is invisible. A bad one breaks everything."

Use Bluewater’s **stateless** structure for easy containerization and horizontal scaling.

---

## ⏩ Next: See [`release.md`](../architecture/release.md) for tagging and version packaging

```
