#!/usr/bin/env python3
"""One-off authoring helper: writes the static HTML files. Not part of the site."""
import math, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500'
         '&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&display=swap">')

# ---------------------------------------------------------------- motifs

def motif_kp():
    ticks = []
    for i in range(11):
        y = 296 - i * 26
        x1 = 140 if i in (0, 5, 10) else 152
        ticks.append(f'<line x1="{x1}" y1="{y}" x2="170" y2="{y}"/>')
    return f'''<svg class="motif" viewBox="0 0 400 400" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" focusable="false">
  <rect class="kp-level anim" x="176" y="112" width="48" height="200" fill="currentColor" stroke="none"/>
  <rect x="176" y="20" width="48" height="292"/>
  <circle cx="200" cy="346" r="42" fill="currentColor"/>
  <g>{"".join(ticks)}</g>
  <text x="132" y="300" text-anchor="end">E01</text>
  <text x="132" y="40" text-anchor="end">E11</text>
  <line x1="232" y1="150" x2="300" y2="150"/><text x="310" y="154">CONV</text>
  <line x1="232" y1="200" x2="300" y2="200"/><text x="310" y="204">ARPU</text>
  <line x1="232" y1="250" x2="300" y2="250"/><text x="310" y="254">RET</text>
</svg>'''

def motif_emcd():
    lanes, flows, heads = [], [], []
    for i in range(6):
        y = 40 + i * 40
        d = f"M40 {y} C 170 {y}, 190 140, 290 140"
        lanes.append(f'<path d="{d}" stroke-opacity="0.35"/>')
        flows.append(f'<path class="emcd-flow anim" d="{d}"/>')
        heads.append(f'<rect x="32" y="{y-4}" width="8" height="8" fill="currentColor" stroke="none"/>'
                     f'<text x="24" y="{y+4}" text-anchor="end">L{i+1}</text>')
    grid = []
    for n in range(15):
        c, r = n % 5, n // 5
        grid.append(f'<rect x="{40 + c*30}" y="{286 + r*30}" width="22" height="22" fill="currentColor" stroke="none"/>')
    return f'''<svg class="motif" viewBox="0 0 400 400" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" focusable="false">
  {"".join(lanes)}
  {"".join(flows)}
  {"".join(heads)}
  <line x1="290" y1="140" x2="352" y2="140" stroke-width="5"/>
  <rect x="352" y="126" width="28" height="28" fill="currentColor" stroke="none"/>
  <text x="366" y="176" text-anchor="middle">PROD</text>
  <g>{"".join(grid)}</g>
  <text x="208" y="302">15 DECISIONS</text>
  <text x="208" y="322" opacity="0.7">CLEANUP ≠ REDESIGN</text>
</svg>'''

QR = ["1110111", "1011101", "1110111", "0101001", "1110110", "1011011", "1110101"]

def qr_cells(ox, oy, s, cls=""):
    out = []
    for r, row in enumerate(QR):
        for c, v in enumerate(row):
            if v == "1":
                out.append(f'<rect{cls} x="{ox + c*s}" y="{oy + r*s}" width="{s}" height="{s}"/>')
    return "".join(out)

def motif_jet():
    labels = []
    for k, t in enumerate(["00", "15", "30", "45", "60", "75"]):
        a = math.radians(k * 60)
        x, y = 200 + 182 * math.sin(a), 200 - 182 * math.cos(a)
        labels.append(f'<text x="{x:.1f}" y="{y+4:.1f}" text-anchor="middle">{t}</text>')
    circ = 2 * math.pi * 150
    seg = circ / 6
    return f'''<svg class="motif" viewBox="0 0 400 400" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" focusable="false">
  <circle cx="200" cy="200" r="150" stroke-width="20" stroke-dasharray="{seg-8:.2f} 8" stroke-dashoffset="-4" transform="rotate(-90 200 200)"/>
  <circle cx="200" cy="200" r="118" stroke-opacity="0.35" stroke-width="1"/>
  {"".join(labels)}
  <g fill="currentColor" stroke="none">{qr_cells(158, 158, 12)}</g>
  <g class="jet-orbit anim"><circle cx="200" cy="50" r="9" class="paper-fill" stroke="currentColor" stroke-width="2"/></g>
</svg>'''

SHIRT = "M40 0 L70 0 Q90 20 110 0 L140 0 L180 42 L152 66 L140 54 L140 200 L40 200 L40 54 L28 66 L0 42 Z"

def motif_om():
    return f'''<svg class="motif" viewBox="0 0 400 400" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true" focusable="false">
  <text x="40" y="28">ORIGINAL</text>
  <rect x="40" y="40" width="210" height="270" stroke-dasharray="6 6"/>
  <line class="om-scan anim" x1="40" y1="44" x2="250" y2="44" stroke-width="1.5"/>
  <path d="{SHIRT}" transform="translate(186 92)" fill="currentColor" stroke="none"/>
  <text x="270" y="316">CUT-OUT</text>
  <g stroke-width="1.5">
    <rect x="40" y="334" width="58" height="14"/><rect x="106" y="334" width="42" height="14" fill="currentColor"/><rect x="156" y="334" width="72" height="14"/>
    <rect x="40" y="356" width="46" height="14"/><rect x="94" y="356" width="78" height="14"/><rect x="180" y="356" width="34" height="14"/>
  </g>
  <text x="40" y="394">TAXONOMY</text>
</svg>'''

MOTIFS = {"kp": motif_kp, "emcd": motif_emcd, "jet": motif_jet, "om": motif_om}

# ---------------------------------------------------------------- diagrams

ARROW = ('<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
         'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="#0F0F0D"/></marker></defs>')

def dg_kp():
    stages = [(60, "01 First open"), (276, "02 Onboarding"), (492, "03 Trial"), (708, "04 Purchase"), (924, "05 Retention")]
    s = [f'<text x="{x+8}" y="36">{t.upper()}</text>' for x, t in stages]
    s += [f'<line class="ln-thin" x1="{x}" y1="20" x2="{x}" y2="420"/>' for x, _ in stages[1:]]
    exps = []
    for i in range(11):
        x = 300 + i * 60
        exps.append(f'<line class="ln" x1="{x}" y1="100" x2="{x}" y2="134"/>'
                    f'<text class="t-sm" x="{x}" y="90" text-anchor="middle">E{i+1:02d}</text>')
    rows = [(248, "Conversion", 276, 924), (304, "ARPU", 708, 1140), (360, "Retention", 924, 1140)]
    r = []
    for y, name, a, b in rows:
        r.append(f'<text x="60" y="{y+15}">{name.upper()}</text>'
                 f'<line class="ln-thin" x1="170" y1="{y+10}" x2="1140" y2="{y+10}"/>'
                 f'<rect class="box-c" x="{a}" y="{y}" width="{b-a}" height="20"/>')
    return f'''<svg class="dg" viewBox="0 0 1200 470" role="img" aria-labelledby="dg-title dg-desc">
  <title id="dg-title">Thermometer timeline of the subscription path</title>
  <desc id="dg-desc">Five stages from first open to retention. Eleven experiments, E01 to E11, are placed across onboarding, trial and purchase. Conversion is read from onboarding through purchase, ARPU from purchase on, retention after purchase. Onboarding purchase conversion rose 21 percent.</desc>
  {"".join(s)}
  <text class="t-sm t-muted" x="60" y="90">11 EXPERIMENTS</text>
  {"".join(exps)}
  <rect class="fill-c" x="110" y="138" width="650" height="28"/>
  <rect class="ln" x="110" y="138" width="1030" height="28"/>
  <circle class="box-c" cx="84" cy="152" r="30"/>
  <text class="t-sm t-muted" x="110" y="190">INTENT TEMPERATURE ALONG THE PATH</text>
  {"".join(r)}
  <line class="ln-dash" x1="384" y1="268" x2="384" y2="404"/>
  <rect class="fill-ink" x="378" y="252" width="12" height="12"/>
  <text class="t-lg" x="396" y="440">+21%</text>
  <text class="t-sm" x="478" y="436">ONBOARDING PURCHASE CONVERSION</text>
</svg>'''

def dg_emcd():
    parts = []
    for i in range(6):
        y = 40 + i * 64
        parts.append(f'<rect class="box" x="40" y="{y}" width="180" height="44"/>'
                     f'<text x="58" y="{y+27}">LINEAGE {i+1:02d}</text>'
                     f'<path class="ln" d="M220 {y+22} C 330 {y+22}, 320 222, 420 222"/>')
    ledger = []
    for n in range(15):
        x = 40 + n * 40
        ledger.append(f'<rect class="box-c" x="{x}" y="500" width="32" height="32"/>'
                      f'<text class="t-sm" x="{x+16}" y="520" text-anchor="middle">{n+1:02d}</text>')
    return f'''<svg class="dg" viewBox="0 0 1200 560" role="img" aria-labelledby="dg-title dg-desc">
  <title id="dg-title">Design-system audit and migration map</title>
  <desc id="dg-desc">Six design-system lineages converge into one audit that reads from production, the source of truth. The audit feeds one migration plan, which splits into two separate tracks: cleanup and redesign. Fifteen design-system decisions are documented.</desc>
  {ARROW}
  {"".join(parts)}
  <rect class="box-ink" x="420" y="192" width="170" height="60"/>
  <text class="t-md t-paper" x="440" y="229">Audit</text>
  <line class="ln" x1="590" y1="222" x2="656" y2="222" marker-end="url(#ah)"/>
  <rect class="box-c" x="660" y="192" width="210" height="60"/>
  <text class="t-md" x="680" y="229">Migration plan</text>
  <path class="ln" d="M870 222 C 910 222, 910 110, 946 110" marker-end="url(#ah)"/>
  <path class="ln-dash" d="M870 222 C 910 222, 910 334, 946 334" marker-end="url(#ah)"/>
  <rect class="box" x="950" y="80" width="210" height="60"/>
  <text class="t-md" x="970" y="107">Cleanup</text>
  <text class="t-sm t-muted" x="970" y="127">CONSOLIDATE WHAT EXISTS</text>
  <rect class="box-dash" x="950" y="304" width="210" height="60"/>
  <text class="t-md" x="970" y="331">Redesign</text>
  <text class="t-sm t-muted" x="970" y="351">SEPARATE TRACK</text>
  <line class="ln-dash" x1="1055" y1="150" x2="1055" y2="202"/>
  <text class="t-sm" x="1055" y="226" text-anchor="middle">KEPT SEPARATE</text>
  <line class="ln-dash" x1="1055" y1="242" x2="1055" y2="294"/>
  <line class="ln-dash" x1="505" y1="252" x2="505" y2="424"/>
  <text class="t-sm t-muted" x="517" y="344">READS FROM</text>
  <line class="ln-bold" x1="40" y1="430" x2="1160" y2="430"/>
  <text x="40" y="462">PRODUCTION — SOURCE OF TRUTH</text>
  {"".join(ledger)}
  <text class="t-md" x="660" y="524">15 documented decisions</text>
</svg>'''

def dg_jet():
    cx, cy, r = 680, 280, 160
    circ = 2 * math.pi * r
    seg = circ / 6
    labels = []
    for k, t in enumerate(["0 MIN", "15", "30", "45", "60", "75"]):
        a = math.radians(k * 60)
        x, y = cx + 206 * math.sin(a), cy - 206 * math.cos(a)
        labels.append(f'<text x="{x:.1f}" y="{y+5:.1f}" text-anchor="middle">{t}</text>')
    venues = []
    for n in range(6):
        x = 940 + n * 38
        venues.append(f'<rect class="box-c" x="{x}" y="410" width="30" height="30"/>')
    def qr_node(y, label):
        return (f'<rect class="box" x="40" y="{y}" width="180" height="52"/>'
                f'<g class="fill-ink">{qr_cells(54, y+12, 4)}</g>'
                f'<text x="96" y="{y+31}">{label}</text>')
    return f'''<svg class="dg" viewBox="0 0 1200 520" role="img" aria-labelledby="dg-title dg-desc">
  <title id="dg-title">Jetable booking system</title>
  <desc id="dg-desc">QR codes at the table and at the door lead guests into the guest app. The guest app and web booking write into one booking cycle of 90 minutes, split into six 15-minute slots. The staff app runs the same schedule. Booking is live in six venues.</desc>
  {ARROW}
  <text class="t-sm t-muted" x="40" y="96">ACQUISITION</text>
  {qr_node(110, "QR · TABLE")}
  {qr_node(190, "QR · DOOR")}
  <path class="ln" d="M220 136 C 260 136, 260 164, 296 164" marker-end="url(#ah)"/>
  <path class="ln" d="M220 216 C 260 216, 260 184, 296 184" marker-end="url(#ah)"/>
  <text class="t-sm t-muted" x="300" y="126">SURFACES</text>
  <rect class="box-c" x="300" y="142" width="180" height="64"/>
  <text class="t-md" x="318" y="181">Guest app</text>
  <rect class="box" x="300" y="360" width="180" height="64"/>
  <text class="t-md" x="318" y="399">Web booking</text>
  <path class="ln" d="M480 174 C 495 174, 488 252, 500 252" marker-end="url(#ah)"/>
  <path class="ln" d="M480 392 C 495 392, 488 308, 500 308" marker-end="url(#ah)"/>
  <circle class="ln-thin" cx="{cx}" cy="{cy}" r="{r+17}"/>
  <circle class="ln-thin" cx="{cx}" cy="{cy}" r="{r-17}"/>
  <circle class="ring-c" cx="{cx}" cy="{cy}" r="{r}" stroke-width="34" stroke-dasharray="{seg-8:.2f} 8" stroke-dashoffset="-4" transform="rotate(-90 {cx} {cy})"/>
  {"".join(labels)}
  <text class="t-lg" x="{cx}" y="{cy-2}" text-anchor="middle">Booking</text>
  <text class="t-sm" x="{cx}" y="{cy+26}" text-anchor="middle">6 × 15-MIN SLOTS</text>
  <text class="t-sm" x="{cx}" y="{cy+46}" text-anchor="middle">90-MIN CYCLE</text>
  <path class="ln" d="M936 280 L 862 280" marker-end="url(#ah)" marker-start="url(#ah)"/>
  <rect class="box-ink" x="940" y="248" width="180" height="64"/>
  <text class="t-md t-paper" x="958" y="287">Staff app</text>
  <line class="ln-thin" x1="1030" y1="312" x2="1030" y2="410"/>
  {"".join(venues)}
  <text x="940" y="470">6 VENUES · BOOKING LIVE</text>
  <text class="t-sm t-muted" x="1160" y="40" text-anchor="end">MARKETPLACE · GUESTS ↔ VENUES</text>
</svg>'''

def dg_om():
    return f'''<svg class="dg" viewBox="0 0 1200 450" role="img" aria-labelledby="dg-title dg-desc">
  <title id="dg-title">Photo-to-wardrobe pipeline</title>
  <desc id="dg-desc">A photo is saved immediately, then enhanced with background removal. On success the cut-out is used; if it fails, the original photo is kept. Both paths are classified into a fixed taxonomy and land in the wardrobe. One feature went from plan to shipped in two days.</desc>
  {ARROW}
  <rect class="box" x="40" y="170" width="120" height="70"/>
  <text class="t-md" x="58" y="212">Photo</text>
  <line class="ln" x1="160" y1="205" x2="196" y2="205" marker-end="url(#ah)"/>
  <rect class="box-c" x="200" y="170" width="150" height="70"/>
  <text class="t-md t-on" x="218" y="203">Save</text>
  <text class="t-sm t-on" x="218" y="225">STORED AT ONCE</text>
  <line class="ln" x1="350" y1="205" x2="386" y2="205" marker-end="url(#ah)"/>
  <rect class="box" x="390" y="170" width="180" height="70"/>
  <text class="t-md" x="408" y="203">Enhance</text>
  <text class="t-sm t-muted" x="408" y="225">BACKGROUND REMOVAL</text>
  <path class="ln" d="M570 205 C 600 205, 600 102, 626 102" marker-end="url(#ah)"/>
  <path class="ln-dash" d="M570 205 C 600 205, 600 312, 626 312" marker-end="url(#ah)"/>
  <text class="t-sm t-muted" x="588" y="154" text-anchor="end">SUCCESS</text>
  <text class="t-sm t-muted" x="588" y="262" text-anchor="end">FAILS</text>
  <rect class="box" x="630" y="70" width="160" height="64"/>
  <path d="{SHIRT}" transform="translate(646 84) scale(0.18)" class="fill-c"/>
  <text class="t-md" x="686" y="110">Cut-out</text>
  <rect class="box-dash" x="630" y="280" width="160" height="64"/>
  <text class="t-md" x="648" y="309">Original kept</text>
  <text class="t-sm t-muted" x="648" y="330">FALLBACK</text>
  <path class="ln" d="M790 102 C 820 102, 820 198, 846 198" marker-end="url(#ah)"/>
  <path class="ln" d="M790 312 C 820 312, 820 212, 846 212" marker-end="url(#ah)"/>
  <rect class="box-ink" x="850" y="170" width="150" height="70"/>
  <text class="t-md t-paper" x="868" y="203">Taxonomy</text>
  <text class="t-sm t-paper" x="868" y="225">CONSTRAINS AI</text>
  <line class="ln" x1="1000" y1="205" x2="1036" y2="205" marker-end="url(#ah)"/>
  <rect class="box" x="1040" y="170" width="130" height="70"/>
  <text class="t-md" x="1058" y="212">Wardrobe</text>
  <line class="ln" x1="200" y1="284" x2="570" y2="284"/>
  <line class="ln" x1="200" y1="276" x2="200" y2="292"/>
  <line class="ln" x1="570" y1="276" x2="570" y2="292"/>
  <text class="t-sm" x="200" y="312">SAVE FIRST · ENHANCE LATER</text>
  <text class="t-sm t-muted" x="40" y="378">ONE FEATURE · PLAN → SHIPPED</text>
  <rect class="fill-c" x="40" y="396" width="520" height="8"/>
  <line class="ln" x1="40" y1="388" x2="40" y2="412"/>
  <line class="ln" x1="300" y1="388" x2="300" y2="412"/>
  <line class="ln" x1="560" y1="388" x2="560" y2="412"/>
  <text class="t-sm" x="40" y="432">PLAN</text>
  <text class="t-sm" x="300" y="432" text-anchor="middle">DAY 1</text>
  <text class="t-sm" x="560" y="432" text-anchor="end">DAY 2 · SHIPPED</text>
</svg>'''

DIAGRAMS = {"kp": dg_kp, "emcd": dg_emcd, "jet": dg_jet, "om": dg_om}

# ---------------------------------------------------------------- content

CASES = [
    dict(
        key="kp", slug="kinopoisk-growth", num="01", name="Kinopoisk Growth", short="Kinopoisk",
        kind="Subscription growth", bar="Experiments · Onboarding · Trial",
        manifesto="Growth experiments.",
        context="Subscription growth for a streaming service, run as a program of experiments across trial and onboarding — each one read against conversion, ARPU and retention.",
        principles=[("Map the moment.", "A thermometer timeline of trial and onboarding shows where intent rises and cools."),
                    ("Read three numbers.", "Conversion, ARPU and retention together — a win on one can’t hide a loss on another."),
                    ("Keep the losses.", "11 experiments, wins and losses both on the record.")],
        figure="+21%", figure_label="Onboarding purchase conversion", strip_out="+21% onboarding conversion",
        thesis="Growth is a sequence of <em>honest</em> experiments.",
        standfirst="Subscription growth at Kinopoisk: a sequence of experiments across the trial and onboarding path, measured on conversion, ARPU and retention.",
        situation_lead="Subscription growth is decided in a narrow window — <em>between first open and first payment.</em>",
        situation_body="Trial and onboarding were where intent was won or lost. Every change there moved more than one number: a push for conversion could cost ARPU, and an easier entry could cost retention. The work needed a map of that window, and a way to test inside it without fooling ourselves.",
        facts=[("Role", "Product design and growth — subscription experiments"),
               ("Scope", "Trial and onboarding path, purchase moments"),
               ("Metrics", "Conversion, ARPU, retention"),
               ("Volume", "11 experiments, wins and losses")],
        decisions=[("Draw the trial as a thermometer timeline", "Every step from first open to retention laid out on one line, with intent as temperature. Each experiment targets a specific point on that line, not “onboarding” in general."),
                   ("Read conversion, ARPU and retention together", "A variant only counts as a win if it doesn’t borrow from the other two. Three metrics, one verdict."),
                   ("Keep the losses on the record", "Across 11 experiments, the losing variants stayed documented next to the winners. A clear loss narrows the next hypothesis."),
                   ("Ship the winner into onboarding", "The winning onboarding variant shipped: purchase conversion from onboarding up 21%.")],
        caption="Fig. 1 — Thermometer timeline: 11 experiments placed on the trial and onboarding path, and where each metric is read.",
        outcome_small="Onboarding purchase conversion",
        outcome_list=[("Experiments run", "11"), ("Record", "Wins and losses documented"), ("Read against", "Conversion · ARPU · Retention")],
        throughline="Experiments teach one rule: <em>trust what is measured in production.</em> At EMCD the same rule became the foundation of a design system.",
    ),
    dict(
        key="emcd", slug="emcd", num="02", name="EMCD", short="EMCD",
        kind="Design systems", bar="Head of Product Designers · Mining BU",
        manifesto="<em>Design systems.</em>",
        context="Six design-system lineages were living in one product. As Head of Product Designers for the Mining business unit, I ran the audit and the migration plan.",
        principles=[("Production is the source of truth.", "Audit what ships, not what the files claim."),
                    ("Separate cleanup from redesign.", "Two projects with different risk, never one."),
                    ("Write decisions down.", "Every rule gets a record, not a meeting.")],
        figure="15", figure_label="Documented design-system decisions", strip_out="15 system decisions",
        thesis="Six lineages. One system, <em>starting from production.</em>",
        standfirst="As Head of Product Designers for EMCD’s Mining business unit, I audited six co-existing design-system lineages and turned them into a migration plan.",
        situation_lead="One product, <em>six design-system lineages</em> — each with its own logic, none of them the system.",
        situation_body="Several generations of components and rules lived side by side in the product. Declaring a new system from scratch would only have produced lineage number seven. The way forward had to start from what users actually see.",
        facts=[("Role", "Head of Product Designers"),
               ("Unit", "Mining business unit"),
               ("Scope", "Design-system audit, migration plan, decision record"),
               ("Baseline", "Production as the source of truth")],
        decisions=[("Production is the source of truth", "The audit started from what is live, not from design files. What ships is what users see, so it is the baseline every lineage is measured against."),
                   ("Audit before migrating", "All six lineages were mapped before anything moved. The migration plan follows from the audit, not the other way round."),
                   ("Separate cleanup from redesign", "Consolidating what exists and changing how it looks are different projects with different risk. Mixing them turns a cleanup into an endless redesign."),
                   ("Write every decision down", "15 design-system decisions documented, so the system keeps its reasoning when people and priorities change.")],
        caption="Fig. 1 — Six lineages audited against production, one migration plan, cleanup and redesign kept on separate tracks.",
        outcome_small="Documented design-system decisions",
        outcome_list=[("Lineages audited", "6"), ("Source of truth", "Production"), ("Plan", "Audit → migration; cleanup separate from redesign")],
        throughline="A design system is only as strong as the decisions it records. <em>Jetable asked for the same discipline</em> — in a live marketplace, as a co-founder.",
    ),
    dict(
        key="jet", slug="jetable", num="03", name="Jetable", short="Jetable",
        kind="Marketplace", bar="Co-founder · Hospitality booking",
        manifesto="Marketplaces.",
        context="A hospitality booking marketplace I co-founded: a guest app, a staff app and web booking, built around one shared schedule.",
        principles=[("One booking, three surfaces.", "Guest app, staff app and web booking share one reservation model."),
                    ("Time as a grid.", "15-minute slots inside a 90-minute cycle — legible to guests, runnable for staff."),
                    ("Acquire in the room.", "QR codes on tables and doors turn walk-ins into users.")],
        figure="6", figure_label="Venues with booking live", strip_out="6 venues live",
        thesis="A marketplace is built <em>table by table.</em>",
        standfirst="I co-founded Jetable, a hospitality booking marketplace: a guest app, a staff app and web booking, with booking live across six venues.",
        situation_lead="A marketplace needs both sides at once — <em>and in hospitality, both sides meet in the room.</em>",
        situation_body="Guests want a table without friction; venues want a schedule they can run on a busy night. The product had to serve both across three surfaces, and bring its own demand in through the door.",
        facts=[("Role", "Co-founder"),
               ("Model", "Hospitality booking marketplace"),
               ("Surfaces", "Guest app · Staff app · Web booking"),
               ("Status", "Booking live in 6 venues")],
        decisions=[("One reservation model, three surfaces", "Guest app, staff app and web booking all read and write the same booking, so what a guest sees and what staff see can’t drift apart."),
                   ("15-minute slots, 90-minute cycle", "Time is a grid: bookable starts every 15 minutes, a table cycle of 90. Simple for guests to read, strict enough for staff to run."),
                   ("Acquire at the table and the door", "QR codes on tables and at the entrance turn people already in the venue into app users. Acquisition happens where the product is used."),
                   ("A marketplace, not a tool", "Venues bring supply, guests bring demand, and the platform holds the schedule between them.")],
        caption="Fig. 1 — Acquisition, surfaces and the 90-minute booking cycle split into six 15-minute slots.",
        outcome_small="Venues with booking live",
        outcome_list=[("Surfaces", "Guest app, staff app, web booking"), ("Booking grid", "15-min slots · 90-min cycle"), ("Acquisition", "QR at table and door")],
        throughline="Running a marketplace made speed a design constraint. <em>OutfitMe takes that to its limit:</em> one person, an AI pipeline, very short loops.",
    ),
    dict(
        key="om", slug="outfitme", num="04", name="OutfitMe", short="OutfitMe",
        kind="AI product", bar="Solo · In active development",
        manifesto="<em>AI products.</em>",
        context="An AI-native wardrobe and outfit builder I’m building solo. Photos go in; a structured wardrobe comes out.",
        principles=[("Save first, enhance later.", "Nothing waits on the model."),
                    ("Fallbacks keep the original.", "If background removal fails, the photo stays."),
                    ("Taxonomy constrains the AI.", "A closed set of answers, not open-ended guesses.")],
        figure="2 days", figure_label="One feature, plan to shipped", strip_out="2 days plan → shipped",
        thesis="Let the model help. <em>Never lose the photo.</em>",
        standfirst="A solo, AI-native wardrobe and outfit builder. Photos become a structured wardrobe; the wardrobe becomes outfits. In active development and tested on device.",
        situation_lead="Every AI step in a wardrobe app can fail. <em>The user shouldn’t be the one who pays for it.</em>",
        situation_body="Turning photos into a usable wardrobe is a chain of fragile steps: capture, background removal, classification. If any of them blocks the save or throws the photo away, people stop adding clothes.",
        facts=[("Role", "Solo — product, design and build"),
               ("Product", "AI-native wardrobe and outfit builder"),
               ("Pipeline", "Photo → wardrobe"),
               ("Status", "Active development, device-tested")],
        decisions=[("Save first, enhance later", "The item is stored the moment the photo is taken. AI enhancement runs afterwards and never blocks the save."),
                   ("Fallback keeps the original", "If background removal fails, the original photo stays in the wardrobe. A plainer image beats a lost item."),
                   ("Taxonomy constrains the AI", "The model classifies into a fixed wardrobe taxonomy — a closed set of answers instead of open-ended guesses."),
                   ("Short loops, real devices", "One feature went from plan to shipped in 2 days, and the app is tested on device, not only in a simulator.")],
        caption="Fig. 1 — Photo-to-wardrobe pipeline: save first, enhance later, fall back to the original, classify into the taxonomy.",
        outcome_small="One feature, plan to shipped",
        outcome_list=[("Pipeline", "Photo → wardrobe"), ("Failure mode", "Original photo kept"), ("Status", "Active development, device-tested")],
        throughline="Constraining a model with a taxonomy is the same move as constraining growth with a metric set: <em>fix the boundaries, then move fast inside them.</em> Which is where this started.",
    ),
]

# ---------------------------------------------------------------- templates

def head(title, desc, prefix, theme):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="{theme}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
{FONTS}
<link rel="stylesheet" href="{prefix}styles.css">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 4 1'%3E%3Crect width='1' height='1' fill='%231D3AE8'/%3E%3Crect x='1' width='1' height='1' fill='%23C6FF3D'/%3E%3Crect x='2' width='1' height='1' fill='%23FF5A1F'/%3E%3Crect x='3' width='1' height='1' fill='%236B3BFF'/%3E%3C/svg%3E">
<script src="{prefix}script.js" defer></script>
</head>'''

FOOT = '''<footer class="site-foot">
  <div class="inner mono">
    <span>Stephane Vasadze — Product / Design / Growth</span>
    <a href="#top">Back to top ↑</a>
  </div>
</footer>
</body>
</html>
'''

def home():
    man = "\n".join(
        f'    <span>{c["manifesto"]}<span class="m-idx t-{c["key"]}" aria-hidden="true"><i class="sw"></i>{c["num"]}</span></span>'
        for c in CASES)
    strip = "\n".join(f'''  <a class="t-{c["key"]}" href="#{c["slug"]}">
    <span class="strip__top mono"><span>{c["num"]}</span><span>{c["kind"]}</span></span>
    <span><span class="strip__name">{c["short"]}</span><span class="strip__out mono" style="display:block">{c["strip_out"]}</span></span>
  </a>''' for c in CASES)
    chapters = []
    for i, c in enumerate(CASES):
        flip = " chapter--flip" if i % 2 else ""
        pr = "\n".join(f'          <li><span><strong>{a}</strong> {b}</span></li>' for a, b in c["principles"])
        chapters.append(f'''<section class="chapter t-{c["key"]}{flip}" id="{c["slug"]}" aria-labelledby="{c["slug"]}-title">
  <div class="inner">
    <div class="chapter__bar mono"><span>{c["num"]} / 04</span><span>{c["kind"]}</span><span>{c["bar"]}</span></div>
    <div class="chapter__lead" data-reveal>
      <span class="chapter__index" aria-hidden="true">{c["num"]}</span>
      <h2 class="chapter__title" id="{c["slug"]}-title"><a href="work/{c["slug"]}/index.html">{c["name"]}</a></h2>
      <p class="chapter__context">{c["context"]}</p>
    </div>
    <div class="chapter__motif" data-motif>
{MOTIFS[c["key"]]()}
    </div>
    <ol class="chapter__principles" data-reveal aria-label="Decision principles">
{pr}
    </ol>
    <div class="chapter__outcome" data-reveal>
      <p class="chapter__figure">{c["figure"]}</p>
      <p class="chapter__figure-label mono">{c["figure_label"]}</p>
      <a class="chapter__link" href="work/{c["slug"]}/index.html" aria-label="Read the {c["name"]} case"><span>Read the case</span><span class="arrow" aria-hidden="true">→</span></a>
    </div>
  </div>
</section>''')
    rows = "\n".join(f'''      <li><a href="work/{c["slug"]}/index.html">
        <span class="num mono">{c["num"]}</span>
        <span><span class="name t-{c["key"]}"><i class="sw" aria-hidden="true"></i><span>{c["name"]}</span></span><span class="kind mono">{c["kind"]}</span></span>
        <span class="res">{c["figure"]}</span>
      </a></li>''' for c in CASES)
    html = f'''{head("Stephane Vasadze — Product / Design / Growth",
                   "Senior product designer and product/growth operator. Growth experiments, design systems, marketplaces and AI products.",
                   "", "#F3EFE6")}
<body id="top">
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="inner">
    <a class="site-head__name" href="index.html">Stephane Vasadze <span>· Product / Design / Growth</span></a>
    <nav aria-label="Primary">
      <ul>
        <li><a href="#work">Work</a></li>
        <li><a href="#about">About</a></li>
      </ul>
    </nav>
  </div>
</header>
<main id="main">
<section class="hero" aria-labelledby="manifesto">
  <div class="inner">
    <p class="hero__kicker mono"><span>Selected work · 4 cases</span><span>Senior / Head product designer · Product &amp; growth operator</span></p>
    <h1 class="manifesto" id="manifesto">
{man}
    </h1>
    <div class="hero__foot">
      <p class="hero__support">I move from ambiguity <em>to shipped systems.</em></p>
      <a class="hero__jump mono" href="#work"><span>Four cases below</span><span class="arrow" aria-hidden="true">↓</span></a>
    </div>
  </div>
</section>

<nav class="strip" id="work" aria-label="Case index">
{strip}
</nav>

{chr(10).join(chapters)}

<section class="closing" id="about" aria-labelledby="closing-title">
  <div class="inner">
    <p class="closing__kicker mono">Throughline</p>
    <h2 class="closing__title" id="closing-title" data-reveal>Four cases.<br><em>One operator.</em></h2>
    <div class="closing__text" data-reveal>
      <p class="lead-in">Senior and head-level product designer who also runs the numbers.</p>
      <p>I frame the problem, design the system and stay through shipping — in subscription growth, design systems, marketplaces and AI products.</p>
      <p>The common move: find the constraint that makes the decision obvious — a metric set, a source of truth, a time grid, a taxonomy — and build inside it.</p>
    </div>
    <ul class="closing__list" data-reveal aria-label="All cases">
{rows}
    </ul>
  </div>
</section>
</main>
{FOOT}'''
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(html)

def case_page(i):
    c = CASES[i]
    n = CASES[(i + 1) % len(CASES)]
    nav = "\n".join(
        f'        <li><a href="../{o["slug"]}/index.html"{" aria-current=\"page\"" if o is c else ""}>{o["num"]}<span class="hide-sm"> {o["short"]}</span></a></li>'
        for o in CASES)
    facts = "\n".join(f'        <div><dt class="mono">{a}</dt><dd>{b}</dd></div>' for a, b in c["facts"])
    decs = "\n".join(f'        <li data-reveal><h3>{a}</h3><p>{b}</p></li>' for a, b in c["decisions"])
    olist = "\n".join(f'        <li><span class="mono">{a}</span><span class="v">{b}</span></li>' for a, b in c["outcome_list"])
    def label(num, text):
        return f'<h2 class="sec__label"><span class="n">{num}</span><i class="sw" aria-hidden="true"></i><span>{text}</span></h2>'
    html = f'''{head(f'{c["name"]} — Stephane Vasadze', c["standfirst"].replace("’", "'"), "../../", "")}
<body id="top" class="case t-{c["key"]}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="inner">
    <a class="site-head__name" href="../../index.html">Stephane Vasadze <span class="hide-sm">· Product / Design / Growth</span></a>
    <nav aria-label="Cases">
      <ul>
        <li><a href="../../index.html#work">Index</a></li>
{nav}
      </ul>
    </nav>
  </div>
</header>
<main id="main">
<section class="case-hero" aria-labelledby="case-title">
  <div class="inner">
    <p class="case-hero__bar mono"><span>Case {c["num"]} / 04</span><span>{c["name"]}</span><span>{c["kind"]}</span></p>
    <h1 class="case-hero__thesis" id="case-title"><span class="sr-only">{c["name"]}: </span>{c["thesis"]}</h1>
    <div class="case-hero__motif" data-motif>
{MOTIFS[c["key"]]()}
    </div>
    <div class="case-hero__foot">
      <p class="case-hero__standfirst">{c["standfirst"]}</p>
      <p class="case-hero__outcome"><span class="case-hero__figure">{c["figure"]}</span><span class="case-hero__figure-label mono">{c["figure_label"]}</span></p>
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="s1">
  <div class="inner">
    {label("01", "Situation").replace('<h2 class', '<h2 id="s1" class')}
    <div class="sec__body" data-reveal>
      <p class="lead">{c["situation_lead"]}</p>
      <p class="body-copy">{c["situation_body"]}</p>
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="s2">
  <div class="inner">
    {label("02", "Role / scope").replace('<h2 class', '<h2 id="s2" class')}
    <div class="sec__body" data-reveal>
      <dl class="facts">
{facts}
      </dl>
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="s3">
  <div class="inner">
    {label("03", "Decisions").replace('<h2 class', '<h2 id="s3" class')}
    <div class="sec__body">
      <ol class="decisions">
{decs}
      </ol>
    </div>
  </div>
</section>

<section class="sec" aria-labelledby="s4">
  <div class="inner">
    {label("04", "Evidence / system").replace('<h2 class', '<h2 id="s4" class')}
    <figure class="sec__body--wide diagram" data-reveal>
      <div class="diagram__scroll" tabindex="0" role="region" aria-label="System diagram, scrollable">
{DIAGRAMS[c["key"]]()}
      </div>
      <figcaption class="mono"><span>{c["caption"]}</span><span class="hint">Scroll sideways →</span></figcaption>
    </figure>
  </div>
</section>

<section class="outcome" aria-labelledby="s5">
  <div class="inner">
    {label("05", "Outcome").replace('<h2 class', '<h2 id="s5" class')}
    <p class="outcome__figure" data-reveal>{c["figure"]}<small>{c["outcome_small"]}</small></p>
    <ul class="outcome__list" data-reveal>
{olist}
    </ul>
  </div>
</section>

<section class="sec" aria-labelledby="s6">
  <div class="inner">
    {label("06", "Throughline").replace('<h2 class', '<h2 id="s6" class')}
    <div class="sec__body" data-reveal>
      <p class="lead">{c["throughline"]}</p>
    </div>
  </div>
</section>

<a class="next t-{n["key"]}" href="../{n["slug"]}/index.html">
  <span class="inner">
    <span class="next__bar mono"><span>Next case</span><span>{n["num"]} / 04</span></span>
    <span class="next__title">{n["name"]} <span class="arrow" aria-hidden="true">→</span></span>
    <span class="next__thesis mono">{n["kind"]} · {n["figure"]} {n["figure_label"].lower()}</span>
  </span>
</a>
</main>
{FOOT}'''
    d = os.path.join(ROOT, "work", c["slug"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(html)

if __name__ == "__main__":
    home()
    for i in range(len(CASES)):
        case_page(i)
    print("ok")
