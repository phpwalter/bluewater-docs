<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/development/contributing.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Flujo de contribución – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/development/contributing.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, development, contributing, ci
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Expectativas de ramas, validación, revisión y compatibilidad
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Un cambio solo está completo cuando la implementación, las pruebas, los ejemplos y la documentación concuerdan.*

---

## 📌 Propósito

Esta guía define el flujo requerido para contribuir al núcleo de Bluewater.

## Flujo de contribución

Flujo recomendado:

```text
main
 ↓
feature/fix branch
 ↓
edit src/
 ↓
edit config/ when defaults change
 ↓
add unit tests
 ↓
update app_1 integration coverage when needed
 ↓
run targeted tests
 ↓
composer check
 ↓
push
 ↓
pull request
 ↓
PHP 8.3 + PHP 8.4 CI
 ↓
review
 ↓
merge
```

No combine un cambio del framework únicamente porque sea válido sintácticamente. Los cambios del núcleo deben conservar los objetivos principales de Bluewater: superficie reducida, comportamiento predecible, descubrimiento automático de endpoints basado en archivos, alta eficiencia en el recorrido de solicitudes, puntos de extensión explícitos y depuración directa.

## 📚 Documentos relacionados

- [Desarrollo del núcleo](index.md)
- [Pruebas del framework](../testing/framework.md)
- [Índice técnico](../index.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
