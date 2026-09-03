<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/development/routing.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Desarrollo del enrutamiento – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/development/routing.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, development, routing
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Modificación del descubrimiento, la detección de conflictos, la caché y la coincidencia
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Los cambios de enrutamiento permanecen deterministas y no toleran conflictos.*

---

## 📌 Propósito

Esta guía define las invariantes y las pruebas requeridas para modificar el descubrimiento y la coincidencia de rutas.

## Desarrollo del enrutamiento

El enrutamiento es un diferenciador principal de Bluewater y debe tratarse como código de alto riesgo del framework.

La promesa orientada al desarrollador es:

```text
create endpoint file
        ↓
no route manifest
        ↓
route becomes available automatically
```

La implementación del entorno de ejecución puede compilar y almacenar internamente metadatos de enrutamiento, pero los desarrolladores de aplicaciones nunca mantienen esa caché ni ese manifiesto.

Los cambios de rutas deben probar como mínimo:

- rutas estáticas;
- rutas dinámicas;
- precedencia de rutas estáticas;
- conflictos de forma de rutas;
- convenciones de nombres de manejadores;
- sobrescrituras `#[Path]`;
- validación de parámetros y firmas de rutas;
- incorporación de archivos de endpoint;
- modificación de archivos de endpoint;
- eliminación de archivos de endpoint;
- invalidación de caché;
- herencia de middleware de directorio;
- middleware de clase;
- middleware de método.

Ejemplos de la convención habitual:

```php
public function get(): array
```

se asigna a:

```text
GET /users
```

para `Endpoints/users.php`.

```php
public function getById(int $id): array
```

se asigna a:

```text
GET /users/{id}
```

Las rutas excepcionales deben utilizar `#[Path]` en lugar de ampliar indefinidamente la convención de nombres.

## 📚 Documentos relacionados

- [Uso de rutas](../usage/routing.md)
- [Arquitectura del núcleo](architecture.md)
- [Pruebas del framework](../testing/framework.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
