# dm-tools-battlemapp
A simple Flask app that serves the current image in `assets/images/current`.

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Then open `http://127.0.0.1:5000`.

## Updating the Displayed Image

Place a single image file (e.g. `map.png`, `scene.jpg`) inside `assets/images/current/`. The app will pick the first image found (alphabetical) and display it responsively. If none is present it creates a 1×1 placeholder.

Supported extensions: `png`, `jpg`, `jpeg`, `gif`, `webp`.
