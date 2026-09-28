# Build notes — Stephane Vasadze portfolio

Static site: plain HTML/CSS/JS, no build step. Deploy the folder as-is (Vercel or any static host).

## Files

| Path | What |
|---|---|
| `index.html` | Home: hero manifesto, colour index strip, four case chapters, closing |
| `work/{kinopoisk-growth,emcd,jetable,outfitme}/index.html` | Case pages |
| `styles.css` | All styles (tokens, layout, motifs, motion, responsive) |
| `script.js` | Progressive enhancement: reveal-on-scroll and motif motion only while in view |
| `vercel.json` | `cleanUrls` + `trailingSlash: true` (relative links need the trailing slash), cache and security headers |
| `.vercelignore` | Keeps `_tools/`, `screens/` and these notes out of the deploy |
| `_tools/build_site.py` | Authoring helper that writes all five HTML files from one content table. Optional: you can edit the HTML directly, but edits get overwritten if you re-run the helper |
| `_tools/shoot.js` | Playwright screenshot script (expects a server on `127.0.0.1:4173`) |
| `screens/` | QA captures: home at 375/768/1280, all four cases at 1280, EMCD at 375, Jetable at 768 |

## Art direction

- **Palette:** warm paper `#F3EFE6` and ink `#0F0F0D`, plus four case colours used as full-bleed fields: Kinopoisk `#1D3AE8`, EMCD `#C6FF3D`, Jetable `#FF5A1F`, OutfitMe `#6B3BFF`. Text is paper on cobalt and violet, and ink on acid and orange, so every pair passes AA contrast.
- **Type:** Instrument Serif for display, Inter for body, IBM Plex Mono for labels (Google Fonts, with system fallbacks).
- **No cards, shadows, gradients, glass or rounded boxes.** Structure comes from 1px rules, a 12-column grid and scale contrast.
- **Motifs:** each case has an inline SVG motif, reused in its chapter and on its case hero:
  - Kinopoisk: a thermometer timeline with 11 experiment ticks
  - EMCD: six lineages converging on production, plus 15 decision blocks
  - Jetable: a 90-minute ring split into six 15-minute slots, with a QR mark
  - OutfitMe: the original photo frame kept behind the cut-out, plus taxonomy tags
- **Evidence diagrams** on the case pages are hand-built SVG system maps, not screenshots. Each has a `<title>`/`<desc>` and sits in a keyboard-focusable region that scrolls sideways under 880px.
- **Order:** chapters alternate the motif left/right. Case pages follow Situation → Role/scope → Decisions → Evidence/system → Outcome (colour band) → Throughline → Next case (a band in the next case's colour, looping 04 → 01).

## Content rules followed

Only the facts from the brief are used. No invented metrics, dates, clients or win/loss splits: the 11 experiments are drawn identically, and the diagrams show structure, not data. There are no placeholders, NDA chips or "needs input" markers. Interpretive copy (situations, throughlines) stays qualitative.

## Accessibility and motion

- Skip link, landmarks, one `h1` per page, labelled sections, `aria-current` in the case nav, and visible `:focus-visible` outlines in `currentColor`.
- Decorative motifs are `aria-hidden`. Diagrams are `role="img"` with a description.
- Content is visible with no JS. JS adds `.js` and hides only elements that start below the fold, then reveals them with IntersectionObserver.
- `prefers-reduced-motion` turns off all animation, transitions, smooth scroll and reveal.
- Motif animation (thermometer level, lane flow, ring orbit, scan line) is paused off-screen.

## QA done

- Captured every page with Playwright (Chromium) at the widths above and reviewed the captures. Fixed:
  - label/swatch misalignment
  - the mobile header wrapping
  - index marks wrapping in the mobile manifesto
  - the hero overflowing a 1280×800 viewport (type is now capped by viewport height)
  - diagram label collisions (Jetable, OutfitMe)
  - the "2 days" descender hitting its label
- No horizontal page overflow at any tested width, and no console errors.
- Replaced the pre-existing `vercel.json` (`trailingSlash: false`), because it would break the relative links between case pages.

## Not included / next

- No contact details or social links: the brief gave none. Add them to the closing section and footer.
- No OG image. Add a 1200×630 export of the hero if you want link previews.
- Fonts load from Google Fonts. Self-host them if you need offline or no-third-party loading.

## Local preview

```
cd portfolio-redesign && python3 -m http.server 4173
node _tools/shoot.js            # re-capture screens/ (uses the Playwright under ~/.npm/_npx)
```
