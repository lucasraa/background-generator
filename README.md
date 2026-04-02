# Background Generator

Automatically generate and set custom Windows desktop backgrounds with configurable overlays.

## Features

✨ **Auto Background Detection**
- Automatically finds and loads any `.png` or `.jpg/.jpeg` in the script folder
- Fallback to random generated images if no local images found

🎨 **Customizable Boxes**
- Draw solid or border-only rectangles on your background
- Configure position, size, color, and transparency per box
- Per-box border-only setting

🔄 **Flexible Configuration**
- All settings in `config.json` — no code editing needed
- Toggle between local images and random generation
- Easy color and transparency adjustment
- Configurable box positioning

💻 **Windows Integration**
- Automatically sets generated image as Windows wallpaper
- Dual-method wallpaper update (Registry + VBScript fallback)
- Runs from a single batch file

## Prerequisites

### Required
- **Python 3.6+**
- **Windows OS** (for wallpaper setting)

### Python Packages
```bash
pip install Pillow requests
```

Or install from `requirements.txt` (if available):
```bash
pip install -r requirements.txt
```

## Installation

1. Clone or download this repository
2. Install Python 3 from [python.org](https://www.python.org)
3. Install required packages:
   ```bash
   pip install Pillow requests
   ```
4. Place background images (`.png` or `.jpg`) in the script folder *(optional)*

## Quick Start

### 1. Configure Your Boxes

Edit `config.json`:

```json
{
  "random-background": false,
  "boxes": [
    {
      "name": "top_box",
      "x": 0,
      "y": 0,
      "width": 960,
      "height": 300,
      "color": [128, 0, 128, 120],
      "border-only": false
    },
    {
      "name": "bottom_border",
      "x": 960,
      "y": 600,
      "width": 960,
      "height": 400,
      "color": [255, 0, 0, 200],
      "border-only": true
    }
  ]
}
```

**Config Options:**

| Field | Type | Description |
|-------|------|-------------|
| `random-background` | bool | If `true`, generates a random image; if `false`, uses local image |
| `boxes[].name` | string | Description (for reference) |
| `boxes[].x` | int | X position (pixels from left) |
| `boxes[].y` | int | Y position (pixels from top) |
| `boxes[].width` | int | Box width in pixels |
| `boxes[].height` | int | Box height in pixels |
| `boxes[].color` | [R,G,B,A] | RGBA color (0-255 each) |
| `boxes[].border-only` | bool | If `true`, draws only outline; if `false`, fills box |

### 2. Add Background Image *(Optional)*

Place any `.png` or `.jpg` file in the script folder. For example:
- `background.png`
- `myimage.jpg`

The script will automatically use the first image found. To force random generation, set `"random-background": true` in `config.json`.

### 3. Run the Script

**Option A: Using Batch File** (Easiest)
```bash
.\set-background.bat
```

This will:
1. Run the Python script to generate the image
2. Set it as your Windows wallpaper
3. Display success message

**Option B: Python Only**
```bash
python make-background.py
```

This generates `output.png` but does not set it as wallpaper.

## Project Structure

```
background-generator/
├── README.md                 # This file
├── config.json               # Configuration for boxes
├── make-background.py        # Main Python script
├── set-background.bat        # Batch runner (sets wallpaper)
├── output.png                # Generated background (auto-created)
├── delete.bat                # Clean up all .png/.jpg/.jpeg images
├── install.bat               # Install script to get started
└── background.png            # (Optional) Your background image
```

## Configuration Examples

### Example 1: Simple Border Frame

```json
{
  "random-background": false,
  "boxes": [
    {
      "name": "border_frame",
      "x": 100,
      "y": 100,
      "width": 1720,
      "height": 880,
      "color": [255, 255, 255, 150],
      "border-only": true
    }
  ]
}
```

### Example 2: Semi-Transparent Overlays

```json
{
  "random-background": true,
  "boxes": [
    {
      "name": "top_overlay",
      "x": 0,
      "y": 0,
      "width": 1920,
      "height": 400,
      "color": [0, 0, 0, 100],
      "border-only": false
    },
    {
      "name": "bottom_overlay",
      "x": 0,
      "y": 600,
      "width": 1920,
      "height": 480,
      "color": [0, 0, 0, 100],
      "border-only": false
    }
  ]
}
```

## Troubleshooting

### Wallpaper Not Updating

- Run `set-background.bat` instead of the Python script directly
- Ensure `output.png` exists in the script folder
- Try manually setting the wallpaper: Right-click `output.png` → Set as desktop background

### Python Module Not Found

```bash
pip install Pillow requests
```

### Image Quality Issues

- Use PNG for best quality and transparency support
- Ensure background image is at least 1920x1080 resolution
- Check color values are in range 0-255

### Batch File Doesn't Work

- Run as Administrator: Right-click `set-background.bat` → Run as Administrator
- Check Python is installed: `python --version` in PowerShell

## Color Reference (RGBA)

- **Red**: `[255, 0, 0, 255]`
- **Green**: `[0, 255, 0, 255]`
- **Blue**: `[0, 0, 255, 255]`
- **White**: `[255, 255, 255, 255]`
- **Black**: `[0, 0, 0, 255]`
- **Semi-transparent Black**: `[0, 0, 0, 128]`

The 4th value is **alpha** (transparency): `0` = fully transparent, `255` = fully opaque.

## Tips & Tricks

💡 **Layer Multiple Boxes**
Overlap boxes to create complex designs. Order in `config.json` determines draw order (bottom to top).

💡 **Use Border-Only for Minimalism**
Mix filled boxes with borders for modern designs:
```json
"border-only": true,  // Just the outline
```

💡 **High Transparency for Subtle Effects**
Low alpha values create subtle overlays:
```json
"color": [0, 0, 0, 30]  // Very subtle darkening
```

💡 **Automate with Task Scheduler**
Schedule `set-background.bat` in Windows Task Scheduler to update backgrounds daily.

## License

Feel free to use and modify this project.

## Contributing

Suggestions and improvements welcome!

---

**Made with ❤️ for Windows desktop customization**
