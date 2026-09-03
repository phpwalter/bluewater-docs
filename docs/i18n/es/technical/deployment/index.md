<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/deployment/index.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Despliegue con PHP-FPM – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/deployment/index.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, deployment, fpm, operations
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Selección de aplicaciones en producción y aislamiento de múltiples aplicaciones
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *La identidad de la aplicación proviene de una configuración de proceso confiable, nunca de la entrada de una solicitud.*

---

## 📌 Propósito

Esta guía define el límite de despliegue en producción implementado por el adaptador de entorno de ejecución FPM de Bluewater.

## Guía de despliegue en producción

Para un host con varias aplicaciones, utilice preferentemente un grupo PHP-FPM por aplicación.

Ejemplo conceptual de despliegue:

```text
app1.example.com
    → app_1 FPM pool
    → BLUEWATER_APP=app_1

app2.example.com
    → app_2 FPM pool
    → BLUEWATER_APP=app_2
```

Ambas pueden utilizar la misma ubicación física:

```text
host/vendor/bluewater/framework
```

pero mantienen independientes:

```text
config
cache
logs
endpoints
services
```

La identidad de la aplicación debe proporcionarse mediante una configuración confiable del servidor web o FPM, no mediante datos arbitrarios de la solicitud.

## Controles responsabilidad del operador

Bluewater no aprovisiona servidores web, TLS, contenedores, clústeres, secretos, bases de datos, copias de seguridad ni plataformas de observabilidad. Los operadores deben configurar esos controles y asegurarse de que los directorios de caché y registros de cada aplicación tengan los privilegios mínimos necesarios.

## 📚 Documentos relacionados

- [Estructura del host](../setup/host-layout.md)
- [Configuración de la aplicación](../setup/configuration.md)
- [Desarrollo del entorno de ejecución](../development/runtime.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
