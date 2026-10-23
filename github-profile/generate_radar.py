"""Generate the neon radar banner for the BalalaikaDev GitHub profile README.

Each project is a "contact" on the scope. The sweep is a pure SMIL animation
(GitHub strips scripts from README images), and every blip flares exactly when
the beam crosses it.

Usage: python generate_radar.py [out.svg]
"""
import math
import sys

# Palette lifted from the Runi Shell (shell/frontend/style.css)
BG = "#06070f"
SURFACE = "#0a0b1a"
GRID = "#18e0ff"      # primary cyan
BEAM = "#ff2e97"      # accent magenta
TEXT = "#ccd6f0"
DIM = "#6e79a8"

SWEEP_SECONDS = 6

# bearing: degrees clockwise from north; range: 0..1 of scope radius;
# size scales the blip, so the flagship repo reads first
CONTACTS = [
    {"name": "runi-os", "tag": "OSINT PLATFORM", "bearing": 52, "range": 0.62, "size": 1.4, "color": "#fcee0a"},
    {"name": "kindle-ai-export", "tag": "READER // FORK", "bearing": 218, "range": 0.48, "size": 0.7, "color": "#00ff9c"},
]

W, H = 860, 400
CX, CY, R = 200, 200, 170
FONT = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"


def polar(bearing, frac):
    a = math.radians(bearing - 90)
    return CX + R * frac * math.cos(a), CY + R * frac * math.sin(a)


def wedge(start, end):
    x1, y1 = polar(start, 1)
    x2, y2 = polar(end, 1)
    return f"M{CX},{CY} L{x1:.1f},{y1:.1f} A{R},{R} 0 0 1 {x2:.1f},{y2:.1f} Z"


def build():
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" font-family="{FONT}">']
    out.append(f"""<defs>
  <radialGradient id="scope" cx="50%" cy="50%" r="50%">
    <stop offset="0" stop-color="#11132b"/><stop offset="1" stop-color="{BG}"/>
  </radialGradient>
  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
    <feGaussianBlur stdDeviation="3" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <clipPath id="clip"><circle cx="{CX}" cy="{CY}" r="{R}"/></clipPath>
  <pattern id="scan" width="4" height="4" patternUnits="userSpaceOnUse">
    <rect width="4" height="1" fill="#ffffff" opacity="0.025"/>
  </pattern>
</defs>""")
    out.append(f'<rect width="{W}" height="{H}" rx="14" fill="{BG}"/>')
    out.append(f'<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="13" fill="none" stroke="{GRID}" stroke-opacity="0.25"/>')

    # scope + grid
    out.append(f'<circle cx="{CX}" cy="{CY}" r="{R}" fill="url(#scope)" stroke="{GRID}" stroke-opacity="0.7" filter="url(#glow)"/>')
    for f in (0.25, 0.5, 0.75):
        out.append(f'<circle cx="{CX}" cy="{CY}" r="{R*f:.0f}" fill="none" stroke="{GRID}" stroke-opacity="0.18" stroke-dasharray="2 4"/>')
    out.append(f'<path d="M{CX-R},{CY} H{CX+R} M{CX},{CY-R} V{CY+R}" stroke="{GRID}" stroke-opacity="0.15"/>')
    for b in range(0, 360, 10):
        x1, y1 = polar(b, 1)
        x2, y2 = polar(b, 0.95 if b % 30 else 0.9)
        out.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{GRID}" stroke-opacity="0.45"/>')

    # sweep: a fading magenta trail behind a bright leading edge, rotating clockwise
    out.append(f'<g clip-path="url(#clip)"><g>')
    out.append(f'<animateTransform attributeName="transform" type="rotate" from="0 {CX} {CY}" to="360 {CX} {CY}" dur="{SWEEP_SECONDS}s" repeatCount="indefinite"/>')
    steps = 18
    for i in range(steps):
        start, end = -(i + 1) * 3, -i * 3
        out.append(f'<path d="{wedge(start, end)}" fill="{BEAM}" opacity="{0.38 * (1 - i / steps) ** 2:.3f}"/>')
    x, y = polar(0, 1)
    out.append(f'<line x1="{CX}" y1="{CY}" x2="{x:.1f}" y2="{y:.1f}" stroke="#ff63b4" stroke-width="2" filter="url(#glow)"/>')
    out.append("</g></g>")
    out.append(f'<circle cx="{CX}" cy="{CY}" r="3" fill="{BEAM}" filter="url(#glow)"/>')

    # contacts: flare when the beam passes, then decay
    for c in CONTACTS:
        x, y = polar(c["bearing"], c["range"])
        begin = f'{SWEEP_SECONDS * c["bearing"] / 360:.2f}s'
        anim = (f'<animate attributeName="opacity" values="1;0.25;0.25" keyTimes="0;0.75;1" '
                f'dur="{SWEEP_SECONDS}s" begin="{begin}" repeatCount="indefinite"/>')
        out.append(f'<g opacity="0.25">{anim}')
        k = c["size"]
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{5*k:.1f}" fill="{c["color"]}" filter="url(#glow)"/>')
        out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{11*k:.1f}" fill="none" stroke="{c["color"]}" stroke-opacity="0.6"/>')
        out.append(f'<text x="{x+11*k+5:.1f}" y="{y+4:.1f}" font-size="{max(10, 11*k**0.5):.0f}" fill="{c["color"]}">{c["name"]}</text>')
        out.append("</g>")

    # readout panel
    px = 420
    out.append(f'<text x="{px}" y="64" font-size="30" font-weight="700" fill="{TEXT}" filter="url(#glow)">BALALAIKA<tspan fill="{BEAM}">DEV</tspan></text>')
    out.append(f'<text x="{px}" y="90" font-size="12" fill="{GRID}" letter-spacing="2">SIGINT CONSOLE // SCOPE ACTIVE<tspan>_<animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></tspan></text>')
    out.append(f'<line x1="{px}" y1="108" x2="{W-40}" y2="108" stroke="{GRID}" stroke-opacity="0.3"/>')
    out.append(f'<text x="{px}" y="134" font-size="11" fill="{DIM}" letter-spacing="1">CONTACTS TRACKED: {len(CONTACTS):02d}</text>')
    y = 168
    for i, c in enumerate(CONTACTS):
        out.append(f'<rect x="{px}" y="{y-16}" width="{W-40-px}" height="42" rx="6" fill="{SURFACE}" stroke="{c["color"]}" stroke-opacity="0.35"/>')
        out.append(f'<circle cx="{px+16}" cy="{y+5}" r="4" fill="{c["color"]}" filter="url(#glow)"/>')
        out.append(f'<text x="{px+32}" y="{y+2}" font-size="14" font-weight="700" fill="{c["color"]}">{c["name"]}</text>')
        out.append(f'<text x="{px+32}" y="{y+18}" font-size="10" fill="{DIM}" letter-spacing="1">{c["tag"]} · BRG {c["bearing"]:03d}° · RNG {c["range"]:.2f}</text>')
        y += 56
    out.append(f'<text x="{px}" y="{H-36}" font-size="10" fill="{DIM}" letter-spacing="1">runi osint // 45+ sources // one graph</text>')

    out.append(f'<rect width="{W}" height="{H}" rx="14" fill="url(#scan)"/>')
    out.append("</svg>")
    return "\n".join(out)


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "radar.svg"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(build())
    print(f"wrote {path}")
