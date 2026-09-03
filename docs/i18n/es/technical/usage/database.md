<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/usage/database.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Acceso a bases de datos – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/usage/database.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, usage, database, pdo
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Operaciones preparadas, transacciones y repositorios de aplicaciones
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *El diseño de persistencia pertenece a las aplicaciones detrás de un contrato reducido y reemplazable.*

---

## 📌 Propósito

Esta guía explica la interfaz de base de datos de Bluewater, la implementación PDO y la devolución de llamada de transacciones.

## Acceso a bases de datos

El núcleo de Bluewater no incluye deliberadamente un ORM.

Proporciona un contrato reducido de base de datos y una implementación basada en PDO para:

- sentencias preparadas;
- consultas;
- transacciones.

Las aplicaciones pueden enlazar su propia abstracción de base de datos o integrar un ORM mediante un paquete o extensión explícitos.

Estructura típica de la aplicación:

```text
Services/
├── UserRepository.php
└── DatabaseUserRepository.php
```

La lógica de negocio de la aplicación debe depender de interfaces de repositorios o servicios, en lugar de acoplar directamente cada endpoint a PDO.

## 📚 Documentos relacionados

- [Inyección de dependencias](dependency-injection.md)
- [Pruebas de aplicaciones](../testing/applications.md)
- [Uso](index.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
