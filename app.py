"""Root application entry point alias for cloud auto-detectors expecting app:app."""

import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Export app instance
from main import app
