<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/development/configuration.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Desarrollo de la configuración – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/development/configuration.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, development, configuration
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Modificación de la configuración predeterminada y del comportamiento de combinación
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Los cambios de configuración conservan el tipo, la propiedad y la resolución determinista.*

---

## 📌 Propósito

Esta guía define las reglas de ingeniería para modificar el comportamiento de configuración de Bluewater.

## Desarrollo de la configuración

Los valores predeterminados propiedad de Bluewater se encuentran bajo `config/`.

Ejemplos:

```text
config/Bluewater.ini.php
config/BW.db.ini.php
config/BW.logging.ini.php
config/BW.session.php
```

Las sobrescrituras de la aplicación corresponden a la aplicación, no al paquete del framework:

```text
app/app_1/config/App.ini.php
app/app_1/config/App.db.ini.php
app/app_1/config/App.logging.ini.php
```

El comportamiento de configuración sigue estas reglas:

- los valores predeterminados de Bluewater se cargan primero;
- la configuración de la aplicación sobrescribe los valores permitidos;
- `BW_VER` está bloqueado;
- los tipos de las sobrescrituras deben coincidir con el tipo definido por Bluewater;
- las referencias no resueltas hacen fallar el arranque;
- las referencias circulares hacen fallar el arranque;
- la configuración efectiva se compila en el directorio de caché de la aplicación activa;
- Bluewater nunca escribe datos generados en el directorio de su propio paquete.

Los marcadores heredados como `{APP_ROOT}`, `{CACHE_ROOT}`, `{BLUEWATER}`, `{SITE_ROOT}` y `{DS}` se admiten como vocabulario de compatibilidad sin hacer que los componentes internos del framework dependan de constantes globales de PHP.

Al agregar configuración nueva al framework, defina un valor predeterminado seguro en el archivo `BW.*` correspondiente y agregue pruebas que cubran tanto el valor predeterminado como el comportamiento de sobrescritura de la aplicación.

## 📚 Documentos relacionados

- [Configuración de la aplicación](../setup/configuration.md)
- [Arquitectura del núcleo](architecture.md)
- [Pruebas del framework](../testing/framework.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
