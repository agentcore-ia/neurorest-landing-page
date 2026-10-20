// Mismo Tailwind que cargaba la pagina desde cdn.tailwindcss.com (v3, plugins
// forms y container-queries, sin configuracion propia), pero generado una vez
// al publicar en vez de en el navegador de cada visitante.
module.exports = {
  content: [
    '../*.html',
    '../*/index.html',
    '../capta-refresh.js',
    '../scripts/**/*.py',
  ],
  plugins: [require('@tailwindcss/forms'), require('@tailwindcss/container-queries')],
};
