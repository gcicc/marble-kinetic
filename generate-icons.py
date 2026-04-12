"""Generate PWA icons for Kinetic marble machine."""
try:
    from PIL import Image, ImageDraw
except ImportError:
    import subprocess, sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageDraw
from pathlib import Path

SIZES = {"icon-180.png": 180, "icon-192.png": 192, "icon-512.png": 512}
BG = (26, 21, 16)
BRASS = (196, 160, 80)
BALL = (212, 168, 67)

out = Path(__file__).parent
for fname, size in SIZES.items():
    img = Image.new("RGBA", (size, size), BG + (255,))
    draw = ImageDraw.Draw(img)
    cx, cy = size//2, size//2
    # Gear-like outer ring
    m = size//6
    draw.ellipse([m, m, size-m, size-m], outline=BRASS+(80,), width=max(2, size//50))
    # Ramp lines
    draw.line([(size*0.2, size*0.3), (size*0.7, size*0.45)], fill=BRASS+(120,), width=max(2, size//60))
    draw.line([(size*0.8, size*0.55), (size*0.3, size*0.7)], fill=BRASS+(120,), width=max(2, size//60))
    # Ball
    r = size//10
    draw.ellipse([cx-r, size//4-r, cx+r, size//4+r], fill=BALL+(220,))
    img.save(out / fname)
    print(f"  {fname} ({size}x{size})")
print("Done.")
