<!-- locale-guard:language-bar:start -->
[<img src="../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../en/contribute/documentation.md) | **<img src="../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Contribuciones a la documentación – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/contribute/documentation.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** contributing, documentation, quality
🔖 **Versión:** 1.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Reglas de redacción, revisión, validación y sincronización
🤝 **Colaboradores:** Mantenedores de la documentación y del framework
👨‍💻 **Autor:** Equipo de documentación de Bluewater

---

> ### 🪶 **Principio de Bluewater**
> *La documentación cambia junto con el comportamiento, no después.*

---

## 📌 Propósito

Esta guía define los criterios de aceptación para las contribuciones a la documentación de Bluewater.

## Reglas de redacción

1. Comience con [`docs/en/_templates/document.md`](../../../en/_templates/document.md).
2. Describa el comportamiento implementado por la rama de código fuente de referencia.
3. Utilice rutas de archivo relativas al repositorio y enlaces relativos válidos.
4. Indique con precisión los límites de seguridad y el comportamiento ante fallos.
5. Incluya ejemplos ejecutables sin credenciales ni secretos realistas.
6. Elimine los marcadores provisionales antes de marcar un documento como Activo o Publicado.
7. Conserve exactamente los marcadores de la barra de idiomas de LocaleGuard.

## Propiedad y sincronización

Las guías técnicas se originan en `bluewater-framework`. La arquitectura, la navegación, la localización y la publicación se mantienen en `bluewater-docs`. Un cambio en el comportamiento del framework debe actualizar su documentación fuente antes que la copia de publicación sincronizada.

## Comprobaciones requeridas

```bash
python -B tools/locale-guard/locale_guard.py update
python -B tools/locale-guard/locale_guard.py check
mkdocs build --strict --config-file docs/mkdocs.yml
```

## 📚 Documentos relacionados

- [Guía de localización](localization.md)
- [Operaciones de documentación](https://github.com/phpwalter/bluewater-docs/blob/main/docs/README.md)
- [Plantilla canónica](../../../en/_templates/document.md)

---

Esta documentación se distribuye bajo la [Licencia MIT](../../../../LICENSE).

---

*Última actualización: 2026-09-03*
