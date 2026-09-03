Here is a formal Markdown file you can include in your contributor documentation or knowledge base:

---

### 📘 `docs/contribute/types-of-docs.md` — Document Types Overview

# 📚 Document Types – Bluewater Framework

📄 **File:** `docs/contribute/types-of-docs.md`
🧮 **Status:** ✍️ Draft
🛫 **ETA:** 2025-06-27
🔖 **Version:** 0.1
📅 **Date:** 2025-06-06
🏷️ **Tags:** documentation, architecture, technical-writing
🌍 **Scope:** Clarifies the distinctions between architectural and technical documents for contributors and maintainers.
👥 **Contributors:** – Technical Writers, Project Maintainers
👨‍💻 **Author:** Walter Torres

<!--  
🧮 STATUS OPTIONS (choose only one):  
  - 🚧 Stub / Placeholder  
  - 📝 In Review  
  - ⏳ Planned  
  - 🔐 Internal Only  
  - ✍️ Draft  
  - ✅ Approved  
  - 📘 Final  
  - ⚠️ Deprecated  
  - ♻️ Needs Update  
  - 🗑️ Obsolete  
-->

---

## 🧭 Overview

This guide defines and distinguishes the two major document types used in Bluewater documentation: **Architectural Documents** and **Full Technical Documents**. Understanding the correct use case and format for each ensures consistency and usability across the project.

---

## 🧱 Document Types

| Type                 | Purpose                                                       | Audience                    |
|----------------------|---------------------------------------------------------------|-----------------------------|
| 🧠 **Architectural** | High-level system structure, design intent, and flow          | Architects, Leads, DevOps   |
| 🛠️ **Technical**    | Detailed implementation, usage, configuration, and interfaces | Developers, Maintainers, QA |

---

### 🧠 Architectural Documents

**Architectural docs** provide a **macro-level view** of how system parts interact, including:

* Component interaction and responsibilities
* Design rationale and constraints
* Diagrams of deployment, flow, and topology
* Choices affecting performance, scale, and maintainability

**Examples:**

* `docs/architecture/system-overview.md`
* `docs/architecture/lifecycle.md`

---

### 🛠 Full Technical Documents

**Technical documents** dive into **implementation details** of a module, class, or service:

* Code structure, inputs/outputs
* Config settings, environment variables
* Error handling, test strategy
* Sample usage or integration patterns

**Examples:**

* `docs/configuration/runtime.md`
* `docs/core/config-class.md` (planned)

---

## 🔁 When to Use Which

| Scenario                                | Use Architectural Doc | Use Technical Doc |
|-----------------------------------------|-----------------------|-------------------|
| Describe inter-service communication    | ✅ Yes                 | ⛔ No              |
| Document class methods or config values | ⛔ No                  | ✅ Yes             |
| Justify using pub/sub architecture      | ✅ Yes                 | ⛔ No              |
| Explain how to implement a new driver   | ⛔ No                  | ✅ Yes             |
| Lay out tenant isolation design         | ✅ Yes                 | ⛔ No              |
| Describe log formats and levels         | ⛔ No                  | ✅ Yes             |

---

## 🧭 Next Steps

* Use [header-template.md](header-template.md) for all new documents.
* Reference this file when creating new document types or assigning contributor tasks.

---
