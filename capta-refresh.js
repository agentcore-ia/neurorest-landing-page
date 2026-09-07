(() => {
  const navToggle = document.getElementById('navToggle');
  const navLinks = document.getElementById('navLinks');
  function closeNavigation() {
    navLinks.classList.remove('is-open');
    navToggle.setAttribute('aria-expanded', 'false');
    navToggle.setAttribute('aria-label', 'Abrir navegación');
  }
  navToggle.addEventListener('click', () => {
    const expanded = navLinks.classList.toggle('is-open');
    navToggle.setAttribute('aria-expanded', String(expanded));
    navToggle.setAttribute('aria-label', expanded ? 'Cerrar navegación' : 'Abrir navegación');
  });
  navLinks.querySelectorAll('a').forEach(link => link.addEventListener('click', closeNavigation));
  document.addEventListener('keydown', event => {
    const modal = document.getElementById('demoModal');
    if (event.key === 'Tab' && !modal.classList.contains('hidden')) {
      const focusable = [...modal.querySelectorAll('button, input, a[href]')].filter(element => element.getClientRects().length);
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus();
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus();
      }
    }
    if (event.key === 'Escape') {
      closeNavigation();
      if (!document.getElementById('demoModal').classList.contains('hidden')) window.closeModal();
    }
  });
  const resources = document.querySelector('.nav-resources');
  document.addEventListener('click', event => {
    if (!resources.contains(event.target)) resources.open = false;
  });
  resources.querySelectorAll('a').forEach(link => link.addEventListener('click', () => { resources.open = false; }));
  document.addEventListener('keydown', event => {
    if (event.key === 'Escape') resources.open = false;
  });

  // Pause decorative SVG loops outside the viewport.
  const scenes = document.querySelectorAll('main svg:not(.hero-orbit):not(.scene-connections)');
  const sceneObserver = new IntersectionObserver((entries) => {
    entries.forEach(({ target, isIntersecting }) => {
      target.getAnimations({ subtree: true }).forEach((animation) => {
        if (isIntersecting && !document.hidden) animation.play();
        else animation.pause();
      });
    });
  }, { rootMargin: '80px' });
  scenes.forEach((scene) => sceneObserver.observe(scene));
})();
