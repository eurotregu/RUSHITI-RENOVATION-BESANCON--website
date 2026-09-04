// Paquet 14 — régénère les PNG d'icônes depuis favicon.svg (Chromium headless, fond transparent).
// Usage : NODE_PATH=/opt/node22/lib/node_modules node gen_icones.js /chemin/du/clone/production
const { chromium } = require('playwright');
const fs = require('fs'); const path = require('path');
const root = process.argv[2] || '.';
const sizes = [['favicon-16.png', 16], ['favicon-32.png', 32], ['apple-touch-icon.png', 180], ['favicon-192.png', 192], ['favicon-512.png', 512]];
(async () => {
  const svg = fs.readFileSync(path.join(root, 'favicon.svg'), 'utf8');
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
  for (const [name, s] of sizes) {
    const p = await b.newPage({ viewport: { width: s, height: s }, deviceScaleFactor: 1 });
    await p.setContent(`<!doctype html><html><head><style>html,body{margin:0;background:transparent}svg{display:block;width:${s}px;height:${s}px}</style></head><body>${svg}</body></html>`);
    await p.screenshot({ path: path.join(root, name), omitBackground: true, clip: { x: 0, y: 0, width: s, height: s } });
    await p.close(); console.log('  ', name, s + 'px');
  }
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
