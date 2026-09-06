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
  const stage = document.querySelector('.mascot-scene');
  const steps = [...document.querySelectorAll('[data-scene-step]')];
  const toggle = document.getElementById('motionToggle');
  const reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  let visible = false;
  let paused = reducedMotion.matches;
  let current = 0;
  let timer;

  function paint() {
    steps.forEach((step, index) => {
      step.classList.toggle('is-active', index === current);
    });
    stage.dataset.beat = String(current);
  }

  function schedule() {
    clearTimeout(timer);
    if (paused || !visible || document.hidden) return;
    timer = setTimeout(() => {
      current = (current + 1) % steps.length;
      paint();
      schedule();
    }, 3800);
  }

  function updateToggle() {
    document.documentElement.classList.toggle('motion-paused', paused);
    toggle.setAttribute('aria-pressed', String(paused));
    toggle.setAttribute('aria-label', paused ? 'Reanudar animaciones' : 'Pausar animaciones');
    toggle.textContent = paused ? 'Reanudar ▷' : 'Pausar Ⅱ';
  }

  if (stage && toggle) {
    current = paused ? steps.length - 1 : 0;
    paint();
    updateToggle();
    new IntersectionObserver(([entry]) => {
      visible = entry.isIntersecting;
      stage.classList.toggle('is-visible', visible);
      schedule();
    }, { threshold: 0.15 }).observe(stage);
    toggle.addEventListener('click', () => {
      paused = !paused;
      updateToggle();
      schedule();
    });
    reducedMotion.addEventListener('change', (event) => {
      paused = event.matches;
      if (paused) current = steps.length - 1;
      paint();
      updateToggle();
      schedule();
    });
    document.addEventListener('visibilitychange', schedule);
  }

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
