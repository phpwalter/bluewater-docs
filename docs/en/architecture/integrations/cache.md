# 🗃️ Caching Integration – Bluewater

📄 **File:** `docs/integrations/cache.md`  
📅 **Status:** Stub  
🏷️ **Tags:** integrations, cache, psr-6, psr-16  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – Performance & Deployment Teams  
👨‍💻 **Author:** Bluewater Team

---

## Overview

Bluewater does not include internal caching logic, but it is fully compatible with any **PSR-6** or **PSR-16** compliant caching adapter. Use it to cache expensive computations, database results, API responses, or configuration blobs.

---

## 📦 Supported Backends

| Tool                                                                   | PSR Support                                                                                       | Use Case                          |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|-----------------------------------|
| [Redis](https://redis.io/)                                             | ✅ [PSR-16](https://www.php-fig.org/psr/psr-16/)                                                   | High-speed memory caching         |
| [Memcached](https://www.memcached.org/)                                | ✅ [PSR-16](https://www.php-fig.org/psr/psr-16/)                                                   | Lightweight distributed cache     |
| [Symfony Cache](https://symfony.com/doc/current/components/cache.html) | ✅ [PSR-16](https://www.php-fig.org/psr/psr-16/)<br/>✅ [PSR-6](https://www.php-fig.org/psr/psr-6/) | Versatile and filesystem-friendly |
| [Doctrine Cache](https://www.doctrine-project.org/projects/cache.html) | ✅ [PSR-16](https://www.php-fig.org/psr/psr-6/)                                                    | Legacy support                    |
| [Laravel Cache](https://laravel.com/docs/cache)                        | 🚫 Adapter required                                                                               | Wrapper around Redis, Memcached   |

---

## 🛠️ Installation

```bash
composer require symfony/cache
composer require cache/filesystem-adapter
````

---

## 🏗️ Usage Example (PSR-16)

```php
use Symfony\Component\Cache\Adapter\FilesystemAdapter;
use Symfony\Component\Cache\Psr16Cache;

$adapter = new FilesystemAdapter();
$cache = new Psr16Cache($adapter);

$cache->set('key', 'value', 3600); // 1 hour TTL
```

---

## 📂 Where to Use Cache

* ✅ Middleware (rate limiting, auth token checks)
* ✅ Controllers (data output, third-party calls)
* ✅ Services (internal logic, lookup tables)

---

## 🧪 Testing with Null Cache

For tests, use:

```php
composer require cache/null-adapter
```

Or manually mock PSR-16:

```php
class DummyCache implements Psr\SimpleCache\CacheInterface {
    public function get($key, $default = null) { return null; }
    public function set($key, $value, $ttl = null) { return true; }
    public function delete($key) { return true; }
    // ...
}
```

---

## 🔐 Security Considerations

* Don't cache secrets or credentials
* Always namespace cache keys by tenant/environment

---

## 🔗 Related

* [`docs/performance.md`](../deployment/performance.md)
* [PSR-6 Spec](https://www.php-fig.org/psr/psr-6/)
* [PSR-16 Spec](https://www.php-fig.org/psr/psr-16/)

---
