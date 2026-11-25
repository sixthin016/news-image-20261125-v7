#!/usr/bin/env python3
"""Draw the v7 front page for Wednesday 25 November 2026.

A make.fun news-image-20261125 entry. Runs at build time (Pillow +
system fonts) and writes assets/entry.png at 1024x1024, under 1 MiB.
The submitted program (main.py, stdlib only) just copies that PNG.

Every story below was verified by the builder against a live named
source on 26 Nov 2026 and first reported on Wednesday 25 November
2026 (UTC). Stories that turned out to belong to Tuesday 24 Nov
(Huawei verdict, Putin's "inevitable" vow, Anthropic -6.5%, the Dow's
first close above 50,000, Miss Universe, the UN femicide report) or
earlier (COP31 Sun 22, GTA VI's $3.79bn Fri 20) are NOT in the body:
they are listed in the DATE CHECK footer as left out.

Layout (1024 x 1024):
  masthead -> KPI strip (6 big numbers) -> UTC timeline strip ->
  3 illustrated hero panels (the consensus top 3 stories) ->
  10 small panels, each with its own drawn scene ->
  world map + 35 more stories (place first) ->
  DATE CHECK footer -> source line.
"""

import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(ROOT, "assets", "entry.png")

# ---------------------------------------------------------------- palette
PAPER = (248, 243, 232)
PAPER2 = (241, 234, 218)
INK = (25, 23, 19)
INK2 = (74, 68, 58)
RED = (176, 36, 24)
BLUE = (29, 78, 137)
TEAL = (15, 107, 92)
GREEN = (30, 107, 52)
AMBER = (138, 97, 0)
GOLD = (198, 158, 62)
SKY = (178, 209, 228)
SEA = (149, 186, 214)
LAND = (227, 211, 168)
LANDLINE = (176, 152, 110)
DARK = (18, 28, 44)
DARK2 = (28, 44, 66)
RULE = (25, 23, 19)

# ---------------------------------------------------------------- fonts
FD = "/usr/share/fonts/truetype/dejavu"
FN = "/usr/share/fonts/truetype/noto"


def font(path, size):
    return ImageFont.truetype(path, size)


SERIF = f"{FN}/NotoSerif-Bold.ttf"
SERIF_BLACK = f"{FN}/NotoSerif-Black.ttf"
SERIF_REG = f"{FN}/NotoSerif-Regular.ttf"
SANS = f"{FN}/NotoSans-Regular.ttf"
SANS_B = f"{FN}/NotoSans-Bold.ttf"
SANS_BLACK = f"{FN}/NotoSans-Black.ttf"


def F_SERIF(s):
    return font(SERIF, s)


def F_SERIF_BLACK(s):
    return font(SERIF_BLACK, s)


def F_SERIF_REG(s):
    return font(SERIF_REG, s)


def F_SANS(s):
    return font(SANS, s)


def F_SANS_B(s):
    return font(SANS_B, s)


def F_SANS_BLACK(s):
    return font(SANS_BLACK, s)


# ---------------------------------------------------------------- the slate
# status: C = CONFIRMED (verified by a named source),
#         R = REPORTED (reported, details unconfirmed),
#         L = CLAIM (one side's claim, no independent confirmation).
# field / region are used for the masthead counts.

HEROES = [
    dict(
        n=1, place="WASHINGTON", lon=-77.0, lat=39.0,
        field="Trade", region="North America", status="C",
        src="Reuters",
        head="US PROPOSES TARIFFS ON 14 ECONOMIES",
        deck=("USTR ends an 8-month Section 301 probe: China faces 20% "
              "on top of 25% already in place. The EU, Japan and South "
              "Korea are capped at 15%. Hearings in January."),
        scene="ship",
    ),
    dict(
        n=2, place="SEOUL", lon=127.0, lat=37.5,
        field="Markets", region="Asia", status="C",
        src="WSJ / AP",
        head="KOSPI CRASHES 6.2% AS CHIP ROUT SPREADS",
        deck=("Seoul closes at 4,697.51, a 10-month low. Samsung -9.9%, "
              "SK Hynix -11.1%. Nikkei -2.8%, Taiex -5% as AI doubts "
              "sweep Asia."),
        scene="chart",
    ),
    dict(
        n=3, place="JIUQUAN", lon=100.0, lat=40.0,
        field="Space", region="Asia", status="C",
        src="Xinhua / CMSA",
        head="PAKISTAN'S FIRST ASTRONAUT DOCKS AT TIANGONG",
        deck=("Shenzhou-24 lifts off 00:18 UTC and docks 03:56 UTC. "
              "Muhammad Zeeshan Ali, 40, is the first foreigner aboard "
              "China's station; he stays 5-10 days."),
        scene="launch",
    ),
]

PANELS = [
    dict(
        n=4, place="SAMARA", lon=50.0, lat=53.0,
        field="Conflict", region="Europe", status="L",
        src="Reuters / Ukr. Gen. Staff",
        head="UKRAINE DRONES SET TWO ROSNEFT REFINERIES ABLAZE",
        deck="Syzran and Kuibyshev hit overnight; 145 drones downed, 1 killed.",
        scene="refinery",
    ),
    dict(
        n=5, place="HORMUZ", lon=56.5, lat=26.5,
        field="Energy", region="Middle East", status="L",
        src="IRGC via Reuters",
        head="TWO TANKERS HIT MINES IN THE STRAIT OF HORMUZ",
        deck="IRGC says mines set both ablaze on an 'unauthorised' route; Brent $91-92.",
        scene="tanker",
    ),
    dict(
        n=6, place="LONDON", lon=-0.1, lat=51.5,
        field="Economy", region="Europe", status="C",
        src="Ofgem",
        head="UK ENERGY BILLS TO JUMP 26% IN JANUARY",
        deck="Ofgem lifts the cap to \u00a32,166 a year, up \u00a3443, as gas prices surge.",
        scene="meter",
    ),
    dict(
        n=7, place="CAIRO", lon=31.2, lat=30.0,
        field="Disaster", region="Africa", status="C",
        src="AP",
        head="TANKER FIRE ON CAIRO RING ROAD KILLS 30+",
        deck="Fuel tanker overturns in Warraq, Giza; 27 vehicles burn; toll preliminary.",
        scene="fire",
    ),
    dict(
        n=8, place="BOGOR", lon=106.8, lat=-6.6,
        field="Disaster", region="Asia", status="C",
        src="AP",
        head="NINE DEAD, 17 TRAPPED IN JAVA GOLD MINE FLOOD",
        deck="Rain swells a river into a 100-m shaft at an illegal pit near Pongkor.",
        scene="mine",
    ),
    dict(
        n=9, place="DHAKA", lon=90.4, lat=23.8,
        field="Labour", region="Asia", status="C",
        src="AP / AFP",
        head="BANGLADESH GARMENT PAY UP 36% AFTER PROTESTS",
        deck="Wage board sets Tk17,000 a month, up from Tk12,500.",
        scene="factory",
    ),
    dict(
        n=10, place="HONIARA", lon=160.0, lat=-9.4,
        field="Diplomacy", region="Oceania", status="C",
        src="AP",
        head="SOLOMON ISLANDS PICKS AUSTRALIA, SHUTS OUT BASES",
        deck="Treaty signed in Canberra: no foreign military base on its soil.",
        scene="pact",
    ),
    dict(
        n=11, place="CANBERRA", lon=149.0, lat=-35.3,
        field="Economy", region="Oceania", status="C",
        src="ABS",
        head="AUSTRALIA INFLATION JUMPS TO 4.9%",
        deck="CPI up from 4.3% in September; housing +6.4%.",
        scene="chartmini",
    ),
    dict(
        n=12, place="NEW YORK", lon=-74.0, lat=40.7,
        field="Markets", region="North America", status="C",
        src="Zacks",
        head="DOW HOLDS 50,000 AFTER 1,100-POINT PLUNGE",
        deck="Dow +0.33% to 50,183; Nasdaq -0.62% into Thanksgiving.",
        scene="dow",
    ),
    dict(
        n=13, place="PYONGYANG", lon=125.8, lat=39.0,
        field="Diplomacy", region="Asia", status="C",
        src="Reuters / KCNA",
        head="NORTH KOREA EXPELS SWISS ENVOY IN 48 HOURS",
        deck="Pyongyang shuts Bern's month-old office over camp sanctions.",
        scene="envoy",
    ),
]

# 35 more stories: (number, place, lon, lat, field, region, status, source,
#                  one-line text)
MORE = [
    (14, "BENGHAZI", 20.0, 32.1, "Conflict", "Africa", "C", "AP",
     "Two Libyan officers die of wounds; army vows revenge."),
    (15, "NEW YORK", -74.0, 40.7, "Markets", "North America", "C", "Barron's",
     "Anthropic slides again, -2.1% to $80.20."),
    (16, "WASHINGTON", -77.0, 39.0, "Economy", "North America", "C", "BEA",
     "US GDP grew 4.3% in Q3, up from 3.4%."),
    (17, "WASHINGTON", -77.0, 39.0, "Economy", "North America", "C", "WSJ",
     "October PCE, jobless claims land before Thanksgiving."),
    (18, "NEW YORK", -74.0, 40.7, "Markets", "North America", "C", "Zacks",
     "S&P -0.25%, Nasdaq -0.62%; VIX 28.3."),
    (19, "LONDON", -0.1, 51.5, "Energy", "Europe", "C", "Reuters",
     "Brent jumps to $91-92 on Hormuz mine claims."),
    (20, "TOKYO", 139.7, 35.7, "Markets", "Asia", "C", "AP",
     "SoftBank -14.8%, Kioxia -14.2% in chip rout."),
    (21, "TOKYO", 139.7, 35.7, "Markets", "Asia", "C", "WSJ",
     "Nikkei -2.8% as chip stocks drag Tokyo lower."),
    (22, "TAIPEI", 121.6, 25.0, "Markets", "Asia", "C", "AP",
     "Taiex -5%; TSMC -3.6%, MediaTek -10%."),
    (23, "WASHINGTON", -77.0, 39.0, "Diplomacy", "North America", "C", "US Virtual Embassy",
     "US tells citizens to leave Iran at once."),
    (24, "DOHA", 51.5, 25.3, "Diplomacy", "Middle East", "C", "Reuters",
     "Iran offers Hormuz reopening in 48 hours via Qatar."),
    (25, "LOS ANGELES", -118.2, 34.0, "Markets", "North America", "C", "Barron's",
     "SpaceX -6.8% to $117.25 in AI sell-off."),
    (26, "ROUND ROCK", -97.7, 30.5, "Technology", "North America", "C", "TradingView",
     "Dell slides 7% despite record Q3 sales +103%."),
    (27, "SPRING, TEXAS", -95.4, 30.1, "Technology", "North America", "C", "Equiti",
     "HPE falls despite solid earnings."),
    (28, "NEW YORK", -74.0, 40.7, "Culture", "North America", "C", "AP",
     "Macy's 100th parade moved to Saturday."),
    (29, "GOMA", 29.2, -1.7, "Health", "Africa", "C", "AP",
     "Fighting forces Ebola workers to evacuate."),
    (30, "MISSISSIPPI", -89.0, 30.2, "Disaster", "North America", "C", "AP",
     "Plane crash kills a family of six."),
    (31, "CARTAGENA", -75.5, 10.4, "Crime", "South America", "C", "AP",
     "All supermarket hostages rescued; 1 captor killed."),
    (32, "VENICE", 12.3, 45.4, "Culture", "Europe", "C", "AP",
     "Biennale prizes go to Nick Cave and India."),
    (33, "MADRID", -3.7, 40.4, "Justice", "Europe", "C", "AP",
     "\u00c1brego Garc\u00eda, wrongly deported, arrives in Spain."),
    (34, "IOWA", -93.6, 42.0, "Defence", "North America", "C", "AP",
     "Army detonates 5 tons of unstable lead azide."),
    (35, "CAPE TOWN", 18.4, -33.9, "Health", "Africa", "C", "AP",
     "Biovac to lift vaccine output with EU loan."),
    (36, "LONDON", -0.1, 51.5, "Culture", "Europe", "C", "AP",
     "Gordon Ramsay to lead Top Gear revival."),
    (37, "CANBERRA", 149.0, -35.3, "Technology", "Oceania", "C", "AP",
     "Online safety law passes; Big Tech faces fines."),
    (38, "PARIS", 2.35, 48.85, "Transport", "Europe", "C", "AP",
     "Eurostar cancels Paris-London trains in staff strike."),
    (39, "WASHINGTON", -77.0, 39.0, "Diplomacy", "North America", "C", "AP",
     "Melania Trump reunites 7th group of children."),
    (40, "LONDON", -0.1, 51.5, "Justice", "Europe", "C", "AP",
     "Nuclear test veterans win 40-year inquiry battle."),
    (41, "WASHINGTON", -77.0, 39.0, "Technology", "North America", "C", "AP",
     "Unclassified CIA system breached, AP source says."),
    (42, "LAGOS", 3.4, 6.45, "Culture", "Africa", "C", "BBC",
     "Film star Pete Edochie dies at 79."),
    (43, "MOSCOW", 37.6, 55.75, "Conflict", "Europe", "R", "BBC",
     "Leaked figures put Russian war dead at 490,334."),
    (44, "VATICAN", 12.45, 41.9, "Culture", "Europe", "C", "AP",
     "Pope Francis diary tells of 'spiritual crisis'."),
    (45, "LOS ANGELES", -118.2, 34.0, "Justice", "North America", "C", "BBC",
     "Thomas Markle indicted on abuse-material charges."),
    (46, "JOHANNESBURG", 28.0, -26.2, "Justice", "Africa", "C", "AP",
     "S. Africa convicts man who tried to fight for Russia."),
    (47, "WORLD", 0.0, 0.0, "Society", "Global", "C", "UN Women",
     "UN: 47,000 women killed by partners in 2025."),
    (48, "LONDON", -0.1, 51.5, "Transport", "Europe", "C", "TfL",
     "Tube strike Thu-Fri: no Circle/Piccadilly Thursday."),
]

KPI = [
    ("20%", "CHINA TARIFFS, TOP RATE"),
    ("-6.2%", "KOSPI, SEOUL"),
    ("1st", "PAKISTANI IN ORBIT"),
    ("+26%", "UK ENERGY CAP"),
    ("30+", "DEAD, CAIRO TANKER FIRE"),
    ("9", "DEAD, JAVA GOLD MINE"),
]

TIMELINE = [
    ("00:18", "Shenzhou-24 lifts off"),
    ("03:56", "Dock at Tiangong"),
    ("06:30", "Kospi closes -6.2%"),
    ("10:59", "Ofgem: cap +26%"),
    ("P.M.", "USTR proposes tariffs"),
    ("20:15", "Cairo tanker fire"),
]

LEFT_OUT = [
    ("Huawei convicted, 10 of 12 counts", "Tue 24 Nov"),
    ("Putin: retaliation 'inevitable'", "Tue 24 Nov"),
    ("Anthropic -6.5%, below $83 IPO price", "Tue 24 Nov"),
    ("Dow first closes above 50,000", "Tue 24 Nov"),
    ("Miss Universe crowned in San Juan", "Tue 24 Nov"),
    ("UN femicide report: 47,000 killed", "Tue 24 Nov"),
    ("COP31 collapses, no deal", "Sun 22 Nov"),
    ("GTA VI: $3.79bn day one", "Fri 20 Nov"),
]

NOT_YET = "Thanksgiving Thu 26 Nov  \u00b7  Macy's parade Sat 28 Nov"

STATUS_TEXT = {"C": "CONFIRMED", "R": "REPORTED", "L": "CLAIM"}
STATUS_COLOR = {"C": GREEN, "R": AMBER, "L": RED}

# Rough continent outlines (lon, lat), equirectangular, for the map.
CONTINENTS = [
    # North America
    [(-168, 66), (-158, 71), (-140, 70), (-128, 71), (-115, 69), (-100, 69),
     (-90, 68), (-82, 66), (-76, 62), (-68, 58), (-60, 55), (-55, 52),
     (-60, 47), (-65, 44), (-70, 42), (-74, 39), (-76, 35), (-80, 32),
     (-81, 26), (-84, 30), (-89, 29), (-91, 19), (-96, 16), (-94, 17),
     (-90, 14), (-86, 13), (-83, 9), (-79, 9), (-77, 7), (-80, 8),
     (-83, 10), (-86, 12), (-88, 14), (-90, 14), (-92, 15), (-95, 16),
     (-97, 16), (-97, 19), (-97, 22), (-97, 26), (-100, 28), (-105, 25),
     (-110, 24), (-114, 29), (-117, 33), (-122, 37), (-124, 42), (-124, 48),
     (-128, 51), (-133, 56), (-140, 60), (-150, 61), (-158, 58), (-165, 60),
     (-168, 66)],
    # South America
    [(-77, 7), (-72, 11), (-64, 11), (-60, 8), (-52, 5), (-50, 0),
     (-44, -3), (-35, -8), (-38, -15), (-40, -21), (-48, -27), (-52, -33),
     (-58, -38), (-62, -41), (-66, -47), (-69, -52), (-71, -54), (-74, -50),
     (-74, -40), (-72, -30), (-70, -20), (-75, -15), (-79, -8), (-81, -4),
     (-80, 1), (-77, 4), (-77, 7)],
    # Africa
    [(-6, 35), (10, 37), (20, 32), (32, 31), (35, 28), (38, 22), (43, 12),
     (51, 11), (51, 2), (46, -2), (40, -10), (36, -18), (33, -26), (28, -33),
     (20, -35), (16, -28), (12, -18), (12, -6), (9, 4), (4, 6), (-8, 5),
     (-13, 8), (-17, 15), (-17, 21), (-16, 25), (-13, 28), (-9, 31),
     (-6, 35)],
    # Europe
    [(-10, 37), (-9, 43), (-2, 48), (-4, 50), (2, 51), (5, 53), (8, 57),
     (10, 59), (5, 60), (10, 62), (18, 69), (28, 71), (32, 70), (40, 68),
     (48, 66), (40, 60), (38, 56), (30, 60), (24, 59), (21, 55), (19, 54),
     (14, 54), (12, 45), (18, 40), (23, 36), (28, 41), (23, 40), (19, 42),
     (12, 44), (8, 44), (3, 43), (0, 40), (-2, 37), (-9, 37), (-10, 37)],
    # Asia
    [(40, 68), (48, 66), (55, 69), (68, 73), (80, 73), (95, 76), (110, 74),
     (125, 73), (140, 72), (158, 70), (170, 67), (178, 65), (170, 60),
     (162, 56), (156, 51), (142, 50), (140, 40), (135, 35), (129, 33),
     (126, 38), (122, 39), (120, 35), (122, 30), (118, 25), (110, 20),
     (108, 12), (105, 9), (100, 7), (98, 12), (94, 17), (92, 21), (89, 22),
     (86, 20), (80, 15), (77, 8), (74, 20), (70, 22), (66, 25), (61, 25),
     (57, 27), (54, 27), (50, 29), (48, 30), (43, 12), (40, 15), (39, 21),
     (43, 27), (48, 29), (50, 29), (52, 27), (56, 26), (58, 23), (60, 25),
     (62, 25), (66, 25), (68, 23), (72, 21), (74, 20), (76, 10), (80, 13),
     (84, 19), (88, 22), (91, 22), (94, 18), (97, 16), (100, 10), (103, 2),
     (104, 1), (100, 5), (98, 8), (95, 15), (92, 20), (89, 22), (85, 19),
     (82, 17), (79, 9), (76, 8), (72, 20), (68, 22), (64, 25), (58, 25),
     (54, 24), (50, 26), (48, 28), (44, 29), (40, 32), (36, 36), (33, 31),
     (30, 36), (28, 41), (24, 36), (22, 37), (26, 40), (30, 42), (34, 44),
     (38, 47), (40, 51), (44, 55), (48, 58), (52, 62), (58, 66), (60, 69),
     (55, 69), (48, 68), (40, 68)],
    # Australia
    [(114, -22), (114, -32), (118, -35), (124, -33), (130, -32), (134, -33),
     (136, -35), (140, -38), (145, -38), (150, -37), (153, -27), (153, -24),
     (146, -19), (142, -11), (136, -12), (132, -11), (126, -14), (122, -17),
     (118, -20), (114, -22)],
]


# ---------------------------------------------------------------- helpers

def text_w(draw, s, f):
    return draw.textlength(s, font=f)


def wrap(draw, s, f, max_w):
    """Greedy word wrap; returns list of lines."""
    words = s.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=f) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_wrapped(draw, x, y, s, f, fill, max_w, leading=None, align="left"):
    if leading is None:
        leading = f.size + 2
    lines = wrap(draw, s, f, max_w)
    for ln in lines:
        lx = x
        if align == "center":
            lx = x - draw.textlength(ln, font=f) / 2
        draw.text((lx, y), ln, font=f, fill=fill)
        y += leading
    return y


def chip(draw, x, y, status, f=None):
    """Small status chip: coloured dot + text."""
    if f is None:
        f = F_SANS_B(8)
    label = STATUS_TEXT[status]
    col = STATUS_COLOR[status]
    draw.ellipse([x, y + 2, x + 6, y + 8], fill=col)
    draw.text((x + 9, y), label, font=f, fill=col)
    return x + 9 + draw.textlength(label, font=f)


def rule(draw, x0, y, x1, wdt=1, fill=INK):
    draw.line([(x0, y), (x1, y)], fill=fill, width=wdt)


def num_badge(draw, cx, cy, n, r=9, fill=RED, fg=PAPER):
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=fill, outline=INK, width=1)
    s = str(n)
    f = F_SANS_B(10 if len(s) < 2 else 8)
    draw.text((cx - draw.textlength(s, font=f) / 2, cy - f.size / 2 - 1),
              s, font=f, fill=fg)


def _scene_into(img, scene_fn, x, y, w, h):
    """Render a scene into a temp image and paste it: clips any overflow."""
    sub = Image.new("RGB", (int(w), int(h)), (255, 255, 255))
    sd = ImageDraw.Draw(sub)
    scene_fn(sd, 0, 0, int(w), int(h))
    img.paste(sub, (int(x), int(y)))


# ---------------------------------------------------------------- hero scenes

def scene_ship(draw, x, y, w, h):
    """Container ship on the sea, % boxes above the containers."""
    draw.rectangle([x, y, x + w, y + h], fill=SKY)
    # sun + clouds
    draw.ellipse([x + w - 52, y + 8, x + w - 22, y + 38], fill=(252, 214, 110))
    for cx, cy, cw in [(x + 12, y + 14, 46), (x + 70, y + 8, 38)]:
        draw.ellipse([cx, cy, cx + cw, cy + 12], fill=(255, 255, 255))
    # sea
    draw.rectangle([x, y + h - 34, x + w, y + h], fill=SEA)
    draw.line([(x, y + h - 34), (x + w, y + h - 34)], fill=(255, 255, 255), width=1)
    for i in range(5):
        wx = x + 14 + i * 62
        draw.arc([wx, y + h - 26, wx + 34, y + h - 14], 200, 340,
                 fill=(255, 255, 255), width=2)
    # ship hull
    hy = y + h - 52
    draw.polygon([(x + 14, hy), (x + w - 14, hy), (x + w - 34, hy + 20),
                  (x + 34, hy + 20)], fill=(140, 30, 22))
    draw.rectangle([x + 14, hy, x + w - 14, hy + 4], fill=(90, 18, 14))
    # bridge tower
    draw.rectangle([x + w - 62, hy - 34, x + w - 38, hy], fill=(240, 240, 235))
    for r in range(3):
        draw.rectangle([x + w - 58, hy - 30 + r * 11, x + w - 42, hy - 23 + r * 11],
                       fill=BLUE)
    # containers with % boxes
    boxes = [("CHN", "20%", RED), ("VNM", "20%", (196, 90, 20)),
             ("EU", "15%", BLUE), ("JPN", "15%", TEAL),
             ("KOR", "15%", (110, 90, 160)), ("MYS", "19%", (120, 80, 40))]
    bw = (w - 92) / 6
    for i, (cc, pct, col) in enumerate(boxes):
        bx = x + 22 + i * bw
        draw.rectangle([bx, hy - 34, bx + bw - 3, hy - 2], fill=col,
                       outline=(255, 255, 255), width=1)
        f1 = F_SANS_B(8)
        f2 = F_SANS_B(11)
        draw.text((bx + (bw - 3) / 2 - draw.textlength(cc, font=f1) / 2, hy - 32),
                  cc, font=f1, fill=(255, 255, 255))
        draw.text((bx + (bw - 3) / 2 - draw.textlength(pct, font=f2) / 2, hy - 22),
                  pct, font=f2, fill=(255, 255, 255))
    # "14 ECONOMIES" flag on the mast
    draw.line([(x + 30, hy - 34), (x + 30, hy - 58)], fill=INK, width=2)
    draw.polygon([(x + 30, hy - 58), (x + 62, hy - 52), (x + 30, hy - 46)],
                 fill=RED)
    f = F_SANS_B(8)
    draw.text((x + 34, hy - 56), "14", font=F_SANS_BLACK(10), fill=(255, 255, 255))


def scene_chart(draw, x, y, w, h):
    """Dark panel: falling index lines with labelled values."""
    draw.rectangle([x, y, x + w, y + h], fill=DARK)
    # grid
    for i in range(1, 4):
        gy = y + i * h / 4
        draw.line([(x + 8, gy), (x + w - 8, gy)], fill=(52, 66, 92), width=1)
    for i in range(1, 5):
        gx = x + i * w / 5
        draw.line([(gx, y + 6), (gx, y + h - 6)], fill=(38, 52, 76), width=1)
    # falling lines: (label, colour, points, value)
    lines = [
        ("KOSPI -6.2%", (255, 92, 72), 0.30),
        ("HYNIX -11.1%", (255, 170, 60), 0.52),
        ("SAMSUNG -9.9%", (255, 220, 90), 0.42),
        ("NIKKEI -2.8%", (120, 200, 255), 0.18),
        ("TAIEX -5%", (150, 230, 170), 0.24),
    ]
    top = y + 12
    for j, (label, col, drop) in enumerate(lines):
        y0 = top + j * (h - 34) / 5
        y1 = y0 + (h - 40) * drop
        pts = [(x + 10 + k * (w - 20) / 4,
                y0 + (y1 - y0) * (k / 4) ** 0.8 + (3 if k % 2 else -2))
               for k in range(5)]
        draw.line(pts, fill=col, width=2)
        for px, py in pts:
            draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=col)
        f = F_SANS_B(9)
        tw = draw.textlength(label, font=f)
        draw.rectangle([x + w - 8 - tw - 4, y0 - 9, x + w - 4, y0 + 2], fill=DARK)
        draw.text((x + w - 8 - tw, y0 - 8),
                  label, font=f, fill=col)
    draw.text((x + 10, y + h - 16), "4,697.51", font=F_SANS_BLACK(13),
              fill=(255, 255, 255))
    draw.text((x + 86, y + h - 13), "10-MONTH LOW", font=F_SANS_B(8),
              fill=(255, 170, 150))


def scene_launch(draw, x, y, w, h):
    """Rocket rising past a space station; Pakistan + China flags."""
    draw.rectangle([x, y, x + w, y + h], fill=(16, 24, 52))
    # stars
    for sx, sy in [(18, 12), (52, 26), (90, 10), (130, 30), (170, 14),
                   (210, 26), (250, 10), (290, 24), (30, 52), (300, 60),
                   (150, 44), (200, 58)]:
        draw.ellipse([x + sx, y + sy, x + sx + 2, y + sy + 2], fill=(255, 255, 255))
    # earth arc at bottom
    draw.ellipse([x - 60, y + h - 26, x + w + 60, y + h + 70], fill=(46, 110, 180))
    draw.arc([x - 60, y + h - 26, x + w + 60, y + h + 70], 200, 340,
             fill=(140, 200, 240), width=2)
    # station (right)
    sx, sy = x + w - 118, y + 18
    draw.rectangle([sx, sy + 12, sx + 96, sy + 26], fill=(200, 205, 210))
    draw.rectangle([sx + 40, sy + 4, sx + 56, sy + 34], fill=(220, 225, 230))
    draw.rectangle([sx - 8, sy + 14, sx, sy + 24], fill=(40, 90, 180))
    draw.rectangle([sx + 96, sy + 14, sx + 104, sy + 24], fill=(40, 90, 180))
    draw.ellipse([sx + 44, sy + 12, sx + 52, sy + 20], fill=(255, 220, 120))
    # flags on the station
    draw.rectangle([sx + 8, sy + 16, sx + 22, sy + 24], fill=(20, 122, 60))
    draw.ellipse([sx + 12, sy + 18, sx + 18, sy + 22], fill=(255, 255, 255))
    draw.rectangle([sx + 70, sy + 16, sx + 84, sy + 24], fill=(222, 41, 16))
    # rocket (left-centre) with flame
    rx, ry = x + 52, y + 34
    draw.polygon([(rx + 12, ry), (rx + 22, ry + 16), (rx + 2, ry + 16)],
                 fill=(255, 90, 60))
    draw.rectangle([rx + 2, ry + 16, rx + 22, ry + 62], fill=(240, 240, 235))
    draw.rectangle([rx + 2, ry + 30, rx + 22, ry + 38], fill=RED)
    draw.polygon([(rx + 2, ry + 62), (rx - 6, ry + 74), (rx + 2, ry + 68)],
                 fill=(255, 90, 60))
    draw.polygon([(rx + 22, ry + 62), (rx + 30, ry + 74), (rx + 22, ry + 68)],
                 fill=(255, 90, 60))
    draw.polygon([(rx + 8, ry + 62), (rx + 16, ry + 62), (rx + 12, ry + 88)],
                 fill=(255, 190, 60))
    draw.ellipse([rx + 7, ry + 20, rx + 17, ry + 30], fill=BLUE)
    # smoke trail
    for i in range(4):
        draw.ellipse([x + 56 + i * 4, y + h - 44 - i * 3, x + 76 + i * 4,
                      y + h - 30 - i * 3], fill=(220, 220, 215))
    # label
    draw.text((x + 10, y + h - 15), "00:18 UTC LIFTOFF  \u00b7  03:56 UTC DOCK",
              font=F_SANS_B(8), fill=(255, 255, 255))


# ---------------------------------------------------------------- mini scenes
# Each draws a small scene in a box of width w, height h (~44px tall).

def mini_refinery(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(46, 38, 34))
    draw.ellipse([x + w - 34, y + 4, x + w - 14, y + 24], fill=(252, 214, 110))
    for i, tx in enumerate([x + 10, x + 46, x + 82]):
        draw.rectangle([tx, y + h - 26, tx + 22, y + h], fill=(120, 118, 112))
        draw.rectangle([tx + 4, y + h - 36, tx + 18, y + h - 26], fill=(90, 88, 82))
    draw.polygon([(x + 118, y + h), (x + 126, y + 6), (x + 134, y + h)],
                 fill=(150, 148, 142))
    for fx, fy, fr in [(x + 52, y + 8, 7), (x + 66, y + 14, 5), (x + 118, y + 10, 6)]:
        draw.polygon([(fx - fr, fy + fr), (fx, fy - fr), (fx + fr, fy + fr)],
                     fill=(255, 120, 40))
    draw.rectangle([x, y + h - 4, x + w, y + h], fill=(20, 16, 14))


def mini_tanker(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(30, 60, 90))
    draw.rectangle([x, y + h - 16, x + w, y + h], fill=(40, 90, 140))
    draw.polygon([(x + 16, y + h - 22), (x + w - 16, y + h - 22),
                  (x + w - 30, y + h - 12), (x + 30, y + h - 12)], fill=(60, 60, 58))
    draw.rectangle([x + w - 46, y + h - 34, x + w - 30, y + h - 22], fill=(200, 200, 195))
    for fx, fy, fr in [(x + 40, y + 8, 8), (x + 58, y + 16, 6), (x + 96, y + 6, 7)]:
        draw.polygon([(fx - fr, fy + fr), (fx, fy - fr), (fx + fr, fy + fr)],
                     fill=(255, 130, 40))
        draw.ellipse([fx - fr - 4, fy - 2, fx + fr + 4, fy + 6], fill=(60, 60, 60))


def mini_meter(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(232, 222, 200))
    draw.rectangle([x + 18, y + 6, x + 66, y + h - 6], fill=(250, 250, 245),
                   outline=INK, width=1)
    draw.arc([x + 26, y + 10, x + 58, y + 30], 180, 360, fill=RED, width=3)
    draw.line([(x + 42, y + 26), (x + 56, y + 14)], fill=RED, width=2)
    draw.text((x + 30, y + 28), "\u00a32,166", font=F_SANS_BLACK(10), fill=INK)
    draw.line([(x + 78, y + 12), (x + w - 12, y + 12)], fill=RED, width=3)
    draw.polygon([(x + w - 12, y + 8), (x + w - 4, y + 12), (x + w - 12, y + 16)],
                 fill=RED)
    draw.text((x + 78, y + 18), "+26%", font=F_SANS_BLACK(11), fill=RED)


def mini_fire(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(40, 34, 40))
    draw.rectangle([x, y + h - 10, x + w, y + h], fill=(70, 68, 66))
    for cx in [x + 26, x + 62, x + 98, x + 128]:
        draw.rectangle([cx - 12, y + h - 18, cx + 12, y + h - 10], fill=(30, 30, 34))
        draw.rectangle([cx - 8, y + h - 24, cx + 8, y + h - 18], fill=(60, 60, 66))
    for fx, fy, fr in [(x + 30, y + 10, 10), (x + 66, y + 6, 12), (x + 104, y + 12, 9),
                       (x + 130, y + 18, 6)]:
        draw.polygon([(fx - fr, fy + fr), (fx, fy - fr), (fx + fr, fy + fr)],
                     fill=(255, 110, 30))
        draw.polygon([(fx - fr // 2, fy + fr // 2), (fx, fy - fr // 2),
                      (fx + fr // 2, fy + fr // 2)], fill=(255, 200, 60))


def mini_mine(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(52, 42, 32))
    draw.polygon([(x, y + h), (x + w // 2, y + 4), (x + w, y + h)], fill=(90, 72, 50))
    draw.polygon([(x + w // 2 - 14, y + h), (x + w // 2, y + 16),
                  (x + w // 2 + 14, y + h)], fill=(20, 16, 12))
    draw.rectangle([x + w // 2 - 4, y + 22, x + w // 2 + 4, y + h - 8], fill=(255, 200, 60))
    for wx in [x + 14, x + w - 30]:
        draw.arc([wx, y + 18, wx + 26, y + 40], 180, 360, fill=(120, 190, 230), width=2)
    draw.rectangle([x, y + h - 6, x + w, y + h], fill=(30, 24, 18))


def mini_factory(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(214, 226, 232))
    draw.rectangle([x + 12, y + 14, x + w - 12, y + h - 6], fill=(150, 90, 70))
    draw.rectangle([x + 18, y + 20, x + 30, y + 30], fill=(255, 240, 180))
    draw.rectangle([x + 38, y + 20, x + 50, y + 30], fill=(255, 240, 180))
    draw.rectangle([x + 58, y + 20, x + 70, y + 30], fill=(255, 240, 180))
    draw.polygon([(x + 84, y + 14), (x + 92, y + 14), (x + 92, y + h - 6),
                  (x + 84, y + h - 6)], fill=(110, 70, 55))
    draw.rectangle([x + 100, y + 14, x + w - 16, y + h - 6], fill=(120, 72, 58))
    for i in range(3):
        draw.ellipse([x + 96 + i * 8, y + 4, x + 106 + i * 8, y + 12],
                     fill=(255, 255, 255))
    draw.text((x + 104, y + 20), "Tk17,000", font=F_SANS_BLACK(9), fill=(255, 255, 255))


def mini_pact(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(222, 232, 222))
    # two flags on poles
    draw.line([(x + 26, y + 8), (x + 26, y + h - 8)], fill=INK, width=2)
    draw.line([(x + w - 26, y + 8), (x + w - 26, y + h - 8)], fill=INK, width=2)
    draw.rectangle([x + 26, y + 8, x + 52, y + 20], fill=(0, 70, 160))
    draw.rectangle([x + 26, y + 8, x + 52, y + 12], fill=(255, 255, 255))
    draw.rectangle([x + w - 52, y + 8, x + w - 26, y + 20], fill=(20, 122, 60))
    draw.ellipse([x + w - 46, y + 11, x + w - 40, y + 17], fill=(255, 255, 255))
    # handshake: two sleeves + clasped hands
    draw.polygon([(x + 52, y + 26), (x + 78, y + 30), (x + 74, y + h - 10),
                  (x + 52, y + h - 6)], fill=(30, 60, 120))
    draw.polygon([(x + w - 52, y + 26), (x + w - 78, y + 30), (x + w - 74, y + h - 10),
                  (x + w - 52, y + h - 6)], fill=(20, 90, 60))
    draw.ellipse([x + w // 2 - 14, y + 26, x + w // 2 + 14, y + h - 12],
                 fill=(232, 190, 150))
    draw.line([(x + w // 2 - 8, y + 30), (x + w // 2 + 8, y + 30)], fill=(180, 130, 100), width=1)
    draw.line([(x + w // 2 - 8, y + 36), (x + w // 2 + 8, y + 36)], fill=(180, 130, 100), width=1)


def mini_chartmini(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(236, 232, 222))
    draw.line([(x + 10, y + h - 10), (x + w - 8, y + h - 10)], fill=INK, width=1)
    draw.line([(x + 10, y + 6), (x + 10, y + h - 10)], fill=INK, width=1)
    pts = [(x + 12, y + h - 18), (x + 40, y + h - 20), (x + 68, y + h - 26),
           (x + 96, y + h - 24), (x + 124, y + h - 34), (x + w - 12, y + 12)]
    draw.line(pts, fill=RED, width=2)
    for px, py in pts:
        draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=RED)
    draw.text((x + w - 44, y + 4), "4.9%", font=F_SANS_BLACK(11), fill=RED)


def mini_dow(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(18, 28, 44))
    pts = [(x + 8, y + 12), (x + 34, y + 16), (x + 58, y + 34), (x + 84, y + 28),
           (x + 110, y + 16), (x + w - 8, y + 10)]
    draw.line(pts, fill=(90, 200, 130), width=2)
    for px, py in pts:
        draw.ellipse([px - 2, py - 2, px + 2, py + 2], fill=(90, 200, 130))
    draw.text((x + 10, y + h - 16), "50,183", font=F_SANS_BLACK(12),
              fill=(255, 255, 255))
    draw.text((x + 72, y + h - 14), "+0.33%", font=F_SANS_B(9), fill=(90, 200, 130))


def mini_envoy(draw, x, y, w, h):
    draw.rectangle([x, y, x + w, y + h], fill=(228, 220, 205))
    # gate + flag pole
    draw.rectangle([x + 14, y + 8, x + 20, y + h - 6], fill=(90, 80, 70))
    draw.rectangle([x + w - 20, y + 8, x + w - 14, y + h - 6], fill=(90, 80, 70))
    draw.line([(x + 14, y + 10), (x + w - 14, y + 10)], fill=(90, 80, 70), width=2)
    # red cross flag (Swiss) on a small pole, tilted away
    draw.line([(x + 30, y + 12), (x + 30, y + 30)], fill=INK, width=1)
    draw.rectangle([x + 30, y + 12, x + 48, y + 26], fill=(218, 41, 28))
    draw.rectangle([x + 36, y + 15, x + 42, y + 23], fill=(255, 255, 255))
    draw.rectangle([x + 33, y + 18, x + 45, y + 20], fill=(255, 255, 255))
    # walking figure with suitcase
    draw.ellipse([x + 78, y + 14, x + 88, y + 24], fill=(220, 180, 140))
    draw.rectangle([x + 76, y + 24, x + 90, y + h - 10], fill=(40, 50, 70))
    draw.line([(x + 78, y + h - 10), (x + 76, y + h - 4)], fill=INK, width=2)
    draw.line([(x + 88, y + h - 10), (x + 90, y + h - 4)], fill=INK, width=2)
    draw.rectangle([x + 96, y + 28, x + 112, y + 40], fill=(120, 70, 40))
    draw.text((x + 116, y + 28), "48h", font=F_SANS_BLACK(10), fill=RED)


MINI_SCENES = {
    "refinery": mini_refinery,
    "tanker": mini_tanker,
    "meter": mini_meter,
    "fire": mini_fire,
    "mine": mini_mine,
    "factory": mini_factory,
    "pact": mini_pact,
    "chartmini": mini_chartmini,
    "dow": mini_dow,
    "envoy": mini_envoy,
}
HERO_SCENES = {"ship": scene_ship, "chart": scene_chart, "launch": scene_launch}


# ---------------------------------------------------------------- layout

MARGIN = 14
CW = W - 2 * MARGIN  # 996


def build():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    x0, x1 = MARGIN, W - MARGIN
    y = 6

    # ---- masthead kicker
    all_stories = HEROES + PANELS + [dict(n=m[0], field=m[4], region=m[5])
                                     for m in MORE]
    n_stories = len(all_stories)
    regions = sorted({s["region"] for s in all_stories})
    fields = sorted({s["field"] for s in all_stories})
    kicker_l = "THE WORLD IN ONE DAY"
    kicker_r = f"{n_stories} STORIES \u00b7 {len(regions)} REGIONS \u00b7 {len(fields)} FIELDS"
    d.text((x0, y), kicker_l, font=F_SANS_B(12), fill=RED)
    d.text((x1 - d.textlength(kicker_r, font=F_SANS_B(12)), y),
           kicker_r, font=F_SANS_B(12), fill=INK)
    y += 18
    rule(d, x0, y, x1, 2)
    y += 4
    title = "Wednesday 25 November 2026"
    tf = F_SERIF_BLACK(34)
    d.text(((W - d.textlength(title, font=tf)) / 2, y), title, font=tf, fill=INK)
    y += 42
    sub = ("US tariffs on 14 economies  \u00b7  Asia's chip rout  \u00b7  "
           "Pakistan's first astronaut")
    sf = F_SERIF_REG(13)
    d.text(((W - d.textlength(sub, font=sf)) / 2, y), sub, font=sf, fill=INK2)
    y += 20
    rule(d, x0, y, x1, 3)
    y += 5

    # ---- KPI strip
    kpi_h = 48
    d.rectangle([x0, y, x1, y + kpi_h], fill=PAPER2, outline=INK, width=1)
    cell_w = CW / len(KPI)
    for i, (num, label) in enumerate(KPI):
        cx = x0 + i * cell_w
        if i:
            d.line([(cx, y + 6), (cx, y + kpi_h - 6)], fill=(200, 190, 170), width=1)
        nf = F_SANS_BLACK(25)
        d.text((cx + cell_w / 2 - d.textlength(num, font=nf) / 2, y + 2),
               num, font=nf, fill=RED if i % 2 == 0 else INK)
        lf = F_SANS_B(8)
        d.text((cx + cell_w / 2 - d.textlength(label, font=lf) / 2, y + 32),
               label, font=lf, fill=INK2)
    y += kpi_h + 5

    # ---- UTC timeline strip
    tl_h = 28
    d.rectangle([x0, y, x1, y + tl_h], fill=DARK)
    d.text((x0 + 8, y + 7), "THE DAY IN UTC", font=F_SANS_BLACK(11),
           fill=(252, 214, 110))
    tx = x0 + 128
    seg = (CW - 128 - 8) / len(TIMELINE)
    tf2 = F_SANS_B(9)
    for i, (t, label) in enumerate(TIMELINE):
        cx = tx + i * seg
        d.ellipse([cx, y + 10, cx + 8, y + 18], fill=(252, 214, 110))
        if i < len(TIMELINE) - 1:
            d.line([(cx + 8, y + 14), (cx + seg, y + 14)],
                   fill=(120, 140, 170), width=1)
        d.text((cx + 12, y + 3), t, font=F_SANS_BLACK(10), fill=(255, 255, 255))
        d.text((cx + 12, y + 15), label, font=tf2, fill=(200, 210, 225))
    y += tl_h + 5

    # ---- heroes
    hero_h = 222
    hero_w = (CW - 16) / 3
    for i, hero in enumerate(HEROES):
        hx = x0 + i * (hero_w + 8)
        d.rectangle([hx, y, hx + hero_w, y + hero_h], fill=(255, 255, 255),
                    outline=INK, width=1)
        _scene_into(img, HERO_SCENES[hero["scene"]], hx + 1, y + 1,
                    int(hero_w - 2), 112)
        num_badge(d, hx + 16, y + 126, hero["n"])
        hx2 = hx + 30
        d.text((hx2, y + 118), hero["place"], font=F_SANS_B(9), fill=RED)
        hy = y + 132
        hy = draw_wrapped(d, hx + 10, hy, hero["head"], F_SERIF_BLACK(15),
                          INK, hero_w - 20, leading=17)
        hy = draw_wrapped(d, hx + 10, hy + 2, hero["deck"], F_SANS(10),
                          INK2, hero_w - 20, leading=12)
        chip(d, hx + 10, y + hero_h - 15, hero["status"])
        src = hero["src"]
        sf3 = F_SANS(8)
        d.text((hx + hero_w - 10 - d.textlength(src, font=sf3), y + hero_h - 15),
               src, font=sf3, fill=INK2)
    y += hero_h + 6

    # ---- section header: ten more
    rule(d, x0, y + 8, x1, 1)
    d.text((x0, y), "TEN MORE, IN PICTURES", font=F_SANS_BLACK(12), fill=INK)
    d.text((x1 - d.textlength("each drawn from the day's reporting",
                              font=F_SANS(9)), y + 1),
           "each drawn from the day's reporting", font=F_SANS(9), fill=INK2)
    y += 19

    # ---- ten small panels, 5 x 2
    panel_w = (CW - 4 * 8) / 5
    panel_h = 120
    scene_h = 44
    for row in range(2):
        for col in range(5):
            p = PANELS[row * 5 + col]
            px = x0 + col * (panel_w + 8)
            py = y + row * (panel_h + 6)
            d.rectangle([px, py, px + panel_w, py + panel_h],
                        fill=(255, 255, 255), outline=INK, width=1)
            _scene_into(img, MINI_SCENES[p["scene"]], px + 1, py + 1,
                        int(panel_w - 2), scene_h)
            num_badge(d, px + 13, py + scene_h + 12, p["n"], r=8)
            d.text((px + 25, py + scene_h + 5), p["place"], font=F_SANS_B(8),
                   fill=RED)
            ty = draw_wrapped(d, px + 7, py + scene_h + 18, p["head"],
                              F_SERIF_BLACK(10), INK, panel_w - 14, leading=11)
            draw_wrapped(d, px + 7, ty + 1, p["deck"], F_SANS(8), INK2,
                         panel_w - 14, leading=10)
            chip(d, px + 7, py + panel_h - 12, p["status"], f=F_SANS_B(7))
    y += 2 * panel_h + 6 + 6

    # ---- section header: map + more stories
    rule(d, x0, y + 8, x1, 1)
    d.text((x0, y), "WHERE IT HAPPENED \u2014 35 MORE STORIES",
           font=F_SANS_BLACK(12), fill=INK)
    d.text((x1 - d.textlength("numbers on the map match the stories",
                              font=F_SANS(9)), y + 1),
           "numbers on the map match the stories", font=F_SANS(9), fill=INK2)
    y += 19

    # ---- map (left) + list (right, two columns)
    map_w = 296
    map_h = 216
    map_x, map_y = x0, y
    d.rectangle([map_x, map_y, map_x + map_w, map_y + map_h], fill=SEA,
                outline=INK, width=1)

    def project(lon, lat):
        return (map_x + 6 + (lon + 180) / 360 * (map_w - 12),
                map_y + 6 + (90 - lat) / 180 * (map_h - 12))

    for poly in CONTINENTS:
        pts = [project(lon, lat) for lon, lat in poly]
        d.polygon(pts, fill=LAND, outline=LANDLINE)
    for lon in range(-150, 181, 30):
        gx = map_x + 6 + (lon + 180) / 360 * (map_w - 12)
        d.line([(gx, map_y + 6), (gx, map_y + map_h - 6)], fill=(170, 200, 225),
               width=1)
    for s in HEROES + PANELS:
        cx, cy = project(s["lon"], s["lat"])
        num_badge(d, cx, cy, s["n"], r=8)
    for m in MORE:
        if m[1] == "WORLD":
            continue
        cx, cy = project(m[2], m[3])
        d.ellipse([cx - 2, cy - 2, cx + 2, cy + 2], fill=INK,
                  outline=(255, 255, 255))

    # list columns (one line each, place first)
    list_x = map_x + map_w + 12
    list_w = (x1 - list_x)
    col_w = (list_w - 10) / 2
    items = MORE
    half = (len(items) + 1) // 2
    list_bottom = map_y
    for ci, chunk in enumerate([items[:half], items[half:]]):
        cx = list_x + ci * (col_w + 10)
        cy = map_y
        for m in chunk:
            n, place = m[0], m[1]
            head_f = F_SANS_B(9)
            body_f = F_SANS(9)
            line = f"{n}. {place} \u2014 {m[8]}"
            # fit: shrink body font if it would wrap
            if d.textlength(line, font=head_f) > col_w:
                body_f = F_SANS(8)
            d.text((cx, cy), f"{n}.", font=head_f, fill=RED)
            nx = cx + d.textlength(f"{n}. ", font=head_f)
            d.text((nx, cy), place, font=head_f, fill=INK)
            px = nx + d.textlength(place + " \u2014 ", font=head_f)
            d.text((px, cy), m[8], font=body_f, fill=INK)
            cy += 12
        list_bottom = max(list_bottom, cy)
    y = max(map_y + map_h, list_bottom) + 4

    # ---- region legend, full width
    region_counts = {}
    for s in all_stories:
        region_counts[s["region"]] = region_counts.get(s["region"], 0) + 1
    lx = x0
    cols = [RED, (196, 90, 20), BLUE, (110, 60, 140), TEAL,
            (150, 100, 20), (40, 110, 90), INK2]
    for i, reg in enumerate(["North America", "South America", "Europe",
                             "Middle East", "Africa", "Asia", "Oceania",
                             "Global"]):
        cnt = region_counts.get(reg, 0)
        if not cnt:
            continue
        d.rectangle([lx, y, lx + 8, y + 8], fill=cols[i])
        lab = f"{reg} {cnt}"
        d.text((lx + 11, y - 1), lab, font=F_SANS_B(8), fill=INK)
        lx += 11 + d.textlength(lab, font=F_SANS_B(8)) + 12
    y += 14

    # ---- DATE CHECK footer
    dc_h = 40
    d.rectangle([x0, y, x1, y + dc_h], fill=(255, 255, 255), outline=RED, width=1)
    d.text((x0 + 8, y + 4), "DATE CHECK \u2014 LEFT OUT, NOT WEDNESDAY",
           font=F_SANS_BLACK(10), fill=RED)
    d.text((x1 - 8 - d.textlength("NOT YET: " + NOT_YET, font=F_SANS_B(9)), y + 4),
           "NOT YET: " + NOT_YET, font=F_SANS_B(9), fill=INK)
    lo = "  \u00b7  ".join(f"{t} ({dt})" for t, dt in LEFT_OUT)
    lo_lines = wrap(d, lo, F_SANS(9), CW - 16)
    ly = y + 19
    for ln in lo_lines:
        d.text((x0 + 8, ly), ln, font=F_SANS(9), fill=INK2)
        ly += 11
    y += dc_h + 5

    # ---- source line
    src_line = ("SOURCES: Reuters \u00b7 AP \u00b7 AFP \u00b7 BBC \u00b7 Xinhua \u00b7 CMSA \u00b7 "
                "Ofgem \u00b7 ABS \u00b7 UN Women \u00b7 BEA. Every story first reported Wed 25 Nov 2026. "
                "All drawings are original illustrations for this page.")
    draw_wrapped(d, x0, y, src_line, F_SANS(8), INK2, CW, leading=10)
    y += 20
    key_line = ("CONFIRMED = verified by a named source   \u00b7   REPORTED = reported, "
                "details unconfirmed   \u00b7   CLAIM = one side's claim, not independently confirmed")
    d.text((x0, y), key_line, font=F_SANS_B(8), fill=INK2)
    y += 12
    print(f"layout bottom y={y} (limit 1024)")
    return img


def main():
    img = build()
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    img.save(OUT, format="PNG", optimize=True)
    size = os.path.getsize(OUT)
    print(f"wrote {OUT} {img.size[0]}x{img.size[1]} {size} bytes")


if __name__ == "__main__":
    main()
