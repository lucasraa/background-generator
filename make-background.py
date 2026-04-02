import os
import glob
import json
from PIL import Image, ImageDraw
import requests
from io import BytesIO

# ---------- KONFIG ----------
BACKGROUND_IMAGE = "background.png"  # eller URL
JSON_CONFIG = "config.json"
OUTPUT_IMAGE = "output.png"

# ---------- LOAD BAGGRUND ----------
def find_background_image():
    candidates = []
    for ext in ("*.png", "*.jpg", "*.jpeg"):
        candidates.extend(glob.glob(ext))

    candidates = [c for c in candidates if os.path.basename(c).lower() != OUTPUT_IMAGE.lower()]

    # Prefer configured background if it exists and is valid
    if os.path.isfile(BACKGROUND_IMAGE) and os.path.basename(BACKGROUND_IMAGE).lower() != OUTPUT_IMAGE.lower():
        return BACKGROUND_IMAGE

    for c in candidates:
        if os.path.isfile(c):
            return c

    return None


def load_background(source):
    if source is None:
        return None

    if source.startswith("http"):
        response = requests.get(source)
        return Image.open(BytesIO(response.content)).convert("RGBA")
    else:
        return Image.open(source).convert("RGBA")

# ---------- LOAD JSON ----------
def load_config(path):
    with open(path, "r") as f:
        return json.load(f)

# ---------- TEGN BOKSE ----------
def draw_boxes(image, config):
    overlay = Image.new("RGBA", image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    global_border_only = config.get("border-only", False)

    for box in config["boxes"]:
        x = box["x"]
        y = box["y"]
        w = box["width"]
        h = box["height"]
        color = tuple(box["color"])

        # Per-box override, falls back to global setting
        border_only = box.get("border-only", global_border_only)

        if border_only:
            draw.rectangle([x, y, x + w, y + h], outline=color, width=3)
        else:
            draw.rectangle([x, y, x + w, y + h], fill=color)

    return Image.alpha_composite(image, overlay)

# ---------- GRATIS BILLEDE GENERERING ----------
def generate_background(prompt):
    # GRATIS placeholder API (kan skiftes ud)
    url = f"https://picsum.photos/1920/1080"
    response = requests.get(url)
    return Image.open(BytesIO(response.content)).convert("RGBA")

# ---------- MAIN ----------
def main():
    config = load_config(JSON_CONFIG)

    # Check if random background is enabled
    use_random = config.get("random-background", False)

    if use_random:
        print("Genererer tilfældig baggrund...")
        image = generate_background("abstract background")
    else:
        # Brug lokalt billede (baggrund.png eller andet *.png/jpg i scriptmappe) eller genereret
        bg_source = find_background_image()
        if bg_source:
            try:
                image = load_background(bg_source)
            except Exception as e:
                print(f"Kunne ikke loade baggrund '{bg_source}' ({e}) – genererer en ny...")
                image = generate_background("abstract background")
        else:
            print("Ingen baggrundsfiler i scriptmappen, genererer en ny...")
            image = generate_background("abstract background")

    image = image.resize((1920, 1080))

    result = draw_boxes(image, config)

    result.save(OUTPUT_IMAGE)
    print(f"Gemte billede som {OUTPUT_IMAGE}")

if __name__ == "__main__":
    main()