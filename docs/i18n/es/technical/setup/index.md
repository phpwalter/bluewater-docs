<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/setup/index.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Configuración inicial – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/setup/index.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, setup, requirements
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Requisitos e instalación
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Un entorno de ejecución válido y un límite explícito del host preceden al código de la aplicación.*

---

## 📌 Propósito

Esta guía define el entorno de ejecución compatible e instala Bluewater en un proyecto host.

## Requisitos

- PHP 8.3 o posterior
- Composer 2
- Un entorno web o de ejecución compatible, como PHP-FPM detrás de Apache o Nginx

## Instalación de Bluewater en un proyecto host

En el proyecto host:

```bash
composer require bluewater/framework
```

Para el desarrollo local del framework, puede utilizarse en su lugar un repositorio de ruta de Composer.

La instalación de Composer del host controla Bluewater y los paquetes compartidos de terceros. No es necesario agregar las clases PHP específicas de la aplicación a la sección de carga automática del `composer.json` del host, porque Bluewater registra dinámicamente el espacio de nombres de la aplicación activa durante la ejecución.

## 📚 Documentos relacionados

- [Estructura del host](host-layout.md)
- [Configuración](configuration.md)
- [Índice técnico](../index.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
