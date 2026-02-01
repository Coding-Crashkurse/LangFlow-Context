from __future__ import annotations

import os
import uuid

import requests
from dotenv import load_dotenv


def main() -> None:
    load_dotenv()

    api_key = os.getenv("LANGFLOW_API_KEY")
    if not api_key:
        raise RuntimeError("LANGFLOW_API_KEY missing in .env")

    url = "http://localhost:7860/api/v1/run/9a92b9ac-4e3f-4197-aa9c-384bbd3e8bc6"

    payload = {
        "output_type": "chat",
        "input_type": "chat",
        "input_value": "hello world!",
        "session_id": str(uuid.uuid4()),
    }

    headers = {
        "x-api-key": api_key,
        "X-LANGFLOW-GLOBAL-VAR-username": "alice",
    }

    response = requests.post(url, json=payload, headers=headers, timeout=30)
    response.raise_for_status()

    data = response.json()
    message = data["outputs"][0]["outputs"][0]["results"]["message"]["text"]
    print(message)


if __name__ == "__main__":
    main()