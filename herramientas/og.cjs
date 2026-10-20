// Genera ../og-capta.png (1200x630), la imagen que se ve al compartir capta.ar.
//   npm run og
const path = require('path');
const sharp = require('sharp');
let chromium;
try { ({ chromium } = require('playwright')); } catch { ({ chromium } = require('/opt/node22/lib/node_modules/playwright')); }
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 630 } });
  await p.goto('file://' + path.join(__dirname, 'og.html'));
  await p.evaluate(() => document.fonts.ready);
  const png = await p.screenshot({ type: 'png' });
  await b.close();
  await sharp(png).png({ compressionLevel: 9, palette: true, quality: 90 }).toFile(path.join(__dirname, '..', 'og-capta.png'));
  console.log('og-capta.png listo');
})();
