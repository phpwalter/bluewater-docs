# ❓ Frequently Asked Questions (FAQ) – Bluewater

📄 **File:** `docs/meta/faq.md`  
📅 **Status:** Stub  
🏷️ **Tags:** faq, help, answers, guidance  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – New Developers & Maintainers  
👨‍💻 **Author:** Bluewater Team

---

## 📘 OVERVIEW

Answers to the most common questions about Bluewater Framework, including usage, philosophy, technical design, and integration behavior. This doc aims to reduce issue volume and speed up onboarding.

---

## 🧪 Setup Issues

### 🔸 "Class not found" in autoload
> Run `composer dump-autoload` to rebuild PSR-4 class map.

---

### 🔸 Permissions on `cache/` directory
> Ensure the `cache/` directory is writable by the web server and CLI user.

---

### 🔸 Missing `.env` file
> Copy `.env.example` → `.env` and customize for your environment.

---

## 🔐 Authentication Questions

### 🔸 "Invalid token" on routes
> Check your middleware stack for missing JWT validator or expired tokens.

---

## 🛠️ CLI Tooling

### 🔸 "Command not found"
> Ensure `bin/bluewater` is symlinked to `vendor/bin/bluewater`.  
> Or run it directly from `vendor/bin`.

---

## 🧠 General

- Want to disable a module? Remove it from the service map or CLI bindings.
- Want to change routing structure? Use `routes/` per tenant.

---

✅ PRs welcome! Add your real-world tips to help other Bluewater devs.

---
