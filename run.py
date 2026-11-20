"""AppVault AI Production & Local Launch Script."""

import uvicorn
import sys
import os

# Set UTF-8 encoding for stdout on Windows
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Expose app object so `uvicorn run:app` also works seamlessly
from backend.app.main import app

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    host = os.environ.get("HOST", "0.0.0.0")
    reload = os.environ.get("RELOAD", "false").lower() in ("true", "1", "yes")

    print("=" * 60)
    print("   AppVault AI - Software Discovery & PC Compatibility")
    print(f"   Listening on: http://{host}:{port}")
    print(f"   Deployment Mode: {'Development (reload)' if reload else 'Production'}")
    print("=" * 60)

    uvicorn.run("main:app", host=host, port=port, reload=reload)
