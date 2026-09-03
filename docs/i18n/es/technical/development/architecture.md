<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/development/architecture.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Desarrollo de la arquitectura del núcleo – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/development/architecture.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, development, architecture, public-api
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Reglas de espacios de nombres, límites de extensión y cambios en subsistemas
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Los contratos públicos permanecen reducidos, explícitos y verificables.*

---

## 📌 Propósito

Esta guía define dónde corresponde el comportamiento nuevo del framework y cómo se protege la compatibilidad pública.

## Convenciones de espacios de nombres y código fuente

Las clases del framework Bluewater utilizan el espacio de nombres `Bluewater\` y la asignación PSR-4 desde `src/`.

Ejemplo:

```text
src/Routing/Router.php
```

se asigna a:

```php
namespace Bluewater\Routing;

final class Router
{
}
```

Los subsistemas públicos actuales incluyen:

```text
Bluewater\Auth
Bluewater\Config
Bluewater\Container
Bluewater\Database
Bluewater\Endpoint
Bluewater\Extension
Bluewater\Http
Bluewater\Logging
Bluewater\Middleware
Bluewater\OpenApi
Bluewater\Routing
Bluewater\Runtime
Bluewater\Serialization
Bluewater\Validation
```

El código exclusivo de implementación debe ubicarse cada vez más bajo:

```text
Bluewater\Internal\...
```

Todo lo que se encuentre bajo `Bluewater\Internal` queda fuera del contrato de compatibilidad de versiones semánticas.

## Reglas de diseño de la API pública

Bluewater debe seguir siendo fácil de comprender desde el código de la aplicación.

Prefiera los mecanismos de extensión en este orden:

1. interfaces;
2. composición e inyección de dependencias;
3. extensiones explícitas;
4. herencia únicamente donde se haya diseñado deliberadamente.

Las clases de implementación del núcleo normalmente deben ser `final`. Si una aplicación necesita reemplazar un comportamiento, exponga una interfaz o un enlace de servicio en lugar de exigir subclases de componentes internos del framework.

Los desarrolladores de aplicaciones no deben necesitar comprender los componentes internos de PSR para el desarrollo habitual con Bluewater. Las API nativas de Bluewater deben seguir siendo la superficie principal, mientras la interoperabilidad PSR se proporciona internamente.

La interoperabilidad actual incluye:

- contenedor PSR-11;
- registro PSR-3;
- puente PSR-7 explícito;
- adaptador de middleware PSR-15 explícito.

## Incorporación de código al framework

Agregue las funcionalidades del framework bajo el subsistema `src/` correspondiente.

Por ejemplo, un atributo de validación nuevo podría requerir:

```text
src/Validation/MaxLength.php
src/Validation/Validator.php
```

y las pruebas correspondientes:

```text
tests/Validation/ValidatorTest.php
```

Una funcionalidad que afecte el modelo de desarrollo orientado a aplicaciones también debe demostrarse o ejercitarse mediante `examples/host/app/app_1`.

Los ejemplos incluyen cambios en:

- enrutamiento;
- invocación de endpoints;
- configuración;
- middleware;
- inyección de dependencias;
- autenticación;
- serialización;
- integración con bases de datos;
- generación de OpenAPI;
- adaptadores del entorno de ejecución.

## 📚 Documentos relacionados

- [Desarrollo del núcleo](index.md)
- [Referencia de la API pública](../references/public-api.md)
- [Flujo de contribución](contributing.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
