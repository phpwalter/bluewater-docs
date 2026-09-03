### 📄 `docs/modules/cache.md`

# 🗃️ Caching Module – Bluewater Framework

📄 **File:** `docs/modules/cache.md`  
📅 **Status:** Stub  
🏷️ **Tags:** caching, psr-6, psr-16, redis, performance  
🔖 **Version:** 1.0  
📦 **Scope:** ⚙️ Infrastructure – Developers & Deployers  
👨‍💻 **Maintainer:** Bluewater Core Team

---

## 📘 OVERVIEW

This module provides caching integration for route resolution, configuration artifacts, and user-defined runtime data. Bluewater supports both **PSR-6** and **PSR-16** cache interfaces and is storage-engine agnostic.

---

## 📦 Supported Caching Engines

| Engine     | Usage Context               | Adapter Standard                                                                            |
|------------|-----------------------------|---------------------------------------------------------------------------------------------|
| Redis      | Distributed or shared cache | [PSR-6](https://www.php-fig.org/psr/psr-6/) / [PSR-16](https://www.php-fig.org/psr/psr-16/) |
| Memcached  | Fast in-memory cache        | [PSR-16](https://www.php-fig.org/psr/psr-16/)                                               |
| Filesystem | Local file cache (default)  | [PSR-16](https://www.php-fig.org/psr/psr-16/)                                               |
| Array      | In-memory cache for testing | [PSR-16](https://www.php-fig.org/psr/psr-16/)                                               |

---

## 📂 Cache Usage in Framework

| Area            | Cached Content                  | TTL?     |
|------------------|----------------------------------|----------|
| Route Resolver   | Route compilation map            | No       |
| Configuration    | Merged env + tenant config       | No       |
| CLI Output       | Tooling state                    | Optional |
| User App Logic   | Custom business logic cache      | Yes      |

---

## 🛠️ Configuration Example

```php
return [
  'cache' => [
    'driver' => 'redis',
    'ttl' => 3600,
    'namespace' => 'clientA:',
    'servers' => ['localhost:6379']
  ]
];
````

---

## 🔧 Extending Caching Layer

To implement a custom cache:

1. Implement `Psr\SimpleCache\CacheInterface` [PSR-16](https://www.php-fig.org/psr/psr-16/)
2. Or use `Psr\Cache\CacheItemPoolInterface` [PSR-6](https://www.php-fig.org/psr/psr-6/)
3. Register it in `app/{client}/config/cache.php`

---

## 🧪 Testing Cache

* Clear all with: `bin/bluewater cache:clear`
* Mock with `ArrayCache` for in-memory testing
* Use Redis CLI to inspect live entries

---

## 🔗 Related Docs

* [PSR-6 Spec](https://www.php-fig.org/psr/psr-6/)
* [PSR-16 Spec](https://www.php-fig.org/psr/psr-16/)
* [`performance.md`](../meta/performance.md)
* [`config-management.md`](../deployment/config-management.md)

---

💡 *A smart cache system is one you can disable, clear, and rebuild at will.*

---
