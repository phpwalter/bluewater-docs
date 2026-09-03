<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/development/runtime.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Desarrollo del entorno de ejecución – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/development/runtime.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, development, runtime
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Implementación y mantenimiento de adaptadores del entorno de ejecución
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *El núcleo delega la E/S de transporte mediante un contrato de adaptador reducido.*

---

## 📌 Propósito

Esta guía define el límite independiente del entorno de ejecución y los requisitos para adaptadores adicionales.

## Arquitectura del entorno de ejecución

El núcleo de aplicaciones de Bluewater debe permanecer independiente del entorno de ejecución.

FPM es un adaptador, no una suposición fundamental.

Las responsabilidades específicas del entorno de ejecución corresponden a `Bluewater\Runtime`, por ejemplo:

- crear una `Request` de Bluewater a partir de la entrada del entorno de ejecución;
- emitir una `Response` de Bluewater;
- adaptar la semántica del ciclo de vida cuando sea necesario.

No coloque variables globales de FPM ni lógica específica de Apache dentro del enrutamiento, DI, validación, serialización o servicios de la aplicación.

## 📚 Documentos relacionados

- [Despliegue](../deployment/index.md)
- [Arquitectura del núcleo](architecture.md)
- [Pruebas del framework](../testing/framework.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
