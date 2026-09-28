const { chromium } = require('/root/.npm/_npx/fd3bca3c548369c0/node_modules/playwright');
const base = 'http://127.0.0.1:4173';
const out = '/root/portfolio-redesign/screens';
const jobs = [
  ['home-375', '/index.html', 375, 812],
  ['home-768', '/index.html', 768, 1024],
  ['home-1280', '/index.html', 1280, 800],
  ['case-kinopoisk-1280', '/work/kinopoisk-growth/index.html', 1280, 800],
  ['case-emcd-1280', '/work/emcd/index.html', 1280, 800],
  ['case-jetable-1280', '/work/jetable/index.html', 1280, 800],
  ['case-outfitme-1280', '/work/outfitme/index.html', 1280, 800],
  ['case-emcd-375', '/work/emcd/index.html', 375, 812],
  ['case-jetable-768', '/work/jetable/index.html', 768, 1024],
];
const only = process.argv.slice(2);
(async () => {
  const browser = await chromium.launch();
  for (const [name, path, w, h] of jobs) {
    if (only.length && !only.includes(name)) continue;
    const page = await browser.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    const errs = [];
    page.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    page.on('pageerror', e => errs.push(e.message));
    await page.goto(base + path, { waitUntil: 'networkidle' });
    await page.evaluate(() => document.fonts.ready);
    // scroll through so reveal observers fire, then return to top
    await page.evaluate(async () => {
      document.documentElement.style.scrollBehavior = 'auto';
      for (let y = 0; y < document.body.scrollHeight; y += 400) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); }
      window.scrollTo(0, 0);
    });
    await page.waitForTimeout(1200);
    const overflow = await page.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
    await page.screenshot({ path: `${out}/${name}.png`, fullPage: true });
    console.log(name, 'overflowX=', overflow, errs.length ? 'ERR ' + errs.join(' | ') : '');
    await page.close();
  }
  await browser.close();
})();
