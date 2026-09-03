# 📝 Logging Integration – Bluewater

📄 **File:** `docs/integrations/logging.md`  
📅 **Status:** Stub  
🏷️ **Tags:** integrations, logging, psr-3, monitoring  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – DevOps & QA Teams  
👨‍💻 **Author:** Bluewater Team

---

## Overview

Bluewater supports PSR-3-compliant logging out of the box via its core `Logger` module. This guide explains how to extend logging using third-party tools and external services.

---

## 🔧 Default Logger

By default, Bluewater uses a null logger unless configured otherwise.

- Interface: `Psr\Log\LoggerInterface`
- Bound in core via dependency injection

---

## 🔌 External Loggers

| Tool                                                        | Description                                   |
|-------------------------------------------------------------|-----------------------------------------------|
| [Monolog](https://seldaek.github.io/monolog/)               | Industry-standard PHP logging library (PSR-3) |
| [stderr](https://www.php.net/manual/en/function.fwrite.php) | Logs to standard error (e.g. Docker, FPM)     |
| [Syslog](https://www.php.net/manual/en/function.syslog.php) | Sends logs to OS-level system logs            |
| [Sentry](https://sentry.io/welcome/)                        | Full-stack cloud error and exception tracking |
| [Loggly](https://www.loggly.com/)                           | Cloud-based log aggregation and analysis      |
| [AWS CloudWatch](https://docs.aws.amazon.com/cloudwatch/)   | Centralized logs and metrics on AWS           |


---

## 🔄 Configuration

You can wire your logger via service provider or middleware.

```php
use Monolog\Logger;
use Monolog\Handler\StreamHandler;

$log = new Logger('api');
$log->pushHandler(new StreamHandler(__DIR__.'/../../logs/app.log'));

$app->set(LoggerInterface::class, $log);
````

---

## 🧪 Testing Log Output

Use PSR-3 mocks or in-memory loggers in test environments.

- [psr/log-test](https://github.com/php-fig/log/blob/master/Psr/Log/Test/LoggerInterfaceTest.php) for testing implementations
- You can also stub `LoggerInterface` manually with anonymous classes or mocks


---

## 🔗 Related

* [`core/logger.md`](../core/logger.md)
* [PSR-3 Spec](https://www.php-fig.org/psr/psr-3/)
* [Monolog Docs](https://seldaek.github.io/monolog/)

---

```
