### 📄 `docs/modules/monitoring.md`

# 📊 Monitoring Module – Bluewater Framework

📄 **File:** `docs/modules/monitoring.md`  
📅 **Status:** Stub  
🏷️ **Tags:** monitoring, tracing, logging, observability  
🔖 **Version:** 1.0  
📦 **Scope:** ⚙️ Infrastructure – Ops & Dev Teams  
👨‍💻 **Maintainer:** Bluewater Core Team

---

## 📘 OVERVIEW

This module defines how to integrate observability into a Bluewater-powered API using standard loggers, tracers, and metrics providers. It supports a pluggable strategy and avoids hard dependencies.

---

✅ Updated the **"Observability Tools"** table in [`monitoring.md`](monitoring.md) to include external links for each tool:

---

### 📈 Observability Tools

| Tool                                                                | Integration Type  | Notes                                                                |
|---------------------------------------------------------------------|-------------------|----------------------------------------------------------------------|
| [Sentry](https://sentry.io/)                                        | Error logging     | Via [PSR-3](https://www.php-fig.org/psr/psr-3/) or custom middleware |
| [New Relic](https://newrelic.com/)                                  | APM               | Agent-based, zero config in app                                      |
| [OpenTelemetry](https://opentelemetry.io/docs/instrumentation/php/) | Tracing + metrics | Middleware-based spans                                               |
| [Prometheus](https://prometheus.io/)                                | Metrics scraping  | Exposed via `/metrics` route                                         |
---

## 🧩 Implementation Strategy

1. Use `LoggerInterface` for application-level logs  
2. Inject tracing middleware per route group  
3. Emit metrics via response headers or endpoints  

---

## 🧪 Debug & Metrics Endpoint Example

```php
$router->get('/metrics', [MetricsController::class, 'expose']);
````

Return content compatible with Prometheus or StatsD.

---

## 🛠️ Configurable Logging

Define logger via PSR-3 config:

```php
return [
  'log' => [
    'driver' => 'monolog',
    'level' => 'error',
    'channels' => ['sentry', 'stderr']
  ]
];
```

---

## 🔧 Best Practices

* Use structured logs (JSON)
* Separate error logs from audit logs
* Don’t log secrets or tokens
* Add unique trace/request IDs in middleware

---

## 🔗 Related Docs

* [`logger.md`](../core/logger.md)
* [`monitoring.md`](../integrations/monitoring.md)
* [OpenTelemetry PHP](https://opentelemetry.io/docs/instrumentation/php/)
* [PSR-3: Logger Interface](https://www.php-fig.org/psr/psr-3/)

---

📊 *If you can’t measure it, you can’t improve it.*

---
