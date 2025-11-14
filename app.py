import os
import base64
from flask import Flask, render_template

app = Flask(__name__, static_folder='assets')

CURRENT_DIR = os.path.join(app.static_folder, 'images', 'current')
PLACEHOLDER_B64 = (
    'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR4nGP4z8DwHwAFgwJ/lJkC7QAAAABJRU5ErkJggg=='
)  # 1x1 PNG

def ensure_placeholder():
    os.makedirs(CURRENT_DIR, exist_ok=True)
    # If no image files present, create placeholder.png
    if not any(f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')) for f in os.listdir(CURRENT_DIR)):
        data = base64.b64decode(PLACEHOLDER_B64)
        with open(os.path.join(CURRENT_DIR, 'placeholder.png'), 'wb') as fh:
            fh.write(data)

ensure_placeholder()

@app.route('/')
def index():
    files = [f for f in os.listdir(CURRENT_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp'))]
    files.sort()
    image = files[0] if files else None
    return render_template('index.html', image_filename=image)

if __name__ == '__main__':
    app.run(debug=False)
