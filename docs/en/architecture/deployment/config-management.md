🛠️ Stub creation complete! Below are the full documents for:

---

### 📄 `docs/deployment/config-management.md`

```markdown
# ⚙️ Config Management – Bluewater Framework

📄 **File:** `docs/deployment/config-management.md`  
📅 **Status:** Stub  
🏷️ **Tags:** configuration, env, deployment, psr-11  
🔖 **Version:** 1.0  
📦 **Scope:** 📦 Contributors – DevOps and backend configuration authors  
👨‍💻 **Author:** Bluewater Team

---

## 📌 Purpose

This document outlines how to manage configuration in Bluewater across environments (development, staging, production). It focuses on strategies that use environment variables, PHP arrays, and the Config module to load and merge settings.

---

## 📂 Configuration Sources

| Source         | Description                              |
|----------------|------------------------------------------|
| `.env` file    | Default environment values               |
| `app/*/config/`| Per-tenant config folders (scoped)       |
| `cache/`       | Merged config artifacts after build step |

---

## 🧩 Resolution Order

1. `.env`  
2. `app/common/config/*.php`  
3. `app/clientX/config/*.php`  
4. Runtime overrides or secrets

Values are merged in order, later files overriding earlier ones.

---

## 🔐 Sensitive Configuration

It is recommended to **exclude secrets from Git** and load them from:

- `.env` file (never commit to repo)
- Deployment secrets manager (e.g., AWS SSM, HashiCorp Vault)

---

## 📌 Best Practices

- Use one config file per domain (e.g., `database.php`, `auth.php`)
- Do not hardcode sensitive credentials
- Document required keys in `README.md` or a `/docs/env.example`

---

🧠 *Environment-aware, modular configuration keeps tenants safe and teams agile.*
