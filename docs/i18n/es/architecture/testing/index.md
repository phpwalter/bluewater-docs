<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/testing/index.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Arquitectura de pruebas – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/testing/index.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, testing, phpunit, quality
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Capas de verificación automatizada y controles de calidad requeridos
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *Solo se confía en el comportamiento del framework cuando las pruebas ejercitan su contrato público.*

---

## 📌 Propósito

Este documento describe la organización actual de las pruebas de Bluewater v8 y las comprobaciones requeridas para modificar el framework.

## Capas de pruebas

Las pruebas unitarias y específicas de subsistemas abarcan la autenticación, la configuración, el contenedor, los registros, el enrutamiento y la validación. `tests/Integration/App1Test.php` inicia y ejercita la aplicación de referencia para verificar que los subsistemas públicos funcionen juntos desde la perspectiva de un desarrollador de aplicaciones.

## Comando de calidad

El script `check` de Composer del framework ejecuta la validación de sintaxis, las comprobaciones de estilo PSR-12, el análisis de PHPStan y PHPUnit. La integración continua ejecuta el conjunto en PHP 8.3 y PHP 8.4.

```bash
composer install
composer check
```

Los cambios en el comportamiento orientado a aplicaciones deben actualizar las pruebas específicas y la aplicación de referencia cuando se vea afectado un contrato integral. Los ejemplos de la documentación deben permanecer coherentes con la API pública probada.

## Nota sobre el entorno

La compilación de la documentación valida los enlaces y la estructura de forma independiente. La verificación de PHP sigue requiriendo un entorno PHP 8.3 o posterior con Composer y las extensiones declaradas por el framework.

## 📚 Documentos relacionados

- [Guía para desarrolladores del núcleo](../../technical/development/index.md)
- [Enrutamiento y despacho](../http/routing-and-dispatch.md)
- [Seguridad](../security/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
