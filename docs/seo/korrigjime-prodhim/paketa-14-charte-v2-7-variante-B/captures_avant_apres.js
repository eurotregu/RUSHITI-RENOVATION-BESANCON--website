const { chromium } = require('playwright');
const tag = process.argv[2] || 'avant';
const out = process.argv[3];
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  const noAnim = '.js-anim main section{opacity:1!important;transform:none!important} *{transition:none!important;animation:none!important}';
  const jobs = [
    ['index.html', 'accueil', 1280, 1000, false],
    ['index.html', 'accueil-complet', 1280, 900, true],
    ['contact.html', 'contact', 1280, 1000, false],
    ['peinture-interieure-besancon.html', 'peinture', 1280, 1000, false],
  ];
  for (const [file, name, w, h, full] of jobs) {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    await p.route('**/*', r => (r.request().url().startsWith('http://127.0.0.1') ? r.continue() : r.abort()));
    await p.goto('http://127.0.0.1:8765/' + file, { waitUntil: 'domcontentloaded' });
    await p.addStyleTag({ content: noAnim });
    await p.waitForTimeout(300);
    await p.screenshot({ path: `${out}/${name}-${tag}.png`, fullPage: full });
    await p.close();
  }
  // mobile : bandeau collant + bloc CTA final + pied de page
  const m = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 });
  await m.route('**/*', r => (r.request().url().startsWith('http://127.0.0.1') ? r.continue() : r.abort()));
  await m.goto('http://127.0.0.1:8765/index.html', { waitUntil: 'domcontentloaded' });
  await m.addStyleTag({ content: noAnim });
  await m.waitForTimeout(300);
  await m.screenshot({ path: `${out}/mobile-haut-${tag}.png` });
  const cta = await m.$('.cta-band');
  if (cta) { await cta.scrollIntoViewIfNeeded(); await m.waitForTimeout(200); await m.screenshot({ path: `${out}/mobile-cta-${tag}.png` }); }
  await m.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
  await m.waitForTimeout(200);
  await m.screenshot({ path: `${out}/mobile-pied-${tag}.png` });
  await m.close();
  await b.close();
  console.log('captures', tag, 'ok');
})().catch(e => { console.error(e); process.exit(1); });
