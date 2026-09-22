"""
Muskan Rajput — Cinematic Birthday Reel
----------------------------------------
Creates a 9:16 vertical birthday video in Python.

Put your photos in:
    photos/photo1.jpg
    photos/photo2.jpg
    photos/photo3.jpg
    ...

Optional music:
    music/birthday.mp3

Run:
    python birthday_muskan.py

The output is:
    output/muskan_birthday.mp4

This version uses OpenCV + Pillow, so it does not depend on MoviePy.
"""

from pathlib import Path
import math
import random
import subprocess
import shutil

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# -------------------- SETTINGS --------------------
NAME = "MUSKAN RAJPUT"
WIDTH, HEIGHT = 1080, 1920
FPS = 30
TOTAL_SECONDS = 33
OUT = Path("output/muskan_birthday_no_music.mp4")
FINAL = Path("output/muskan_birthday.mp4")
MUSIC = Path("music/birthday.mp3")

# Put photo1.jpg, photo2.jpg, photo3.jpg in the SAME folder as birthday.py.
HERE = Path(__file__).resolve().parent
PHOTOS = []
for pattern in ("*.jpg", "*.jpeg", "*.png", "*.JPG", "*.JPEG", "*.PNG"):
    PHOTOS.extend(HERE.glob(pattern))
PHOTOS = sorted(set(PHOTOS))

MESSAGES = [
    "Happy birthday to the love of my life!",
    "Every moment with you feels like a dream come true.",
    "You light up my world with your laugh, your love,",
    "and your beautiful soul. Have the best day ever.",
    "I didn't know what I was missing until I met you.",
    "You make my life warmer and a thousand times happier.",
    "As you blow out your candles, know that you aren't",
    "just making a wish — you already fulfilled all of mine."
]

# A clean font is easier to find on most systems.
FONT_CANDIDATES = [
    "C:/Windows/Fonts/arial.ttf",
    "C:/Windows/Fonts/ARLRDBD.TTF",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]

def font(size, bold=False):
    candidates = [
        "C:/Windows/Fonts/arialbd.ttf" if bold else "C:/Windows/Fonts/arial.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for f in candidates:
        if Path(f).exists():
            return ImageFont.truetype(f, size)
    return ImageFont.load_default()

FONT_SMALL = font(42)
FONT_MED = font(60)
FONT_BIG = font(100, True)
FONT_NAME = font(88, True)
FONT_HUGE = font(118, True)

def ease(t):
    """Smooth 0..1 easing."""
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)

def fit_crop(im, size, zoom=1.0, focus=(0.5, 0.5)):
    """Crop an image to 9:16 while applying a gentle zoom."""
    target_w, target_h = size
    im = im.convert("RGB")
    iw, ih = im.size

    target_ratio = target_w / target_h
    ratio = iw / ih

    if ratio > target_ratio:
        # Wider than target: crop width.
        new_w = int(ih * target_ratio)
        left = int((iw - new_w) * focus[0])
        left = max(0, min(left, iw - new_w))
        im = im.crop((left, 0, left + new_w, ih))
    else:
        # Taller than target: crop height.
        new_h = int(iw / target_ratio)
        top = int((ih - new_h) * focus[1])
        top = max(0, min(top, ih - new_h))
        im = im.crop((0, top, iw, top + new_h))

    if zoom != 1.0:
        nw = int(target_w * zoom)
        nh = int(target_h * zoom)
        im = im.resize((nw, nh), Image.Resampling.LANCZOS)
        left = (nw - target_w) // 2
        top = (nh - target_h) // 2
        im = im.crop((left, top, left + target_w, top + target_h))
    else:
        im = im.resize((target_w, target_h), Image.Resampling.LANCZOS)

    return im

def gradient_overlay(size, alpha=100):
    """Soft dark gradient for readable cinematic text."""
    w, h = size
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    px = layer.load()
    for y in range(h):
        # Stronger at bottom.
        a = int(alpha * (y / h) ** 2)
        for x in range(w):
            px[x, y] = (0, 0, 0, a)
    return layer

def add_glow_text(base, text, y, fnt, fill=(255,255,255,255), glow=(255,180,220,150)):
    """Draw text with a soft glow."""
    w, h = base.size
    bbox = ImageDraw.Draw(base).textbbox((0,0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    x = (w - tw) // 2

    glow_layer = Image.new("RGBA", base.size, (0,0,0,0))
    gd = ImageDraw.Draw(glow_layer)
    gd.text((x, y), text, font=fnt, fill=glow, stroke_width=3, stroke_fill=glow)
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(18))
    base.alpha_composite(glow_layer)

    d = ImageDraw.Draw(base)
    d.text((x, y), text, font=fnt, fill=fill,
           stroke_width=2, stroke_fill=(30, 20, 30, 210))
    return base

def draw_centered(draw, text, y, fnt, fill, stroke=0):
    box = draw.textbbox((0,0), text, font=fnt, stroke_width=stroke)
    x = (WIDTH - (box[2]-box[0])) // 2
    draw.text((x, y), text, font=fnt, fill=fill, stroke_width=stroke,
              stroke_fill=(20, 15, 25, 230) if stroke else None)

def add_particles(img, t, seed=10):
    """Floating sparkles/hearts/confetti."""
    random.seed(seed)
    layer = Image.new("RGBA", img.size, (0,0,0,0))
    d = ImageDraw.Draw(layer)

    for i in range(55):
        x0 = random.randint(30, WIDTH-30)
        speed = random.uniform(20, 80)
        y = (HEIGHT - ((t * speed * 18 + i*97) % (HEIGHT + 200)))
        size = random.choice([3,4,5,7,9])
        alpha = random.randint(70, 180)
        if i % 7 == 0:
            # tiny heart
            d.text((x0, y), "♥", font=font(max(18,size*4), True),
                   fill=(255, 170, 205, alpha))
        else:
            d.ellipse((x0, y, x0+size, y+size), fill=(255, 240, 250, alpha))
    return Image.alpha_composite(img, layer)

def text_fade(text, local_t, duration=2.0):
    """Opacity that fades in then gently fades out."""
    if local_t < 0:
        return 0
    fade_in = min(1.0, local_t / 0.45)
    fade_out = min(1.0, max(0.0, (duration - local_t) / 0.45))
    return int(255 * min(fade_in, fade_out))

def scene(frame_no, photo_imgs):
    t = frame_no / FPS

    # Timeline:
    # 0-4   intro
    # 4-9   photo 1
    # 9-14  photo 2
    # 14-19 photo 3
    # 19-26 message sequence
    # 26-33 final birthday reveal

    if t < 4:
        bg = Image.new("RGBA", (WIDTH, HEIGHT), (12, 8, 16, 255))
        # subtle moving light
        overlay = Image.new("RGBA", (WIDTH, HEIGHT), (0,0,0,0))
        od = ImageDraw.Draw(overlay)
        cx = int(WIDTH * (0.35 + 0.25*math.sin(t*0.8)))
        cy = int(HEIGHT * (0.30 + 0.08*math.cos(t*0.7)))
        od.ellipse((cx-420, cy-420, cx+420, cy+420), fill=(255,150,205,45))
        overlay = overlay.filter(ImageFilter.GaussianBlur(130))
        bg.alpha_composite(overlay)
        bg = add_particles(bg, t, 77)

        a = int(255 * ease(min(t/1.2, 1)))
        d = ImageDraw.Draw(bg)
        draw_centered(d, "A LITTLE SURPRISE", 690, FONT_MED, (255,255,255,a))
        draw_centered(d, "FOR SOMEONE SPECIAL", 770, FONT_SMALL, (255,190,220,a))
        return bg.convert("RGB")

    if t < 9:
        idx, start = 0, 4
    elif t < 14:
        idx, start = 1, 9
    elif t < 19:
        idx, start = 2, 14
    else:
        idx, start = 2, 19

    if t < 19:
        local = t - start
        zoom = 1.02 + 0.07 * ease((local % 5)/5)
        im = fit_crop(photo_imgs[idx], (WIDTH, HEIGHT), zoom=zoom,
                      focus=((0.45 + 0.04*math.sin(local)), 0.48))
        base = im.convert("RGBA")
        base = Image.alpha_composite(base, gradient_overlay((WIDTH, HEIGHT), 125))
        base = add_particles(base, t, idx+3)

        # small cinematic label
        d = ImageDraw.Draw(base)
        d.text((65, 150), "✨", font=font(50), fill=(255,255,255,210))
        d.text((65, 210), NAME, font=font(34, True), fill=(255,225,240,220))
        return base.convert("RGB")

    if t < 26:
        # Message montage on top of a blurred version of the third photo.
        bg = fit_crop(photo_imgs[2], (WIDTH, HEIGHT), zoom=1.12)
        bg = bg.filter(ImageFilter.GaussianBlur(7)).convert("RGBA")
        bg.alpha_composite(gradient_overlay((WIDTH, HEIGHT), 185))
        bg = add_particles(bg, t, 91)

        # Four short cards.
        idx = min(3, int((t - 19) / 1.75))
        lines = MESSAGES[idx*2:idx*2+2]
        if not lines:
            lines = MESSAGES[-2:]
        alpha = text_fade("", (t-19) % 1.75, 1.75)

        # translucent card
        card = Image.new("RGBA", (900, 440), (15,10,20,115))
        cd = ImageDraw.Draw(card)
        cd.rounded_rectangle((0,0,899,439), radius=38,
                             outline=(255,200,225,100), width=2)
        y = 95
        for line in lines:
            box = cd.textbbox((0,0), line, font=FONT_SMALL)
            x = (900 - (box[2]-box[0]))//2
            cd.text((x,y), line, font=FONT_SMALL, fill=(255,255,255,alpha))
            y += 90
        bg.alpha_composite(card, ((WIDTH-900)//2, 740))
        return bg.convert("RGB")

    # Final reveal.
    local = t - 26
    if local < 2.0:
        bg = Image.new("RGBA", (WIDTH, HEIGHT), (12, 7, 17, 255))
        bg = add_particles(bg, t, 120)
        a = int(255 * ease(local/1.3))
        draw_centered(ImageDraw.Draw(bg), "HAPPY BIRTHDAY", 600,
                      FONT_HUGE, (255,255,255,a), stroke=2)
        draw_centered(ImageDraw.Draw(bg), NAME, 760,
                      FONT_NAME, (255,185,220,a), stroke=2)
        draw_centered(ImageDraw.Draw(bg), "♥", 930, font(120, True),
                      (255,80,150,a))
        return bg.convert("RGB")

    # Photo finale with cinematic zoom + message.
    local2 = local - 2
    zoom = 1.0 + 0.10 * ease(min(local2/5,1))
    bg = fit_crop(photo_imgs[0], (WIDTH, HEIGHT), zoom=zoom, focus=(0.50,0.45)).convert("RGBA")
    bg.alpha_composite(gradient_overlay((WIDTH, HEIGHT), 155))
    bg = add_particles(bg, t, 121)

    d = ImageDraw.Draw(bg)
    draw_centered(d, "HAPPY BIRTHDAY", 1260, FONT_BIG, (255,255,255,255), stroke=2)
    draw_centered(d, NAME, 1390, FONT_NAME, (255,190,220,255), stroke=2)
    draw_centered(d, "You already fulfilled all of my wishes. ♥", 1545,
                  font(39, False), (255,245,250,245), stroke=1)
    return bg.convert("RGB")

def add_music(video_path, music_path, final_path):
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        print("\nFFmpeg was not found, so the video was created without music.")
        print("Install FFmpeg and run the mux command later if you want music.")
        return False

    cmd = [
        ffmpeg, "-y",
        "-i", str(video_path),
        "-stream_loop", "-1", "-i", str(music_path),
        "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k",
        "-shortest",
        str(final_path)
    ]
    subprocess.run(cmd, check=True)
    return True

def main():
    if not PHOTOS:
        raise FileNotFoundError(
        "No photos found. Put photo1.jpg, photo2.jpg and photo3.jpg "
        "in the same folder as birthday.py."
    )

    print(f"Found {len(PHOTOS)} photo(s). Creating {TOTAL_SECONDS}-second 9:16 reel...")

    photo_imgs = [Image.open(p).convert("RGB") for p in PHOTOS]
    # Repeat the last photo if fewer than 3 were supplied.
    while len(photo_imgs) < 3:
        photo_imgs.append(photo_imgs[-1].copy())

    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(str(OUT), fourcc, FPS, (WIDTH, HEIGHT))

    total_frames = TOTAL_SECONDS * FPS
    for n in range(total_frames):
        rgb = np.array(scene(n, photo_imgs))
        bgr = cv2.cvtColor(rgb, cv2.COLOR_RGB2BGR)
        writer.write(bgr)

        if n % FPS == 0:
            print(f"Rendering: {n//FPS:02d}/{TOTAL_SECONDS} sec")

    writer.release()
    print(f"\nVideo created: {OUT}")

    if MUSIC.exists():
        try:
            if add_music(OUT, MUSIC, FINAL):
                print(f"Final video with music: {FINAL}")
                return
        except Exception as e:
            print("Music could not be added:", e)

    shutil.copy2(OUT, FINAL)
    print(f"Final video without music: {FINAL}")

if __name__ == "__main__":
    main()