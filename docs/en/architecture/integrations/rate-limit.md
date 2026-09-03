# 🚦 Rate Limiting – Bluewater

📄 **File:** `docs/integrations/rate-limit.md`  
📅 **Status:** Stub  
🏷️ **Tags:** integrations, rate-limiting, security  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – Security & API Gateways  
👨‍💻 **Author:** Bluewater Team

---

## Overview

Rate limiting protects your API from abuse and ensures fair usage across clients. Bluewater supports pluggable rate limiting strategies, typically implemented using Redis, shared memory, or in-process counters.

---

## 📦 Common Strategies

| Method         | Description                                        |
|----------------|----------------------------------------------------|
| Fixed Window   | Allow N requests per fixed time period (e.g., 60s) |
| Sliding Window | Tracks request timestamps for rolling intervals    |
| Token Bucket   | Allows bursts followed by recovery over time       |
| Leaky Bucket   | Smooth request flow via gradual token drain        |

---

## 🧰 Recommended Libraries

| Tool                                                                     | Install                                 | Notes                |
|--------------------------------------------------------------------------|-----------------------------------------|----------------------|
| [malkusch/lock](https://github.com/malkusch/lock)                        | `composer require malkusch/lock`        | Locking + rate logic |
| [Symfony RateLimiter](https://symfony.com/doc/current/rate_limiter.html) | `composer require symfony/rate-limiter` | PSR-compatible       |
| Redis (native)                                                           | —                                       | Fast and distributed |

---

## 🛠️ Basic Redis Middleware (Example)

```php
function rateLimit($ip) {
    $key = "rate:{$ip}";
    $count = $redis->incr($key);
    if ($count == 1) $redis->expire($key, 60);
    if ($count > 100) {
        return new JsonResponse(['error' => 'Rate limit exceeded'], 429);
    }
}
````

---

## 🧱 Integration Points

* Place in middleware stack early (before auth/logging)
* Rate limits can vary by:

  * IP address
  * API key
  * Route or HTTP method

---

## 📊 Headers & Response

Send headers to inform clients of rate usage:

```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 42
X-RateLimit-Reset: 1685572132
```

---

## 🔐 Best Practices

* Return HTTP 429 (`Too Many Requests`)
* Log and alert on abuse patterns
* Whitelist trusted IPs/devs in `.env`

---

## 🔗 Related

* [`docs/security/jwt.md`](../security/jwt.md)
* [RFC 6585 – HTTP 429](https://datatracker.ietf.org/doc/html/rfc6585)
* [Symfony RateLimiter Docs](https://symfony.com/doc/current/rate_limiter.html)

---
