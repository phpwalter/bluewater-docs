# 🧭 Distributed Tracing – Bluewater

📄 **File:** `docs/integrations/tracing.md`  
📅 **Status:** Stub  
🏷️ **Tags:** integrations, tracing, observability, devops  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – Platform Engineers & SREs  
👨‍💻 **Author:** Bluewater Team

---

## Overview

Distributed tracing lets you track the lifecycle of a request across services, making it essential for debugging and performance profiling in microservice architectures.

While Bluewater does not include built-in tracing, it supports integration with tools like **OpenTelemetry**, **Jaeger**, and **Zipkin**.

---

## 🛰️ Key Benefits

- Understand bottlenecks across services
- Visualize execution flow and latency
- Profile middleware, DB, and external services
- Correlate logs and traces with request IDs

---

## 📦 Recommended Tools

| Tool                                                                    | Description                                 |
|-------------------------------------------------------------------------|---------------------------------------------|
| [OpenTelemetry PHP](https://opentelemetry.io/docs/instrumentation/php/) | Standard tracing & metrics SDK              |
| [Jaeger](https://www.jaegertracing.io/)                                 | Distributed tracing backend via OpenTracing |
| [Zipkin](https://zipkin.io/)                                            | Lightweight trace collection + UI           |
| [New Relic](https://newrelic.com/)                                      | APM with tracing support                    |

---

## 🛠️ Setup with OpenTelemetry

```bash
composer require open-telemetry/sdk
composer require open-telemetry/exporter-jaeger
````

---

### Example Usage

```php
use OpenTelemetry\API\Trace\TracerProvider;

$provider = TracerProvider::getDefault();
$tracer = $provider->getTracer('bluewater');

$span = $tracer->spanBuilder('http_request')->startSpan();
$span->end();
```

---

## 🔗 Middleware Integration

* Wrap request lifecycle with a root span
* Create child spans for:

  * Router/dispatcher
  * Middleware stack
  * DB queries or external APIs

---

## 🧠 Best Practices

* Inject `trace-id` into all logs and errors
* Use HTTP headers to propagate context across services
* Limit span detail in production (to reduce overhead)

---

## 🔐 Security Tips

* Never trace sensitive user data
* Sanitize trace attributes before export
* Limit trace retention period

---

## 🔗 Related

* [OpenTelemetry PHP Docs](https://opentelemetry.io/docs/instrumentation/php/)
* [`docs/integrations/monitoring.md`](monitoring.md)
* [`docs/performance.md`](../deployment/performance.md)

---
