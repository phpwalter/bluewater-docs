<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/architecture/http/validation.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Arquitectura de validación – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/architecture/http/validation.md`
📅 **Estado:** Publicado
🏷️ **Etiquetas:** architecture, validation, dto, attributes
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Hidratación de DTO, atributos de validación, errores y limitaciones
🤝 **Colaboradores:** Arquitectos y mantenedores del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *La validación rechaza las entradas de aplicación mal formadas antes de que comience el trabajo de dominio.*

---

## 📌 Propósito

Este documento describe cómo los cuerpos de solicitud de endpoints se convierten en DTO y cómo se representan los fallos de validación.

## Hidratación

Un cuerpo de solicitud en forma de arreglo puede hidratar una clase cuyo espacio de nombres contenga `\DTO\`. Los parámetros del constructor se completan mediante claves de cadena coincidentes. Las claves desconocidas se ignoran. Los parámetros ausentes del constructor que no tienen valores predeterminados producen errores de campo antes de la construcción.

## Restricciones integradas

- `#[Required]` rechaza valores ausentes, nulos, cadenas en blanco y arreglos vacíos.
- `#[Email]` valida un valor no vacío como dirección de correo electrónico.
- `#[MinLength(n)]` aplica la longitud mínima de caracteres configurada.

La validación se habilita mediante el valor de configuración `features.VALIDATION`. Una `ValidationException` contiene un mapa estable de campos a listas de mensajes. Durante el despacho del endpoint se convierte en JSON HTTP 422 con `error: validation_failed` y `fields`.

## Límite

La validación de DTO valida el contrato de entrada. No autentica llamadores, autoriza acciones, valida políticas de negocio entre registros ni conserva valores. Los servicios de la aplicación deben seguir aplicando las invariantes del dominio.

## 📚 Documentos relacionados

- [Enrutamiento y despacho](routing-and-dispatch.md)
- [Seguridad](../security/index.md)
- [Guía para desarrolladores de aplicaciones](../../technical/usage/index.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../../LICENSE).

---

*Última actualización: 2026-09-03*
