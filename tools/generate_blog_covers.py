from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "assets" / "images" / "blog"
WIDTH, HEIGHT, SCALE = 1200, 630, 2
PAPER = (241, 234, 220)
INK = (24, 20, 15)
RED = (216, 32, 42)
MUTED = (108, 96, 79)
DARK = (31, 27, 21)

FONT_DIR = Path(r"C:\Windows\Fonts")
DISPLAY_FONT = FONT_DIR / "impact.ttf"
MONO_FONT = FONT_DIR / "consola.ttf"

COVERS = {
    "android-open": ("ANDROID / OPEN WEB", "KEEP ANDROID|OPEN", "phone", (216, 32, 42)),
    "local-first": ("LOCAL-FIRST / DATA", "YOUR DATA,|YOUR DEVICE", "sync", (76, 120, 91)),
    "minimal-software": ("SOFTWARE / DESIGN", "LESS SOFTWARE.|MORE FOCUS.", "window", (192, 112, 58)),
    "building-public": ("OPEN SOURCE / RELEASES", "BUILD IN|THE OPEN", "branch", (89, 108, 160)),
    "build-verification": ("ANDROID / TRUST", "VERIFY THE|BUILD", "shield", (65, 130, 113)),
    "image-optimization": ("WEB / PERFORMANCE", "LIGHTER IMAGES,|FASTER PAGES", "image", (198, 115, 53)),
    "digital-ownership": ("PRIVACY / OWNERSHIP", "OWN YOUR|WORKSPACE", "folder", (124, 95, 147)),
    "decap-local": ("JEKYLL / DECAP CMS", "WRITE LOCAL.|PUBLISH CLEARLY.", "editor", (64, 121, 147)),
    "android-roms": ("ANDROID / CHOICE", "KEEP YOUR|PHONE YOURS", "choice", (190, 68, 71)),
    "small-open-source": ("FOSS / DESIGN", "SMALL TOOLS.|CLEAR PURPOSE.", "tools", (83, 132, 90)),
    "technical-notes": ("WRITING / NOTES", "WRITE IT DOWN.|FIND IT LATER.", "notes", (136, 104, 75)),
    "static-sites": ("WEB / STATIC", "PAGES THAT|SHIP FAST", "static", (65, 117, 148)),
    "web-accessibility": ("WEB / ACCESSIBILITY", "DESIGN FOR|MORE PEOPLE", "access", (96, 121, 89)),
    "passkeys": ("WEB / SECURITY", "A BETTER WAY|TO SIGN IN", "key", (118, 96, 153)),
    "core-web-vitals": ("WEB / PERFORMANCE", "MEASURE WHAT|PEOPLE FEEL", "vitals", (202, 113, 53)),
    "http-caching": ("WEB / HTTP", "REUSE THE|RIGHT RESPONSE", "cache", (74, 112, 149)),
    "image-usage-rights": ("IMAGES / LICENSING", "SEARCH IS NOT|A LICENSE", "license", (161, 86, 80)),
}


def px(value):
    return int(value * SCALE)


def rectangle(draw, bounds, fill, outline=None, width=1):
    coords = tuple(px(value) for value in bounds)
    draw.rectangle(coords, fill=fill, outline=outline, width=px(width) if outline else 1)


def line(draw, points, fill, width=1):
    draw.line([(px(x), px(y)) for x, y in points], fill=fill, width=px(width))


def ellipse(draw, bounds, fill, outline=None, width=1):
    coords = tuple(px(value) for value in bounds)
    draw.ellipse(coords, fill=fill, outline=outline, width=px(width) if outline else 1)


def polygon(draw, points, fill):
    draw.polygon([(px(x), px(y)) for x, y in points], fill=fill)


def label(draw, x, y, value, size, color, font=DISPLAY_FONT, max_width=None):
    font_size = size
    typeface = ImageFont.truetype(str(font), px(font_size))
    while max_width and draw.textlength(value, font=typeface) / SCALE > max_width and font_size > 16:
        font_size -= 2
        typeface = ImageFont.truetype(str(font), px(font_size))
    draw.text((px(x), px(y)), value, font=typeface, fill=color)


def draw_phone(draw, motif, accent):
    rectangle(draw, (908, 184, 1058, 428), (13, 12, 10), PAPER, 4)
    rectangle(draw, (921, 202, 1045, 397), (47, 41, 31), (93, 81, 62), 2)
    ellipse(draw, (977, 407, 989, 419), PAPER)

    if motif == "phone":
        ellipse(draw, (962, 255, 1004, 297), accent)
        line(draw, [(983, 297), (983, 351)], PAPER, 7)
        polygon(draw, [(960, 340), (983, 365), (1006, 340)], accent)
    elif motif == "choice":
        label(draw, 947, 238, "OS", 32, PAPER, MONO_FONT)
        line(draw, [(940, 300), (1025, 300)], accent, 5)
        line(draw, [(940, 331), (1025, 331)], PAPER, 3)
        line(draw, [(940, 358), (1008, 358)], MUTED, 3)
    elif motif == "key":
        ellipse(draw, (954, 264, 1002, 312), None, accent, 7)
        line(draw, [(994, 306), (1031, 343)], accent, 8)
        line(draw, [(1016, 329), (1016, 347)], accent, 6)
        line(draw, [(1029, 342), (1029, 357)], accent, 6)
    else:
        polygon(draw, [(983, 246), (1024, 263), (1019, 320), (983, 348), (947, 320), (942, 263)], accent)
        line(draw, [(963, 291), (979, 307), (1005, 279)], PAPER, 6)


def draw_browser(draw, motif, accent):
    rectangle(draw, (856, 187, 1108, 411), (15, 14, 12), PAPER, 3)
    rectangle(draw, (856, 187, 1108, 226), accent)
    for index in range(3):
        x = 870 + index * 16
        ellipse(draw, (x, 201, x + 8, 209), PAPER)

    if motif == "window":
        rectangle(draw, (877, 251, 1087, 376), (39, 34, 27), (93, 81, 62), 2)
        rectangle(draw, (895, 271, 932, 351), accent)
        line(draw, [(949, 277), (1066, 277)], PAPER, 4)
        line(draw, [(949, 301), (1052, 301)], MUTED, 4)
        line(draw, [(949, 325), (1070, 325)], MUTED, 4)
    elif motif == "editor":
        for index in range(5):
            y = 253 + index * 25
            line(draw, [(879, y), (915 + index * 10, y)], accent if index == 1 else PAPER, 3)
            line(draw, [(931, y), (1085, y)], MUTED, 3)
        rectangle(draw, (885, 385, 1078, 397), accent)
    elif motif == "static":
        rectangle(draw, (878, 250, 960, 373), (36, 32, 26), MUTED, 2)
        for index in range(4):
            y = 269 + index * 22
            line(draw, [(891, y), (947 - (index % 2) * 14, y)], PAPER if index == 0 else MUTED, 3)
        polygon(draw, [(969, 292), (990, 310), (969, 328)], accent)
        rectangle(draw, (1000, 279, 1085, 345), (54, 48, 36), PAPER, 2)
    elif motif == "cache":
        rectangle(draw, (880, 250, 1087, 366), (36, 32, 26), MUTED, 2)
        rectangle(draw, (896, 267, 1071, 294), accent)
        line(draw, [(898, 318), (975, 318)], PAPER, 4)
        line(draw, [(898, 339), (1059, 339)], MUTED, 3)
        polygon(draw, [(1068, 247), (1092, 265), (1069, 283)], PAPER)
    elif motif == "license":
        rectangle(draw, (879, 252, 1048, 371), (36, 32, 26), MUTED, 2)
        ellipse(draw, (1003, 267, 1026, 290), accent)
        polygon(draw, [(891, 350), (931, 304), (960, 332), (982, 307), (1037, 350)], PAPER)
        rectangle(draw, (1000, 358, 1093, 395), PAPER, INK, 2)
        label(draw, 1010, 367, "LICENSE", 14, INK, MONO_FONT)
    elif motif == "access":
        rectangle(draw, (878, 248, 1087, 374), (36, 32, 26), MUTED, 2)
        ellipse(draw, (964, 261, 1002, 299), accent)
        line(draw, [(983, 301), (983, 348)], PAPER, 5)
        line(draw, [(948, 315), (1018, 315)], PAPER, 5)
        line(draw, [(983, 348), (954, 367)], accent, 5)
        line(draw, [(983, 348), (1012, 367)], accent, 5)
        for x in (881, 943, 1005):
            rectangle(draw, (x, 383, x + 49, 398), PAPER)
    elif motif == "image":
        rectangle(draw, (878, 250, 1087, 367), (36, 32, 26), MUTED, 2)
        ellipse(draw, (1041, 263, 1067, 289), accent)
        polygon(draw, [(890, 350), (933, 295), (967, 330), (995, 301), (1074, 350)], PAPER)
        line(draw, [(892, 386), (1073, 386)], accent, 5)
    else:
        for index, (metric, value) in enumerate((("LCP", 78), ("INP", 53), ("CLS", 91))):
            x = 874 + index * 76
            rectangle(draw, (x, 251, x + 67, 376), (48, 42, 31), MUTED, 1)
            label(draw, x + 6, 261, metric, 13, PAPER, MONO_FONT)
            rectangle(draw, (x + 12, 355 - value * 0.65, x + 54, 355), accent if index == 1 else (193, 153, 95))


def draw_files(draw, motif, accent):
    rectangle(draw, (866, 231, 1098, 379), (38, 33, 26), PAPER, 2)
    if motif == "sync":
        ellipse(draw, (887, 269, 954, 336), accent)
        label(draw, 895, 291, "FILE", 16, INK, MONO_FONT)
        ellipse(draw, (1012, 267, 1068, 323), None, PAPER, 4)
        line(draw, [(956, 286), (1012, 286)], PAPER, 4)
        polygon(draw, [(1003, 276), (1017, 286), (1003, 297)], PAPER)
        line(draw, [(1015, 346), (958, 346)], accent, 4)
        polygon(draw, [(968, 336), (954, 346), (968, 357)], accent)
    elif motif == "folder":
        polygon(draw, [(885, 273), (953, 273), (973, 290), (1076, 290), (1076, 354), (885, 354)], accent)
        rectangle(draw, (903, 301, 1058, 341), PAPER)
        line(draw, [(915, 314), (1044, 314)], MUTED, 3)
        line(draw, [(915, 328), (1024, 328)], MUTED, 3)
    else:
        rectangle(draw, (912, 248, 1056, 361), PAPER, MUTED, 2)
        for index in range(4):
            y = 271 + index * 21
            line(draw, [(939, y), (1038, y)], accent if index == 0 else MUTED, 3)
        line(draw, [(925, 263), (925, 346)], accent, 3)


def draw_motif(draw, motif, accent):
    rectangle(draw, (826, 136, 1138, 477), DARK, INK, 3)
    rectangle(draw, (842, 152, 1122, 461), (41, 36, 28), (93, 81, 62), 1)

    if motif in ("phone", "choice", "key", "shield"):
        draw_phone(draw, motif, accent)
    elif motif in ("window", "editor", "static", "cache", "license", "access", "image", "vitals"):
        draw_browser(draw, motif, accent)
    elif motif in ("sync", "folder", "notes"):
        draw_files(draw, motif, accent)
    elif motif == "branch":
        line(draw, [(901, 253), (901, 356)], PAPER, 5)
        line(draw, [(901, 287), (1018, 287), (1018, 252)], accent, 5)
        line(draw, [(901, 328), (1060, 328), (1060, 365)], accent, 5)
        for x, y in ((901, 253), (901, 356), (1018, 252), (1060, 365)):
            color = PAPER if x == 901 else accent
            ellipse(draw, (x - 11, y - 11, x + 11, y + 11), color)
        rectangle(draw, (947, 384, 1077, 401), PAPER)
    else:
        for index, (x, y) in enumerate(((878, 251), (969, 300), (890, 349))):
            rectangle(draw, (x, y, x + 153, y + 42), (46, 40, 30), PAPER, 2)
            rectangle(draw, (x + 10, y + 11, x + 67, y + 17), accent if index == 1 else PAPER)
            line(draw, [(x + 10, y + 29), (x + 134, y + 29)], MUTED, 2)


def create_cover(slug, details):
    eyebrow, headline, motif, accent = details
    image = Image.new("RGB", (WIDTH * SCALE, HEIGHT * SCALE), PAPER)
    draw = ImageDraw.Draw(image)

    rectangle(draw, (14, 14, 1186, 616), None, INK, 4)
    rectangle(draw, (18, 18, 1182, 30), accent)
    for row in range(5):
        for column in range(7):
            x = 790 + column * 48
            y = 71 + row * 42
            ellipse(draw, (x, y, x + 3, y + 3), (205, 195, 177))

    rectangle(draw, (56, 58, 108, 110), PAPER, INK, 3)
    label(draw, 62, 69, "BX", 27, INK)
    label(draw, 125, 57, "BLOXIO", 34, INK)
    label(draw, 127, 99, eyebrow, 14, MUTED, MONO_FONT)

    first_line, second_line = headline.split("|")
    label(draw, 58, 192, first_line, 76, INK, max_width=715)
    label(draw, 58, 288, second_line, 84, accent, max_width=715)
    rectangle(draw, (60, 405, 122, 413), INK)
    label(draw, 60, 437, "PRACTICAL NOTES FOR THE OPEN WEB", 18, MUTED, MONO_FONT)
    draw_motif(draw, motif, accent)
    rectangle(draw, (826, 505, 1138, 564), PAPER, INK, 2)
    label(draw, 846, 520, "FIELD NOTES / BLOXIO", 17, INK, MONO_FONT)

    destination = OUTPUT_DIR / f"{slug}.jpg"
    image.resize((WIDTH, HEIGHT), Image.Resampling.LANCZOS).save(
        destination,
        "JPEG",
        quality=90,
        optimize=True,
        progressive=True,
    )
    return destination


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for slug, details in COVERS.items():
        path = create_cover(slug, details)
        print(f"Generated {path.relative_to(ROOT)}")
    print(f"Done: {len(COVERS)} covers at {WIDTH}x{HEIGHT}.")


if __name__ == "__main__":
    main()
