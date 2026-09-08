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

  const vectorArt = document.querySelector('.vector-art');
  const motionToggle = vectorArt.querySelector('.vector-motion-toggle');
  let vectorVisible = false;
  const syncVectorVisibility = () => vectorArt.classList.toggle('is-offscreen', !vectorVisible || document.hidden);
  new IntersectionObserver(([entry]) => {
    vectorVisible = entry.isIntersecting;
    syncVectorVisibility();
  }, { threshold: 0.1 }).observe(vectorArt);
  document.addEventListener('visibilitychange', syncVectorVisibility);
  motionToggle.addEventListener('click', () => {
    const paused = vectorArt.classList.toggle('is-paused');
    motionToggle.setAttribute('aria-pressed', String(paused));
    motionToggle.setAttribute('aria-label', paused ? 'Reanudar animación de Capta' : 'Pausar animación de Capta');
    motionToggle.textContent = paused ? 'Reanudar animación ▷' : 'Pausar animación Ⅱ';
  });

  // The hero has its own pause control; other scenes retain viewport pausing.
  const scenes = document.querySelectorAll('main svg:not(.hero-orbit):not(.scene-connections):not(.capta-vector)');
  const sceneObserver = new IntersectionObserver((entries) => {
    entries.forEach(({ target, isIntersecting }) => {
      target.getAnimations({ subtree: true }).forEach((animation) => {
        if (isIntersecting && !document.hidden) animation.play();
        else animation.pause();
      });
    });
  }, { rootMargin: '80px' });
  scenes.forEach((scene) => {
    if (!scene.closest('.capta-vector')) sceneObserver.observe(scene);
  });
})();
