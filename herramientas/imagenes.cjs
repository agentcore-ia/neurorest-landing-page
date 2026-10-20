// Versiones livianas de las imagenes que se ven en todas las paginas.
//   npm run imagenes
const path = require('path');
const sharp = require('sharp');
const r = (f) => path.join(__dirname, '..', f);
(async () => {
  // Logo de la navegacion y el pie: se muestra a 56x58 (x2 para pantallas retina).
  await sharp(r('logo-capta.png')).resize(112, 117).png({ compressionLevel: 9, palette: true }).toFile(r('assets/logo-capta-112.png'));
  // Favicon CUADRADO (el original es 560x584): Google pide multiplos de 48 px.
  const cuadrado = (lado) => sharp(r('favicon.png'))
    .resize(lado, lado, { fit: 'contain', background: { r: 0, g: 0, b: 0, alpha: 0 } })
    .png({ compressionLevel: 9, palette: true });
  await cuadrado(48).toFile(r('assets/favicon-48.png'));
  await cuadrado(192).toFile(r('assets/favicon-192.png'));
  // Apple pide 180x180 sin transparencia.
  await sharp(r('favicon.png')).resize(180, 180, { fit: 'contain', background: '#ffffff' }).flatten({ background: '#ffffff' })
    .png({ compressionLevel: 9 }).toFile(r('assets/apple-touch-icon.png'));
  // La mascota del hero (1374x1145): misma imagen en WebP.
  await sharp(r('capta-mascot.png')).webp({ quality: 82, alphaQuality: 90 }).toFile(r('assets/capta-mascot.webp'));
  console.log('imagenes listas');
})();
