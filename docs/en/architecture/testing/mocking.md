### 📄 `docs/testing/mocking.md`

# 🧪 Mocking & Stubbing in Bluewater Tests

📄 **File:** `docs/testing/mocking.md`  
📅 **Status:** Stub  
🏷️ **Tags:** testing, mocking, QA, dev-tools  
🔖 **Version:** 1.0  
📦 **Scope:** 🧪 Testing Utilities & Dependency Isolation  
👨‍💻 **Maintainer:** QA/Dev Team

---

## 📘 OVERVIEW

This guide describes how to use **mocking** and **stubbing** within the Bluewater framework to simulate dependencies during tests. This is essential for isolating logic in unit and integration tests.

---

## 🛠️ Mocking vs Stubbing

| Term     | Purpose                                |
|----------|----------------------------------------|
| **Stub** | Returns predefined data for test input |
| **Mock** | Also tracks usage (e.g., method calls) |

---

## 🔧 Libraries

| Tool        | Purpose                    |
|-------------|----------------------------|
| [Mockery](https://github.com/mockery/mockery) | Fluent mocking API for PHP |
| PHPUnit Mocks | Native PHPUnit mocking    |

---

## 🧩 Example: Stubbing a Service

```php
$mockService = \Mockery::mock(MyService::class);
$mockService->shouldReceive('getStatus')
            ->once()
            ->andReturn('OK');

$app->instance(MyService::class, $mockService);
````

---

## 🛠️ Anonymous Mock via Interface

```php
$logger = new class implements \Psr\Log\LoggerInterface {
  public function emergency($msg, array $context = []) { /* ... */ }
  // Implement all required PSR-3 methods...
};
```

📎 See: [PSR-3 LoggerInterface](https://www.php-fig.org/psr/psr-3/)

---

## 💡 Use Cases

* Mocking DB/ORM layers
* Intercepting third-party APIs
* Faking time, auth, environment behavior
* Replacing config/service container entries

---

## ⚠️ Tips & Considerations

| Concern              | Guidance                                        |
|----------------------|-------------------------------------------------|
| Overuse of mocks     | May obscure real issues—use judiciously         |
| Maintenance overhead | Keep mocks in helper methods or trait utilities |
| Test fragility       | Prefer mocking interfaces, not full classes     |

---

## 📎 Related Topics

* [`unit-testing.md`](unit-testing.md)
* [`integration-testing.md`](integration-testing.md)
* [`testing.md`](testing.md)

---

📎 *Mock what you don't own. Trust what you do.*

---
