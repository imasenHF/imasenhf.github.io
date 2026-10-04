"""Generate the homepage SVG from the supplied EPR CSV and unchanged structure.
All spectral points share one linear mapping; no peak-specific scaling or smoothing.
Run from the repository root: python3 scripts/build_plastocyanin_visual.py
"""
from pathlib import Path
import csv, base64
root = Path(__file__).resolve().parents[1]
assets = root / 'assets/images/plastocyanin'
rows = list(csv.DictReader((assets / 'plastocyanin_Xband.csv').open()))
points = [(float(r['B_mT']), float(r['Derivative_normalized'])) for r in rows]
# Fixed coordinates: 275–350 mT; normalized derivative, one common scale.
x0, x1, baseline, scale = 60, 580, 407, 150
path = ' '.join(f'{x0+(b-275)/75*(x1-x0):.3f},{baseline-scale*y:.3f}' for b,y in points)
protein = base64.b64encode((assets/'config6.png').read_bytes()).decode()
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 640 660" role="img" aria-labelledby="title desc">
<title id="title">Plastocyanin structure and simulated EPR spectrum</title>
<desc id="desc">The unchanged protein structure overlaps the simulated EPR line. All 4096 data points use uniform amplitude scaling; axes are omitted for the homepage illustration.</desc>

<image x="-135" y="-20" width="930" height="728.38" xlink:href="data:image/png;base64,{protein}"/>
<g fill="none" stroke-linejoin="round" stroke-linecap="round"><polyline points="{path}" stroke="#ffffff" stroke-width="9.5"/><polyline points="{path}" stroke="#f0be32" stroke-width="3.5"/></g></svg>'''
(assets/'plastocyanin-composition.svg').write_text(svg)
print(f'Generated SVG: {len(points)} points; normalized range {min(y for _,y in points):.6f} to {max(y for _,y in points):.6f}')
