"""Root entry point for Cloud Deployment Platforms (Render, Railway, Heroku, Fly.io, Koyeb, AWS)."""

import os
import sys

# Ensure the root directory is at the front of python path
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Expose the FastAPI ASGI application instance at the root module level
from backend.app.main import app

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    reload = os.environ.get("RELOAD", "false").lower() in ("true", "1", "yes")
    uvicorn.run("main:app", host=host, port=port, reload=reload)
