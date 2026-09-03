<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/development/index.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Desarrollo del núcleo – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/development/index.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, development, repository
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Requisitos de desarrollo del framework y propiedad del repositorio
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *El trabajo en el framework conserva el contrato orientado a aplicaciones.*

---

## 📌 Propósito

Esta guía establece los límites del entorno y del repositorio para el desarrollo del núcleo de Bluewater.

## Requisitos de desarrollo

- PHP 8.3 o posterior
- Composer 2
- Git
- PDO SQLite para las pruebas de integración
- SimpleXML para las pruebas de serialización XML

Clone el repositorio e instale las dependencias:

```bash
git clone https://github.com/phpwalter/bluewater-framework.git
cd bluewater-framework
composer install
```

Durante el desarrollo, trabaje en una rama de funcionalidad en lugar de hacerlo directamente en `main`:

```bash
git switch main
git pull
git switch -c feature/my-change
```

Hasta que se combine la implementación inicial de Bluewater 8, utilice la rama de implementación:

```bash
git switch build/bluewater-v8
composer install
```

## Estructura del repositorio

```text
bluewater-framework/
├── src/                 # Framework source
├── config/              # Bluewater default configuration
├── tests/               # Unit and integration tests
├── examples/
│   └── host/
│       ├── app/
│       │   └── app_1/   # Reference application
│       └── public/
│           └── app_1/   # Reference front controller
├── composer.json
├── phpunit.xml.dist
└── README.md
```

La regla principal de propiedad es sencilla:

```text
src/ + config/ + tests/ = Bluewater framework
examples/host/app/app_1 = application-level reference implementation
```

No implemente comportamiento del framework dentro de `app_1`. `app_1` existe para demostrar que el framework se comporta correctamente desde el punto de vista de un desarrollador de aplicaciones.

## 📚 Documentos relacionados

- [Arquitectura del núcleo](architecture.md)
- [Flujo de contribución](contributing.md)
- [Pruebas](../testing/framework.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
