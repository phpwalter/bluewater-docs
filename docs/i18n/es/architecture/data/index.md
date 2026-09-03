<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/data/index.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Acceso a datos – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/data/index.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, database, pdo, transactions
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Contrato de base de datos, operaciones preparadas y límite de transacciones
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *El framework proporciona un límite de datos reducido y deja el diseño de persistencia a la aplicación.*

---

## 📌 Propósito

Este documento define la abstracción de base de datos implementada y sus exclusiones deliberadas.

## Contrato de base de datos

`Database` expone `fetchOne()`, `fetchAll()`, `execute()` y `transaction()`. `PdoDatabase` implementa ese contrato con sentencias preparadas y parámetros enlazados. `connect()` crea una conexión PDO con modo de error por excepciones, obtención asociativa y sentencias preparadas nativas, salvo que los llamadores sobrescriban expresamente esas opciones.

`fetchOne()` devuelve una fila asociativa o `null`; `fetchAll()` devuelve una lista de filas asociativas; `execute()` devuelve la cantidad de filas afectadas.

## Transacciones

`transaction()` inicia una transacción, invoca la devolución de llamada una vez, confirma cuando tiene éxito y revierte cuando la devolución genera una excepción mientras la conexión permanece en una transacción. La excepción original vuelve a propagarse. No se proporciona semántica para transacciones anidadas.

## Exclusiones deliberadas

Bluewater no incluye ORM, herramienta de migración de esquemas, generador de consultas, generador de repositorios, grupo de conexiones, enrutador de réplicas de lectura ni filtro de inquilinos. Las aplicaciones pueden enlazar otra implementación de `Database` o integrar un paquete de persistencia externo.

## 📚 Documentos relacionados

- [Inyección de dependencias](../core/dependency-injection.md)
- [Aislamiento de aplicaciones](../runtime/application-isolation.md)
- [Seguridad](../security/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
