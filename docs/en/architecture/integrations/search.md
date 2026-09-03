# 🔍 Search Integration – Bluewater

📄 **File:** `docs/integrations/search.md`  
📅 **Status:** Stub  
🏷️ **Tags:** integrations, search, elasticsearch, fulltext  
🔖 **Version:** 1.0  
📦 **Scope:** 🌐 Public – Backend Developers  
👨‍💻 **Author:** Bluewater Team

---

## Overview

Bluewater does not include built-in search services, but integrates easily with full-text indexing engines and APIs like **ElasticSearch**, **Meilisearch**, or **Algolia**.

---

## 🧠 When to Use Search

| Use Case                        | Solution             |
|---------------------------------|----------------------|
| Full-text search over content   | Meilisearch, Elastic |
| Fuzzy search/autocomplete       | Algolia, Meilisearch |
| Filtering & aggregation         | ElasticSearch        |
| Instant results + typo handling | Algolia              |

---

## 🔧 Recommended Tools

| Tool                                                   | Type        | Highlights                                |
|--------------------------------------------------------|-------------|-------------------------------------------|
| [Meilisearch](https://www.meilisearch.com/)            | Self-hosted | Fast, typo-tolerant, dev-friendly         |
| [ElasticSearch](https://www.elastic.co/elasticsearch/) | Self-hosted | Enterprise search, scaling, DSL query     |
| [Algolia](https://www.algolia.com/)                    | SaaS        | Fastest hosted search, generous free tier |

---

## ⚙️ Installation Example (Meilisearch PHP)

```bash
composer require meilisearch/meilisearch-php
````

```php
$client = new MeiliSearch\Client('http://127.0.0.1:7700', 'masterKey');
$index = $client->index('products');
$index->addDocuments([ ['id' => 1, 'name' => 'Bluewater API'] ]);
```

---

## 🔐 Security Tips

* Use API keys for hosted SaaS services
* Sanitize search queries
* Monitor query performance + abuse

---

## 🧩 Best Practices

* Normalize all searchable content
* Store search index config alongside models
* Cache common queries in Redis

---

## 🔗 Related

* [Meilisearch PHP Docs](https://docs.meilisearch.com/reference/api/)
* [Elasticsearch PHP Client](https://www.elastic.co/guide/en/elasticsearch/client/php-api/current/index.html)
* [Algolia PHP Client](https://www.algolia.com/doc/api-client/getting-started/install/php/)

---

```
