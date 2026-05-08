# fastapi-boilerplate

A minimal FastAPI starter set up with Poetry, Docker Compose, and a layout for routers, middlewares, models, and DB code. Originally scaffolded for a quiz-master AI backend with LangChain and Ollama bindings included.

## Quickstart

```bash
poetry install
poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Or with Docker:

```bash
docker compose up --build
```

The API listens on `http://localhost:8000`.

## Project layout

```
app/
  core/           # config
  db/             # database wiring
  dependencies.py # FastAPI dependencies
  internal/       # internal helpers
  main.py         # FastAPI app entry
  middlewares/    # request/response middleware
  models/         # Pydantic models (incl. ResponseModel)
  routers/        # route modules
  utils/          # response helpers
utils/
  langchain/      # LangChain helpers
  logger/         # rotating-file logger setup
  ollama/         # Ollama chat/embedding/model helpers
tests/
```

## Standard response shape

`app/utils/create_response.py` wraps responses in `ResponseModel`:

```python
from app.utils.create_response import create_response

@router.get("/health")
def health():
    return create_response(status_code=200, message="ok", data={"status": "healthy"})
```

Producing:

```json
{
  "status_code": 200,
  "message": "ok",
  "data": {"status": "healthy"},
  "error_code": null,
  "timestamp": "2025-01-01T00:00:00",
  "success": true
}
```

## Tech

- Python 3.12, FastAPI, Uvicorn
- Poetry for dependency management
- Pydantic v2
- Optional: LangChain, langchain-community, langchain-ollama, OpenAI, PyTorch

## License

MIT
