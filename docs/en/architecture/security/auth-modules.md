📘 docs/security/auth-modules.md — Authentication Modules
🛡️ Authentication Modules – Bluewater Framework
📄 File: docs/security/auth-modules.md
🧮 Status: ✍️ Draft
🛫 ETA: 2025-06-27
🔖 Version: 0.1
📅 Date: 2025-06-09
🏷️ Tags: security, authentication, jwt, oauth
🌍 Scope: Define available authentication mechanisms in the Bluewater Framework and how they are configured, swapped, and integrated per tenant
👥 Contributors: – Core developers, DevOps engineers, platform integrators
👨‍💻 Author: Bluewater Core Team

📘 Overview
This document outlines the pluggable authentication modules supported by Bluewater. These are designed to accommodate stateless, secure, tenant-aware authentication strategies optimized for API-first use cases.

🪶 Bluewater Principle
Security should be consistent, transparent, and tenant-aware.

🔐 Supported Authentication Modules
Module	Description
JWT	Stateless token-based auth; simple and widely adopted
OAuth2	Delegated authorization with external providers
Next-Gen Auth	Reserved for future pluggable strategies (e.g., mTLS, HMAC)
Each module is configured per tenant and can be swapped dynamically based on configuration.

🧱 Authentication Directory Layout
/src/Bluewater/Security/
├── jwt/
├── oauth/
└── nextgen/
Each folder contains a fully-encapsulated strategy and adheres to a shared authentication interface for flexibility and testability.

🧩 Integration Strategy
Defined in tenant config:
return [
'auth' => [
'driver' => 'jwt',
'issuer' => 'client-name',
'secret' => 'your-client-secret'
]
];
Drivers are loaded dynamically at runtime based on this configuration.
Middleware attaches the chosen driver per request context.
Supports multi-tenancy, statelessness, and horizontal scaling.
🔁 Swappable Auth Architecture
All auth modules implement a common interface, making them interchangeable and extensible. Benefits include:

🔄 Swap jwt for oauth without core rewrites
🧪 Plug in mocks for secure unit/integration testing
🏢 Extend modules with enterprise-specific policies
🔗 Related Documents
middleware.md – Add authentication filters via PSR-15
multi-tenant.md – Per-tenant strategy integration
PSR-15 Middleware Spec
