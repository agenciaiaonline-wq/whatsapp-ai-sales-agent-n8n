# Importing & Wiring the 3 n8n Workflows

1. Start the local stack (`docker compose -f docker/docker-compose.example.yml up -d`).
2. Import [`02-rag-quote-and-booking.example.json`](02-rag-quote-and-booking.example.json) and [`03-human-handoff-crm.example.json`](03-human-handoff-crm.example.json) first so sub-workflow IDs exist.
3. Import [`whatsapp-ai-closer.example.json`](whatsapp-ai-closer.example.json) and point WAHA's webhook target to `http://n8n:5678/webhook/waha-inbound`.
4. Test locally by posting [`../examples/sample_waha_webhook.json`](../examples/sample_waha_webhook.json) and confirming `Redis` deduplicates duplicate retries cleanly.
