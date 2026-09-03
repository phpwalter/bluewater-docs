<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/usage/logging.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Registro de aplicaciones – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/usage/logging.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, usage, logging, psr-3
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Selección del registrador PSR-3 y registro de solicitudes
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Los registros operativos nunca incluyen credenciales ni contexto sensible no controlado.*

---

## 📌 Propósito

Esta guía explica el registrador predeterminado, el control de la funcionalidad y el middleware de registro de solicitudes.

## Registro

Utilice el registrador proporcionado mediante la capa de registro compatible con PSR-3 de Bluewater en lugar de `echo`, `print_r` o archivos improvisados.

Los registros de la aplicación corresponden al directorio de ejecución de la aplicación:

```text
app/app_1/logs/
```

No escriba registros de la aplicación en `vendor/bluewater/framework`.

## 📚 Documentos relacionados

- [Middleware](middleware.md)
- [Configuración de la aplicación](../setup/configuration.md)
- [Despliegue](../deployment/index.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
