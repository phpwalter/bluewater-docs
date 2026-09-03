<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/development/dependency-injection.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Desarrollo de la inyección de dependencias – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/development/dependency-injection.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, development, container, psr-11
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Modificación del registro y la resolución de servicios y de la conexión automática
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *La construcción automática nunca adivina entre dependencias ambiguas.*

---

## 📌 Propósito

Esta guía define el contrato de desarrollo del contenedor PSR-11 de Bluewater.

## Desarrollo de la inyección de dependencias

Bluewater utiliza un modelo de DI híbrido:

- servicios registrados explícitamente;
- enlaces de interfaz a clase;
- fábricas invocables;
- conexión automática del constructor para clases concretas cuando sea posible.

No introduzca un descubrimiento oculto de servicios. Las implementaciones de reemplazo deben registrarse explícitamente.

Al agregar un servicio reemplazable del framework, prefiera:

```php
interface Cache
{
    public function get(string $key): mixed;
}
```

con una implementación predeterminada:

```php
final class FileCache implements Cache
{
}
```

Una aplicación puede reemplazarla explícitamente mediante el contenedor.

## 📚 Documentos relacionados

- [Uso de la inyección de dependencias](../usage/dependency-injection.md)
- [Arquitectura del núcleo](architecture.md)
- [Pruebas del framework](../testing/framework.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
