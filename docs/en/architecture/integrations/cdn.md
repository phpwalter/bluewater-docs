# 🌐 CDN Integration – Bluewater

📄 **File:** `docs/integrations/cdn.md`  
📅 **Status:** Stub  
🏷️ **Tags:** integrations, cdn, static, delivery, assets  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – DevOps & Frontend Infrastructure  
👨‍💻 **Author:** Bluewater Team

---

## Overview

A CDN (Content Delivery Network) improves the performance, scalability, and reliability of your API and asset delivery. Bluewater is CDN-compatible out of the box, and static assets can be served via any modern CDN layer.

---

## 🌍 Popular CDN Providers

| Provider                                                | Notes                                   |
|---------------------------------------------------------|-----------------------------------------|
| [Cloudflare](https://www.cloudflare.com/)               | Global edge cache, DNS, firewall        |
| [Fastly](https://www.fastly.com/)                       | Real-time purging, dynamic origin rules |
| [Amazon CloudFront](https://aws.amazon.com/cloudfront/) | Integrated with S3, scalable            |
| [BunnyCDN](https://bunny.net/)                          | Cost-effective, image optimization      |

---

## 📁 Use Cases

- Serve versioned API documentation (`/docs`)
- Host static frontend assets (SPA)
- Cache JSON API responses (with headers)
- Deliver file uploads & avatars
- Integrate edge-side security (WAFs, bot protection)

---

## 🔧 Setup Guidelines

- Ensure Bluewater emits correct caching headers (via `Responder`)
- Use unique URLs or cache-busting query strings for updated content
- Configure CDN to forward request headers (e.g. `Authorization` for protected endpoints)

---

## 🧩 Caching Example

```php
$response = new JsonResponse($data, 200, [
    'Cache-Control' => 'public, max-age=3600',
    'ETag' => $etag
]);
````

---

## 🔐 Security Considerations

* Disable caching on authenticated endpoints
* Sign asset URLs or use expiring links
* Combine with rate-limiting middleware

---

## 📂 Suggested Assets Folder

```
public/
 └── assets/
      └── docs/
      └── avatars/
```

---

## 🔗 Related

* [`docs/performance.md`](../deployment/performance.md)
* [`docs/integrations/file-storage.md`](file-storage.md)
* [Cloudflare CDN Docs](https://developers.cloudflare.com/cache/about/)

---

```
