# 📬 Webhooks Integration – Bluewater

📄 **File:** `docs/integrations/webhooks.md`  
📅 **Status:** Stub  
🏷️ **Tags:** integrations, webhooks, async, events  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – External API Consumers  
👨‍💻 **Author:** Bluewater Team

---

## Overview

Webhooks are a common way to **receive external events** (e.g., Stripe, GitHub, Twilio) or **notify external systems** when something changes in your app.

Bluewater makes it simple to create **inbound** and **outbound** webhook endpoints using controllers, middleware, and signed requests.

---

## 📥 Inbound Webhooks (e.g., Stripe, GitHub)

### Routing Example

```php
$app->post('/webhooks/github', \App\Controllers\WebhookController::class . ':handleGitHub');
````

### Controller Example

```php
public function handleGitHub($request)
{
    $payload = $request->getParsedBody();
    $sig = $request->getHeaderLine('X-Hub-Signature');

    if (!$this->verifySignature($payload, $sig)) {
        return new JsonResponse(['error' => 'unauthorized'], 401);
    }

    // Process event
}
```

---

## 📤 Outbound Webhooks (e.g., notify partner system)

```php
$payload = json_encode(['event' => 'order.shipped', 'order_id' => 123]);

$response = $httpClient->post('https://partner.io/hook', [
    'headers' => ['X-Signature' => hash_hmac('sha256', $payload, $secret)],
    'body' => $payload,
]);
```

---

## 🔐 Security Best Practices

* Always verify signatures with a shared secret
* Support replay protection (timestamps + nonce)
* Use HTTPS for all webhook delivery
* Respond with `200 OK` only after verification + success
* Log all webhook traffic (success/failure)

---

## 🧱 Suggested Folder Structure

```
app/
 └── Webhooks/
      └── StripeWebhook.php
      └── GitHubWebhook.php
```

---

## 🔗 Related

* [`docs/integrations/payment.md`](payment.md)
* [Stripe Webhooks](https://stripe.com/docs/webhooks)
* [GitHub Webhooks](https://docs.github.com/en/webhooks)

---
