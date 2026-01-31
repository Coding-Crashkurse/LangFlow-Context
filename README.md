# Langflow Context Demo

Minimal example showing how to pass request context into a Langflow flow so a custom component can read it via `self.ctx`.

---

## What this shows

- Send JSON `context` to `/api/v1/run/{flow_id}`
- Custom component reads values from `self.ctx`
- Alternative: use `X-LANGFLOW-GLOBAL-VAR-*` headers instead of payload context

---

## Project structure
```
langflow-context-demo/
├── mycomponent/
│   └── personalizer.py   # reads ctx["username"]
└── README.md
```

---

## Call flow with context

**Option A: Context in payload**
```powershell
curl -X POST "$env:LANGFLOW_HOST/api/v1/run/$env:FLOW_ID" `
  -H "x-api-key: $env:LANGFLOW_API_KEY" `
  -H "Content-Type: application/json" `
  -d '{
    "input_request": {
      "input_value": "ping",
      "input_type": "chat",
      "output_type": "chat"
    },
    "context": {
      "username": "alice"
    }
  }'
```

**Option B: Context via header**
```powershell
curl -X POST "$env:LANGFLOW_HOST/api/v1/run/$env:FLOW_ID" `
  -H "x-api-key: $env:LANGFLOW_API_KEY" `
  -H "Content-Type: application/json" `
  -H "X-LANGFLOW-GLOBAL-VAR-username: alice" `
  -d '{
    "input_request": {
      "input_value": "ping",
      "input_type": "chat",
      "output_type": "chat"
    }
  }'
```