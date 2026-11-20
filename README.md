# AppVault AI — Smart Software Discovery & PC Compatibility Platform

**AppVault AI** is a modern, full-stack platform built for discovering PC applications, auditing computer hardware compatibility with a deterministic benchmark engine, comparing software prices in Indian Rupees (INR), and discovering smarter or free alternatives.

---

## 🌟 Key Features

1. **Deterministic PC Compatibility Engine**:
   - Compares user's CPU, GPU, RAM, Available Free Storage, and OS against verified minimum and recommended system requirements.
   - Evaluates hardware based on normalized benchmark capability tiers (0–100 scale), compute capabilities, and dedicated VRAM rather than naive string matching.
   - Outputs plain-language diagnostics (*Meets Recommended Requirements*, *Meets Minimum Requirements*, *May Have Performance Limitations*, or *Does Not Meet Minimum Requirements*).
   - Distinguishes total installed disk capacity from available free space.
   - Includes real-world performance disclaimers (thermal throttling, FPS, 4K scrubbing).

2. **Verified INR Pricing Index**:
   - Comprehensive pricing in Indian Rupees (`₹`) across subscriptions, one-time purchases, freemium, and free open-source software.
   - Filters for 100% Free Software, Under ₹500, Under ₹1,000, Subscriptions, and Lifetime licenses.
   - Official vendor and store links with last-verified timestamps.

3. **Curated Catalog (34 Verified Software Titles)**:
   - Spanning: Games (Cyberpunk 2077, GTA V, The Last of Us Part I, Steam), Video Editing (Premiere Pro, DaVinci Resolve, CapCut, Shotcut, OBS), Graphic Design (Photoshop, GIMP, Krita, Inkscape, Figma), 3D & CAD (Blender, AutoCAD, FreeCAD), Programming & Dev (VS Code, Android Studio, Unity, Unreal Engine 5, Docker Desktop, Visual Studio 2022), AI Applications (ChatGPT Desktop, Notion, Microsoft 365 Copilot), and Audio (FL Studio, Audacity).

4. **AI Application Finder (with Rule-Based Fallback)**:
   - Natural language query parser with instant hardware constraints alignment.
   - Sample queries: *"Find free video editing software for my laptop"*, *"I need software for 3D modelling that works with my RTX 4060"*, *"Find a free alternative to Photoshop"*, *"Recommend programming tools for a beginner"*.
   - Explains *Why Recommended*, *Hardware Fit on Active PC*, and *Known Limitations*.

5. **Side-by-Side Multi-Application Comparison**:
   - Compare up to 3 applications simultaneously.
   - Matrix includes Pricing, Free tier availability, Minimum & Recommended specs, Live PC compatibility, Supported OS, Target Audience, and Features.

6. **My PC Hardware Profile & Presets**:
   - Interactive profile editor with instant 1-click test rigs (*Standard Test PC*, *Budget College Laptop*, *Mid-Tier Gaming Rig*, *Ultimate 3D Workstation*, *Older Office Desktop*).
   - LocalStorage persistence + SQLite database synchronization.

---

## 🛠️ Technology Stack

- **Backend**: Python 3 with **FastAPI**, **Pydantic** typed schemas, **Uvicorn** ASGI server.
- **Database**: **SQLite** (`appvault.db`) with automatic table creation and 34-app seed database.
- **Frontend**: Clean Vanilla JavaScript SPA with reactive state management.
- **Styling**: **Tailwind CSS** with custom dark charcoal dashboard theme (`#0B0F17`) and purple/cyan neon accents (`custom.css`).
- **Icons & Typography**: **Lucide Icons**, Google Fonts (*Outfit* and *Plus Jakarta Sans*).

---

## 🚀 How to Run the Project Locally

### Prerequisites
- Python 3.10+ installed on your system.

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Launch the Application
You can run the application with any of the following methods:

**Method A: Python Launcher (Recommended)**
```bash
python run.py
```

**Method B: Windows Batch Script**
Double-click `start.bat` in the root folder.

**Method C: Direct Uvicorn Command**
```bash
uvicorn backend.app.main:app --host 127.0.0.1 --port 8000 --reload
```

### 3. Open in Browser
Visit: **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 📁 Project Structure

```
ai adv project/
├── backend/
│   └── app/
│       ├── __init__.py
│       ├── main.py                  # FastAPI application routes & static mounts
│       ├── database.py              # SQLite connection, seeding, search queries
│       ├── models.py                # Pydantic schemas (App, Profile, Compatibility)
│       ├── compatibility.py         # Deterministic PC hardware evaluator
│       ├── hardware_benchmarks.py   # CPU & GPU normalized benchmark score tiers
│       ├── seed_data.py             # 34 curated apps with verified specs & INR pricing
│       └── ai_recommender.py        # Natural language query parser & recommender
├── frontend/
│   ├── index.html                   # Semantic HTML5 dark layout with Lucide & Tailwind
│   └── static/
│       ├── css/
│       │   └── custom.css           # Glassmorphism, glow accents, scrollbars
│       └── js/
│           └── app.js               # Reactive SPA router, modals, compare tray, client sync
├── run.py                           # Console-safe launcher script
├── start.bat                        # Double-click Windows batch launcher
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment template
└── README.md                        # Documentation
```

---

## 🔒 Security & Data Integrity
- No hardcoded secret API keys in frontend code.
- Rule-based AI recommendation fallback runs locally on the server without mandatory external LLM subscriptions.
- Deterministic compatibility engine prevents hallucinated hardware capabilities.
