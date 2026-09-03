<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/core/dependency-injection.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Inyección de dependencias – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/core/dependency-injection.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, container, psr-11, services
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Registro y resolución de servicios, conexión automática y comportamiento ante fallos
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *Las dependencias son explícitas incluso cuando su construcción es automática.*

---

## 📌 Propósito

Este documento describe el contenedor PSR-11 que utiliza cada aplicación Bluewater.

## Formas de registro

El contenedor acepta instancias de objetos retenidas, enlaces de interfaz a clase, fábricas invocables y conexión automática de clases concretas. Un registro duplicado reemplaza la definición anterior solo cuando la API de registro lo permite expresamente.

## Resolución

Los parámetros del constructor con tipos de clases registradas o concretas se resuelven de forma recursiva. Los valores predeterminados pueden satisfacer parámetros opcionales no resueltos. Las interfaces requieren enlaces explícitos. La construcción circular, los parámetros escalares irresolubles, las clases ausentes y los resultados no válidos de fábricas fallan con excepciones del contenedor.

El contenedor tiene alcance de aplicación. Los servicios del framework, como la configuración, el enrutador, la canalización de middleware, el despachador y el administrador de extensiones, se instalan durante la construcción de la aplicación. Los servicios de la aplicación normalmente se registran en `Bootstrap::register()`.

## Límite

La conexión automática construye dependencias; no realiza validación de dominio, no elige entre implementaciones ambiguas ni descubre automáticamente paquetes de terceros.

## 📚 Documentos relacionados

- [Ciclo de vida de la aplicación](application-lifecycle.md)
- [Extensiones](extensions.md)
- [Guía para desarrolladores del núcleo](../../technical/development/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
