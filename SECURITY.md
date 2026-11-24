# Security Policy

- Require shared webhook secret headers between WAHA and n8n inbound triggers; never expose n8n editor UI publicly without reverse-proxy TLS + basic/SSO auth.
- Rotate `N8N_ENCRYPTION_KEY`, WAHA API tokens, and PostgreSQL passwords prior to production cutover.
- Report issues via [Golden Nodalix Studio on LinkedIn](https://www.linkedin.com/in/agency-golden-nodalix-880598438/).
