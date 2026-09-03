<!-- locale-guard:language-bar:start -->
[<img src="../../../../_generated/assets/flags/us.svg" alt="English" width="20" height="auto"> English](../../../../en/technical/usage/dependency-injection.md) | **<img src="../../../../_generated/assets/flags/es.svg" alt="Español" width="20" height="auto"> Español** | <img src="../../../../_generated/assets/flags/de.svg" alt="Deutsch" width="20" height="auto"> Deutsch *(missing)* | <img src="../../../../_generated/assets/flags/jp.svg" alt="日本語" width="20" height="auto"> 日本語 *(missing)*
<!-- locale-guard:language-bar:end -->

# Inyección de dependencias de la aplicación – Bluewater Framework

📄 **Archivo:** `docs/i18n/es/technical/usage/dependency-injection.md`
📅 **Estado:** Activo
🏷️ **Etiquetas:** technical, usage, container, services
🔖 **Versión:** 8.0.0
📅 **Fecha:** 2026-09-03
🌍 **Alcance:** Enlace de parámetros de endpoints y registro de servicios de la aplicación
🤝 **Colaboradores:** Mantenedores del framework Bluewater
👨‍💻 **Autor:** Equipo de Bluewater Framework

---

> ### 🪶 **Principio de Bluewater**
> *Las dependencias permanecen explícitas en los límites de los manejadores y constructores.*

---

## 📌 Propósito

Esta guía explica cómo se resuelven los parámetros de endpoints y los servicios de la aplicación mediante el contenedor.

## Parámetros de solicitud e inyección de dependencias

Los argumentos de los endpoints se resuelven automáticamente.

La resolución incluye:

1. parámetros de ruta;
2. parámetros de la cadena de consulta;
3. inyección de `Request` de Bluewater;
4. hidratación de DTO desde el cuerpo de la solicitud;
5. servicios registrados o conectables automáticamente desde el contenedor de DI;
6. valores predeterminados de parámetros.

Ejemplo:

```php
public function getById(
    int $id,
    UserRepository $users,
): UserDto {
    return $users->find($id);
}
```

`$id` proviene de la ruta y `UserRepository` proviene del contenedor.

## Registro de servicios de la aplicación

Utilice `Bootstrap::register()`.

Ejemplo:

```php
public function register(Application $app): void
{
    $app->services()->bind(
        UserRepository::class,
        DatabaseUserRepository::class,
    );
}
```

Los servicios concretos con constructores resolubles pueden conectarse automáticamente sin registro explícito.

Utilice enlaces explícitos cuando:

- se inyecte una interfaz;
- se reemplace una implementación de Bluewater o predeterminada;
- se creen servicios que requieran configuración o fábricas;
- se elija entre varias implementaciones.

## 📚 Documentos relacionados

- [Enrutamiento](routing.md)
- [Validación](validation.md)
- [Desarrollo del contenedor](../development/dependency-injection.md)

---

Esta documentación publicada se distribuye bajo la [Licencia MIT](../../../../../LICENSE). El código fuente de Bluewater Framework se distribuye por separado bajo la licencia OSL-3.0.

---

*Última actualización: 2026-09-03*
