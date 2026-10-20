// Navegacion de las paginas de soluciones: el menu del celular y "Recursos".
// La home tiene su propio script (capta-refresh.js), que espera elementos que
// aca no existen.
(() => {
  const toggle = document.getElementById('navToggle');
  const links = document.getElementById('navLinks');
  if (toggle && links) {
    toggle.addEventListener('click', () => {
      const abierto = links.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(abierto));
      toggle.setAttribute('aria-label', abierto ? 'Cerrar navegación' : 'Abrir navegación');
    });
  }
  const recursos = document.querySelector('.nav-resources');
  if (recursos) {
    document.addEventListener('click', (e) => { if (!recursos.contains(e.target)) recursos.open = false; });
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape') recursos.open = false; });
  }
})();
