<!-- locale-guard:language-bar:start -->
[<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../en/contribute/localization.md) | **<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Contribuciones de localización – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/contribute/localization.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** contributing, localization, locale-guard
🔖 **Versión:** 1.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Estructura de traducciones, idiomas compatibles y cobertura determinista
🤝 **Colaboradores:** Traductores y mantenedores de documentación
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *La cobertura de traducción se deriva de los archivos; nunca se mantiene como un porcentaje editado manualmente.*

---

## 📌 Propósito

Esta guía explica cómo LocaleGuard gobierna la documentación en inglés, español, alemán y japonés.

## Estructura de idiomas

El inglés es el idioma canónico bajo `docs/en`. Las traducciones reflejan la ruta relativa a esa raíz:

```text
docs/en/architecture/core/index.md
docs/i18n/es/architecture/core/index.md
docs/i18n/de/architecture/core/index.md
docs/i18n/ja/architecture/core/index.md
```

LocaleGuard identifica un documento mediante esta ruta relativa. Mide su existencia y estado de gobernanza; no traduce ni evalúa la calidad de la traducción.

## Actualización del contenido generado

```bash
python -B tools/locale-guard/locale_guard.py update
python -B tools/locale-guard/locale_guard.py check
python -B tools/locale-guard/locale_guard.py missing es
```

Confirme en Git el informe generado, los recursos de banderas copiados y las regiones de marcadores actualizadas junto con el cambio de documentación.

## 📚 Documentos relacionados

- [Guía para contribuir a la documentación](documentation.md)
- [Proyecto LocaleGuard](https://github.com/phpwalter/locale-guard)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../LICENSE).

---

*Última actualización: 2026-09-03*
