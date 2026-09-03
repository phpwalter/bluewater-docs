### 📚 `docs/core/logger.md` — Stub Content

# 📚 Logger – Bluewater Core Module

📄 **File:** `docs/core/logger.md`  
📅 **Status:** Published  
🏷️ **Tags:** core, logging, psr-3  
🔖 **Version:** 1.0  
📦 **Scope:** 📦 Contributors – Logger implementers and maintainers  
👨‍💻 **Author:** Bluewater Team

---

### ✅ `docs/core/logger.md`

# 📓 Module 5: Logger Module

The Logger module handles internal logging for the framework and application code. It implements the [PSR-3](https://www.php-fig.org/psr/psr-3/) standard to ensure pluggable and interchangeable logging providers.

---

## 🧩 Responsibilities

- Provide centralized logging access across the app
- Delegate to any PSR-3-compliant logger (e.g., Monolog)
- Support multiple output strategies (stdout, file, remote)
- Allow per-environment or per-client configuration

---

## 🔧 Integration Options

Supported backends:

- 🪵 Monolog (file-based, stream, loggly)
- 🐘 PHP error_log()
- 🌐 Remote (e.g., Sentry, DataDog)
- 📦 Custom logger implementing `LoggerInterface`

---

## 🧬 Usage Example

```php
Logger::info('User logged in', ['user_id' => 123]);
Logger::error('Payment failed', ['code' => 500]);
````

Or via injection:

```php
function handle(Request $req, LoggerInterface $log) {
  $log->debug('Processing', [...]);
}
```

---

## 📁 Files

```txt
src/
└── Bluewater/
    └── Core/
        └── Logger/
            ├── Logger.php
            └── LoggerFactory.php
```

---

## ⚙️ Configuration

```env
LOG_CHANNEL=stderr
LOG_LEVEL=debug
LOG_PATH=storage/logs/app.log
```

Each client can override these in their `config/log.php`.

---

## 🧪 Testing

* Assert fallback to stderr on null logger
* Validate log level filtering
* Mock logger to capture output
* Ensure PSR-3 compliance

See [testing.md](../testing/testing.md)

---

## 🔗 Related

* [Responder](responder.md)
* [Architecture Spec](../architecture/architecture.md)
* [Config](config.md)

---

📎 Tags: `core`, `logger`, `psr-3`, `logging`, `debug`

```
