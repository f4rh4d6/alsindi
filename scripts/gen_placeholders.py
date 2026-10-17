#!/usr/bin/env python3
"""Generate abstract placeholder 'photographs' for the portfolio site.
Each file in images/ is a stand-in; overwrite with real JPGs of the same name."""
import os

OUT = "assets/images"
os.makedirs(OUT, exist_ok=True)

INK = "#1C1B18"
ORANGE = "#D9480F"

GRAIN_DEF = (
    '<defs><filter id="g" x="0" y="0" width="100%" height="100%">'
    '<feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="2" stitchTiles="stitch"/>'
    '<feColorMatrix type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0.05 0"/>'
    '</filter></defs>'
)

def svg(w, h, body):
    grain = f'<rect width="{w}" height="{h}" filter="url(#g)" opacity="0.55"/>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'preserveAspectRatio="xMidYMid slice">{GRAIN_DEF}{body}{grain}</svg>')

def grad(w, h, top, bottom, gid="sky"):
    return (f'<defs><linearGradient id="{gid}" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{top}"/><stop offset="1" stop-color="{bottom}"/>'
            f'</linearGradient></defs><rect width="{w}" height="{h}" fill="url(#{gid})"/>')

def write(name, w, h, body):
    with open(os.path.join(OUT, name), "w") as f:
        f.write(svg(w, h, body))
    print("wrote", name)

# ---------- hero: monumental facade ----------
w, h = 2400, 1400
b = [grad(w, h, "#E7E4DC", "#C7C3B8")]
b.append(f'<circle cx="1850" cy="400" r="185" fill="#F4EFE2" opacity="0.9"/>')
for i in range(14):  # distant skyline
    bw = 90 + (i * 53) % 160
    b.append(f'<rect x="{i * 190}" y="{640 - (i * 37) % 180}" width="{bw}" height="560" fill="#B4AFA3" opacity="0.75"/>')
b.append(f'<rect x="560" y="380" width="1400" height="840" fill="#23211C"/>')  # main slab
cols, rows = 16, 10
cw, ch = (1280 - 15 * 24) / cols, (700 - 9 * 24) / rows
for r in range(rows):
    for c in range(cols):
        x = 620 + c * (cw + 24); y = 440 + r * (ch + 24)
        k = (r * 7 + c * 13) % 29
        fill = "#100F0C"
        op = ""
        if k == 0:
            fill, op = ORANGE, ' opacity="0.95"'
        elif k in (5, 17):
            fill, op = "#E9D9A8", ' opacity="0.85"'
        b.append(f'<rect x="{x:.0f}" y="{y:.0f}" width="{cw:.0f}" height="{ch:.0f}" fill="{fill}"{op}/>')
b.append('<polygon points="560,380 1960,380 1960,720 560,940" fill="#000000" opacity="0.16"/>')
b.append(f'<rect x="0" y="1220" width="{w}" height="180" fill="#6E6A60"/>')
b.append(f'<rect x="150" y="1180" width="220" height="46" fill="{ORANGE}"/>')  # barrier on ground
b.append(f'<rect x="150" y="1180" width="220" height="10" fill="#1C1B18" opacity="0.35"/>')
write("hero.svg", w, h, "".join(b))

# ---------- 01 housing block ----------
w, h = 1600, 1200
b = [grad(w, h, "#E5E2D9", "#C9C4B7")]
b.append(f'<rect x="180" y="240" width="1240" height="880" fill="#D9D3C4"/>')
for band in range(3):
    y0 = 280 + band * 280
    b.append(f'<rect x="180" y="{y0 - 14}" width="1240" height="14" fill="#B9B2A1" opacity="0.7"/>')
    for r in range(3):
        for c in range(9):
            x = 240 + c * 132; y = y0 + r * 78
            fill = "#26241F"; op = ""
            k = (band * 31 + r * 7 + c * 11) % 27
            if k == 3: fill, op = ORANGE, ' opacity="0.95"'
            elif k in (9, 21): fill, op = "#EFE6C8", ' opacity="0.9"'
            b.append(f'<rect x="{x}" y="{y}" width="86" height="56" rx="2" fill="{fill}"{op}/>')
b.append(f'<rect x="0" y="1120" width="{w}" height="80" fill="#57534B"/>')
write("01-housing-block.svg", w, h, "".join(b))

# ---------- 02 horizon line ----------
w, h = 1600, 1200
b = [f'<rect width="{w}" height="560" fill="#E5E2DA"/>',
     f'<circle cx="1180" cy="470" r="90" fill="#F2ECDD"/>',
     f'<rect y="560" width="{w}" height="80" fill="#C3BEB1"/>',
     f'<rect y="640" width="{w}" height="80" fill="#A39D8E"/>',
     f'<rect y="720" width="{w}" height="280" fill="#7F7A6C"/>',
     f'<rect y="1000" width="{w}" height="200" fill="#5F5A4E"/>',
     f'<rect y="634" width="{w}" height="6" fill="{ORANGE}"/>']
for i in range(9):
    b.append(f'<rect x="{i * 190}" y="760" width="120" height="8" fill="#6E695C" opacity="0.6"/>')
write("02-horizon-line.svg", w, h, "".join(b))

# ---------- 03 scaffold ----------
w, h = 1600, 1200
b = [f'<rect width="{w}" height="{h}" fill="#ECE9E1"/>']
for i in range(-4, 18):
    x0 = i * 120
    stroke, sw = "#2A2822", "6"
    if i == 5: stroke, sw = ORANGE, "14"
    b.append(f'<line x1="{x0 - 400}" y1="1300" x2="{x0 + 400}" y2="-100" stroke="{stroke}" stroke-width="{sw}"/>')
for i in range(6):
    x = 200 + i * 240
    b.append(f'<line x1="{x}" y1="200" x2="{x + 160}" y2="420" stroke="#2A2822" stroke-width="5"/>')
    b.append(f'<line x1="{x + 160}" y1="200" x2="{x}" y2="420" stroke="#2A2822" stroke-width="5"/>')
b.append(f'<rect x="240" y="820" width="560" height="26" fill="#2A2822" transform="rotate(-18 520 833)"/>')
write("03-scaffold.svg", w, h, "".join(b))

# ---------- 04 viaduct ----------
w, h = 1600, 1200
b = [grad(w, h, "#E3DFD6", "#CBC5B8")]
b.append(f'<rect x="0" y="560" width="{w}" height="44" fill="#26241F"/>')
for i in range(6):
    x = 90 + i * 250
    b.append(f'<path d="M{x} 1200 L{x} 700 A80 80 0 0 1 {x + 160} 700 L{x + 160} 1200" '
             f'stroke="#26241F" stroke-width="36" fill="none"/>')
b.append(f'<rect x="620" y="530" width="52" height="30" fill="{ORANGE}"/>')  # small vehicle on deck
b.append(f'<rect x="0" y="1120" width="{w}" height="80" fill="#8A857A"/>')
write("04-viaduct.svg", w, h, "".join(b))

# ---------- 05 field curves ----------
w, h = 1600, 1200
b = [grad(w, h, "#E8E5DC", "#D2CDBF")]
hills = [
    (560, "#9AA18C", "M0,700 C300,560 500,640 800,580 C1100,520 1350,620 1600,560 L1600,1200 L0,1200 Z"),
    (700, "#7E8672", "M0,780 C260,700 520,780 820,720 C1120,660 1380,760 1600,700 L1600,1200 L0,1200 Z"),
    (840, "#B08D68", "M0,900 C320,830 600,910 900,860 C1200,810 1400,900 1600,860 L1600,1200 L0,1200 Z"),
    (1000, "#6B6E66", "M0,1020 C340,950 660,1030 960,980 C1260,930 1440,1010 1600,980 L1600,1200 L0,1200 Z"),
]
for y, col, d in hills:
    b.append(f'<path d="{d}" fill="{col}"/>')
b.append(f'<path d="M0,900 C320,830 600,910 900,860 C1200,810 1400,900 1600,860" '
         f'stroke="{ORANGE}" stroke-width="5" fill="none" opacity="0.9"/>')
write("05-field-curves.svg", w, h, "".join(b))

# ---------- 06 facade, morning ----------
w, h = 1600, 1200
b = [f'<rect width="{w}" height="{h}" fill="#DCD7CA"/>']
mw, mh, gx, gy = 128, 128, 18, 18
x0, y0 = 90, 110
for r in range(7):
    for c in range(10):
        x = x0 + c * (mw + gx); y = y0 + r * (mh + gy)
        k = (r * 5 + c * 9) % 23
        fill, op = "#E4E0D5", ""
        if k in (2, 12, 19): fill, op = "#C9C4B6", ""
        elif k in (7, 16): fill, op = "#26241F", ""
        if c >= 7 and r >= 4:  # orange cluster lower-right
            fill, op = ORANGE, ' opacity="0.92"'
        b.append(f'<rect x="{x}" y="{y}" width="{mw}" height="{mh}" fill="{fill}"{op}/>')
b.append('<polygon points="0,0 700,0 200,1200 0,1200" fill="#FFFFFF" opacity="0.14"/>')
write("06-facade-morning.svg", w, h, "".join(b))

# ---------- 07 tower in fog (portrait) ----------
w, h = 1200, 1600
b = [grad(w, h, "#E8E5DE", "#B4AFA2")]
b.append(f'<rect x="430" y="200" width="340" height="1260" fill="#211F1A"/>')
for r in range(16):
    for c in range(4):
        k = (r * 3 + c * 5) % 11
        if k in (1, 6):
            b.append(f'<rect x="{470 + c * 70}" y="{260 + r * 72}" width="34" height="26" fill="#E9D9A8" opacity="0.55"/>')
b.append(f'<circle cx="600" cy="170" r="46" fill="{ORANGE}" opacity="0.18"/>')
b.append(f'<circle cx="600" cy="170" r="14" fill="{ORANGE}"/>')
for i, (bx, by) in enumerate([(240, 420), (300, 480), (880, 360)]):
    b.append(f'<path d="M{bx},{by} q 10 -10 20 0 q 10 -10 20 0" stroke="#2A2822" stroke-width="5" fill="none"/>')
write("07-tower-fog.svg", w, h, "".join(b))

# ---------- 08 coast, low tide ----------
w, h = 1600, 1200
b = [f'<rect width="{w}" height="600" fill="#E6E2D8"/>',
     f'<circle cx="800" cy="600" r="95" fill="{ORANGE}"/>',
     f'<rect y="600" width="{w}" height="320" fill="#5F6E72"/>',
     f'<rect y="920" width="{w}" height="280" fill="#C9BFA9"/>']
for i in range(12):
    y = 640 + i * 24
    b.append(f'<rect x="{120 + (i * 97) % 300}" y="{y}" width="{700 - i * 30}" height="4" fill="#7E8B8E" opacity="0.7"/>')
b.append(f'<rect x="792" y="695" width="16" height="225" fill="{ORANGE}" opacity="0.35"/>')
for fx in (560, 640):  # two figures
    b.append(f'<circle cx="{fx}" cy="880" r="14" fill="#26241F"/>')
    b.append(f'<rect x="{fx - 5}" y="894" width="10" height="70" fill="#26241F"/>')
write("08-coast.svg", w, h, "".join(b))

# ---------- 09 stairwell (portrait) ----------
w, h = 1200, 1600
b = [f'<rect width="{w}" height="{h}" fill="#E9E6DE"/>']
for i in range(8):
    x = 120 + i * 130; y = 1380 - i * 150
    shade = ["#E1DDD3", "#D6D1C5"][i % 2]
    b.append(f'<polygon points="{x},{y} {x + 260},{y - 60} {x + 260},{y + 40} {x},{y + 100}" fill="{shade}" stroke="#2A2822" stroke-width="5"/>')
    if i == 4:
        b.append(f'<line x1="{x}" y1="{y}" x2="{x + 260}" y2="{y - 60}" stroke="{ORANGE}" stroke-width="10"/>')
b.append(f'<line x1="120" y1="1480" x2="1030" y2="280" stroke="#2A2822" stroke-width="8"/>')
for i in range(6):
    t = i / 5
    b.append(f'<line x1="{120 + 910 * t:.0f}" y1="{1480 - 1200 * t:.0f}" x2="{120 + 910 * t:.0f}" y2="{1540 - 1200 * t:.0f}" stroke="#2A2822" stroke-width="6"/>')
write("09-stairwell.svg", w, h, "".join(b))

# ---------- 10 billboard (commentary, dusk) ----------
w, h = 1600, 1200
b = [grad(w, h, "#3A362F", "#6B6257", "dusk")]
for i in range(11):
    bw = 100 + (i * 67) % 120
    bh = 300 + (i * 91) % 380
    b.append(f'<rect x="{i * 150}" y="{1050 - bh}" width="{bw}" height="{bh}" fill="#191713"/>')
    for r in range(3):
        for c in range(2):
            if (i * 7 + r * 3 + c) % 5 == 0:
                b.append(f'<rect x="{i * 150 + 18 + c * 40}" y="{1050 - bh + 30 + r * 60}" width="22" height="30" fill="#E9D9A8" opacity="0.8"/>')
b.append(f'<rect x="420" y="180" width="760" height="420" fill="{ORANGE}"/>')
b.append(f'<rect x="470" y="300" width="660" height="180" fill="#EFEDE7"/>')
b.append(f'<rect x="470" y="330" width="420" height="26" fill="#1C1B18"/>')
b.append(f'<rect x="470" y="380" width="560" height="14" fill="#1C1B18" opacity="0.6"/>')
b.append(f'<rect x="760" y="600" width="40" height="450" fill="#191713"/>')
write("10-billboard.svg", w, h, "".join(b))

# ---------- 11 forest edge ----------
w, h = 1600, 1200
b = [grad(w, h, "#E4E1D8", "#A9A496")]
for i in range(22):
    x = i * 76 + (i * 31) % 40
    tw = 12 + (i * 17) % 30
    th = 500 + (i * 83) % 420
    b.append(f'<rect x="{x}" y="{1050 - th}" width="{tw}" height="{th}" fill="#2B2925" opacity="0.85"/>')
b.append(f'<rect x="0" y="1000" width="{w}" height="200" fill="#3A382F" opacity="0.5"/>')
b.append(f'<rect x="0" y="940" width="{w}" height="70" fill="{ORANGE}" opacity="0.22"/>')
for i in range(5):
    b.append(f'<circle cx="{200 + i * 300}" cy="975" r="10" fill="{ORANGE}" opacity="0.55"/>')
write("11-forest-edge.svg", w, h, "".join(b))

# ---------- 12 perimeter (commentary) ----------
w, h = 1600, 1200
b = [grad(w, h, "#D8D4C9", "#A8A394")]
for i, (x, y, rw, rh, col) in enumerate([(60, 300, 420, 500, "#8E897D"), (560, 180, 500, 640, "#7E796C"), (1120, 360, 400, 520, "#979285")]):
    b.append(f'<rect x="{x}" y="{y}" width="{rw}" height="{rh}" fill="{col}" opacity="0.55"/>')
b.append(f'<defs><pattern id="fence" width="46" height="46" patternUnits="userSpaceOnUse">'
         f'<path d="M0,46 L46,0 M0,0 L46,46" stroke="#26241F" stroke-width="3"/></pattern></defs>')
b.append(f'<rect x="0" y="240" width="{w}" height="720" fill="url(#fence)" opacity="0.9"/>')
b.append(f'<defs><pattern id="haz" width="60" height="60" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         f'<rect width="30" height="60" fill="{ORANGE}"/><rect x="30" width="30" height="60" fill="#26241F"/></pattern></defs>')
b.append(f'<rect x="0" y="1040" width="{w}" height="160" fill="url(#haz)"/>')
b.append(f'<circle cx="800" cy="900" r="16" fill="#1C1B18"/>')
b.append(f'<rect x="793" y="916" width="14" height="90" fill="#1C1B18"/>')
write("12-perimeter.svg", w, h, "".join(b))

# ---------- portrait placeholder ----------
w, h = 1200, 1500
b = [grad(w, h, "#E8E5DD", "#C6C0B2")]
b.append(f'<circle cx="600" cy="560" r="175" fill="#23211C"/>')
b.append(f'<path d="M240,1500 C240,1080 420,940 600,940 C780,940 960,1080 960,1500 Z" fill="#23211C"/>')
b.append(f'<path d="M745,420 A175,175 0 0 1 700,700" stroke="{ORANGE}" stroke-width="12" fill="none" opacity="0.9"/>')
b.append(f'<path d="M820,1080 A330,330 0 0 1 700,1330" stroke="{ORANGE}" stroke-width="10" fill="none" opacity="0.55"/>')
write("portrait.svg", w, h, "".join(b))

print("done")
