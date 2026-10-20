"""Arma las paginas de soluciones de capta.ar, el JSON-LD de la home y el sitemap.

Las paginas son HTML estatico: se generan una vez, se commitean y Vercel las
sirve tal cual. Asi cualquier rastreador (con o sin JavaScript) lee el
contenido completo.

    cd herramientas && npm run todo     # paginas + CSS

El texto de cada pagina esta en scripts/contenido.py.
"""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

from contenido import ACTUALIZADO, ACTUALIZADO_TEXTO, PAGINAS, TESTIMONIOS, CLIENTES  # noqa: E402

SITIO = "https://capta.ar"
VERSION = "20261020"

ORGANIZACION = {
    "@type": "Organization",
    "@id": f"{SITIO}/#organization",
    "name": "Capta",
    "url": f"{SITIO}/",
    "logo": {"@type": "ImageObject", "url": f"{SITIO}/logo-capta.png", "width": 560, "height": 584},
    "alternateName": "Capta, sistema gastronómico",
    "description": "Capta es un software de gestión gastronómica con inteligencia artificial, hecho en Argentina, para restaurantes, bares, pizzerías y locales de comida.",
    "disambiguatingDescription": "Capta (capta.ar) es el sistema de gestión gastronómica con IA hecho en Argentina, distinto de otros productos de software que también se llaman Capta.",
    "knowsAbout": ["software de gestión gastronómica", "sistemas para restaurantes", "inteligencia artificial para restaurantes", "automatización de WhatsApp para restaurantes", "delivery para restaurantes"],
    "areaServed": {"@type": "Country", "name": "Argentina"},
    "knowsLanguage": "es-AR",
}

SITIO_WEB = {
    "@type": "WebSite",
    "@id": f"{SITIO}/#website",
    "url": f"{SITIO}/",
    "name": "Capta",
    "inLanguage": "es-AR",
    "publisher": {"@id": f"{SITIO}/#organization"},
}

SOFTWARE = {
    "@type": "SoftwareApplication",
    "@id": f"{SITIO}/#software",
    "name": "Capta",
    "applicationCategory": "BusinessApplication",
    "applicationSubCategory": "Software de gestión gastronómica",
    "operatingSystem": "Web",
    "url": f"{SITIO}/",
    "inLanguage": "es-AR",
    "description": "Software de gestión gastronómica en la nube con inteligencia artificial: pedidos de todos los canales, mesas con QR, reservas, cocina, caja, stock, facturación con ARCA, delivery y clientes, con atención automática por WhatsApp, Instagram y llamadas.",
    "featureList": [
        "Atención automática con IA por WhatsApp e Instagram",
        "Atención de llamadas con IA (plan Pro)",
        "Toma de pedidos automática",
        "Menú digital y mesas con QR",
        "Gestión de reservas",
        "Comandas a cocina impresas o en pantalla",
        "Caja, stock e insumos",
        "Facturación electrónica con ARCA",
        "Verificación de pagos con Mercado Pago",
        "Delivery con zonas, repartidores y seguimiento en vivo",
        "CRM, puntos y campañas para recuperar clientes",
        "Analíticas y asistente Gerente IA",
    ],
    "offers": [
        {"@type": "Offer", "name": "Plan Base", "price": "50000", "priceCurrency": "ARS", "url": f"{SITIO}/#pricing"},
        {"@type": "Offer", "name": "Plan Growth", "price": "65000", "priceCurrency": "ARS", "url": f"{SITIO}/#pricing"},
        {"@type": "Offer", "name": "Plan Pro", "price": "85000", "priceCurrency": "ARS", "url": f"{SITIO}/#pricing",
         "description": "Más $150 por minuto de llamada atendida por la IA."},
    ],
    "publisher": {"@id": f"{SITIO}/#organization"},
}

TITULOS_CORTOS = {p["ruta"]: p["miga"] for p in PAGINAS}


def url_de(ruta: str) -> str:
    return f"{SITIO}/{ruta}" if ruta else f"{SITIO}/"


def sin_html(texto: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", texto)).strip()


def e(texto: str) -> str:
    """Escapa para atributos y texto plano."""
    return html.escape(texto, quote=True)


# ----------------------------------------------------------------- partes

def nav() -> str:
    links = "".join(
        f'<a href="/{p["ruta"]}">{e(p["miga"])}</a>' for p in PAGINAS
    )
    return f'''<nav id="siteNav" class="nav-glass reference-nav fixed inset-x-0 top-0 z-50" aria-label="Navegación principal">
  <div class="reference-nav-inner">
    <a href="/" class="reference-brand" aria-label="Capta inicio"><img src="/assets/logo-capta-112.png" alt="" width="56" height="58"/><span>Capta</span></a>
    <button id="navToggle" type="button" class="mobile-nav-toggle" aria-label="Abrir navegación" aria-expanded="false" aria-controls="navLinks"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>
    <div id="navLinks" class="reference-nav-links">
      <a href="/#features">Cómo funciona</a>
      <a href="/#pricing">Precios</a>
      <a class="mobile-login" href="https://app.capta.ar/">Iniciar sesión</a>
      <details class="nav-resources"><summary>Recursos <svg viewBox="0 0 16 16" width="16" height="16" fill="none" aria-hidden="true"><path d="m3 6 5 5 5-5" stroke="currentColor" stroke-width="1.7"/></svg></summary><div class="resources-menu">{links}<a href="/#faq">Preguntas frecuentes</a></div></details>
    </div>
    <div class="reference-nav-actions"><a class="login-link" href="https://app.capta.ar/">Iniciar sesión</a><a href="/#demo" class="reference-start">Solicitar demo</a></div>
  </div>
</nav>'''


def footer() -> str:
    soluciones = "".join(
        f'<li><a href="/{p["ruta"]}" class="transition-colors hover:text-[#1d1d1f]">{e(p["miga"])}</a></li>'
        for p in PAGINAS
    )
    return f'''<footer class="bg-[#f5f5f7] px-5 py-16 md:px-8">
  <div class="mx-auto grid max-w-6xl gap-12 md:grid-cols-4">
    <div class="space-y-5 md:col-span-2">
      <div class="flex items-center gap-2.5">
        <img src="/assets/logo-capta-112.png" alt="Capta" width="36" height="36" class="h-9 w-9 object-contain" loading="lazy"/>
        <span class="text-lg font-extrabold tracking-[-0.02em] text-[#1d1d1f]">Capta</span>
      </div>
      <p class="max-w-sm text-[14px] font-medium leading-relaxed text-[#6e6e73]">Software de gestión gastronómica con inteligencia artificial, hecho en Argentina.</p>
    </div>
    <div>
      <p class="text-[12px] font-black uppercase tracking-[0.14em] text-[#1d1d1f]">Producto</p>
      <ul class="mt-5 space-y-3 text-[14px] font-medium text-[#6e6e73]">
        <li><a href="/#features" class="transition-colors hover:text-[#1d1d1f]">Plataforma</a></li>
        <li><a href="/#funciones" class="transition-colors hover:text-[#1d1d1f]">Funciones</a></li>
        <li><a href="/#pricing" class="transition-colors hover:text-[#1d1d1f]">Precios</a></li>
        <li><a href="/#faq" class="transition-colors hover:text-[#1d1d1f]">Preguntas frecuentes</a></li>
        <li><a href="/automatizacion-gastronomica.html" class="transition-colors hover:text-[#1d1d1f]">Automatización gastronómica</a></li>
      </ul>
    </div>
    <div>
      <p class="text-[12px] font-black uppercase tracking-[0.14em] text-[#1d1d1f]">Soluciones</p>
      <ul class="mt-5 space-y-3 text-[14px] font-medium text-[#6e6e73]">{soluciones}</ul>
    </div>
  </div>
  <div class="mx-auto mt-14 flex max-w-6xl flex-col items-center justify-between gap-3 border-t border-black/[.07] pt-6 text-[13px] font-medium text-[#a1a1a6] sm:flex-row">
    <span>&copy; 2026 Capta. Todos los derechos reservados.</span>
    <div class="flex items-center gap-5">
      <a href="/privacidad.html" class="transition-colors hover:text-[#1d1d1f]">Política de privacidad</a>
      <span class="hidden sm:block">Hecho en Argentina</span>
    </div>
  </div>
</footer>'''


def h2(texto: str, id_: str) -> str:
    return f'<h2 id="{id_}" class="t-display text-3xl text-[#1d1d1f] md:text-5xl">{texto}</h2>'


def testimonio(t: dict) -> str:
    return (f'<figure class="flex flex-col rounded-[1.75rem] bg-[#f5f5f7] p-7">'
            f'<p class="text-[13px] font-bold uppercase tracking-[0.14em] text-[#ff6b1a]">{e(t["tema"])}</p>'
            f'<blockquote class="mt-4 flex-1 text-[16px] font-medium leading-relaxed text-[#3a3a3f]"><p>“{e(t["texto"])}”</p></blockquote>'
            f'<figcaption class="mt-6 text-[14px] font-bold text-[#1d1d1f]">{e(t["autor"])}</figcaption></figure>')


def clientes() -> str:
    return "".join(
        f'<figure class="overflow-hidden rounded-[1.75rem] bg-[#f5f5f7]">'
        f'<img src="{c["foto"]}" alt="{e(c["alt"])}" width="1200" height="800" loading="lazy" decoding="async" class="aspect-[3/2] w-full object-cover"/>'
        f'<figcaption class="px-7 py-5"><span class="block text-lg font-extrabold tracking-[-0.02em] text-[#1d1d1f]">{e(c["nombre"])}</span>'
        f'<span class="mt-1 block text-[14px] font-medium text-[#6e6e73]">{e(c["detalle"])}</span></figcaption></figure>'
        for c in CLIENTES
    )


def bloque(b: dict, n: int) -> str:
    id_ = f"s{n}"
    intro = f'<p class="mt-5 max-w-3xl text-[17px] font-medium leading-relaxed text-[#6e6e73]">{b["intro"]}</p>' if b.get("intro") else ""
    if b["tipo"] == "prosa":
        parrafos = "".join(f"<p>{p}</p>" for p in b["parrafos"])
        return f'''<section class="px-5 py-16 md:px-8 md:py-20" aria-labelledby="{id_}">
  <div class="mx-auto max-w-3xl">{h2(b["h2"], id_)}<div class="pg-prosa mt-7">{parrafos}</div></div>
</section>'''
    if b["tipo"] == "tarjetas":
        items = "".join(
            f'<div class="pg-tarjeta"><h3>{t}</h3><p>{d}</p></div>' for t, d in b["items"]
        )
        return f'''<section class="px-5 py-16 md:px-8 md:py-20" aria-labelledby="{id_}">
  <div class="mx-auto max-w-6xl">{h2(b["h2"], id_)}{intro}<div class="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-3">{items}</div></div>
</section>'''
    if b["tipo"] == "pasos":
        items = "".join(
            f'<li class="pg-tarjeta flex gap-5"><span class="pg-num shrink-0">{i}</span><div><h3>{t}</h3><p>{d}</p></div></li>'
            for i, (t, d) in enumerate(b["items"], 1)
        )
        return f'''<section class="px-5 py-16 md:px-8 md:py-20" aria-labelledby="{id_}">
  <div class="mx-auto max-w-4xl">{h2(b["h2"], id_)}{intro}<ol class="mt-10 grid gap-4">{items}</ol></div>
</section>'''
    if b["tipo"] == "tabla":
        cab = "".join(f'<th scope="col">{c}</th>' for c in b["columnas"])
        filas = "".join(
            f'<tr><th scope="row">{f[0]}</th>' + "".join(f"<td>{c}</td>" for c in f[1:]) + "</tr>"
            for f in b["filas"]
        )
        return f'''<section class="px-5 py-16 md:px-8 md:py-20" aria-labelledby="{id_}">
  <div class="mx-auto max-w-6xl">{h2(b["h2"], id_)}{intro}
    <div class="pg-tabla-wrap mt-10"><table class="pg-tabla"><caption>{b.get("caption", "")}</caption><thead><tr>{cab}</tr></thead><tbody>{filas}</tbody></table></div>
  </div>
</section>'''
    if b["tipo"] == "dos":
        def col(titulo, items, acento):
            lis = "".join(f'<li class="flex gap-3"><span aria-hidden="true" class="mt-2 h-2 w-2 shrink-0 rounded-full {acento}"></span><span>{x}</span></li>' for x in items)
            return f'<div class="pg-tarjeta"><h3>{titulo}</h3><ul class="mt-5 space-y-3 text-[15px] font-medium leading-relaxed text-[#4a4a50]">{lis}</ul></div>'
        return f'''<section class="px-5 py-16 md:px-8 md:py-20" aria-labelledby="{id_}">
  <div class="mx-auto max-w-6xl">{h2(b["h2"], id_)}
    <div class="mt-10 grid gap-4 md:grid-cols-2">{col(*b["izquierda"], "bg-[#ff6b1a]")}{col(*b["derecha"], "bg-[#86868b]")}</div>
  </div>
</section>'''
    if b["tipo"] == "clientes":
        return f'''<section class="px-5 py-16 md:px-8 md:py-20" aria-labelledby="{id_}">
  <div class="mx-auto max-w-6xl">{h2(b["h2"], id_)}{intro}<div class="mt-10 grid gap-4 md:grid-cols-2">{clientes()}</div></div>
</section>'''
    if b["tipo"] == "testimonios":
        items = "".join(testimonio(TESTIMONIOS[i]) for i in b["items"])
        mas = '<p class="mt-8"><a href="/casos-de-exito" class="text-[15px] font-bold text-[#1d1d1f] underline decoration-[#ffb27a] underline-offset-4">Ver casos de éxito →</a></p>' if b.get("mas") else ""
        return f'''<section class="px-5 py-16 md:px-8 md:py-20" aria-labelledby="{id_}">
  <div class="mx-auto max-w-6xl">{h2(b["h2"], id_)}{intro}<div class="mt-10 grid gap-4 md:grid-cols-2 lg:grid-cols-3">{items}</div>{mas}</div>
</section>'''
    raise ValueError(f"Bloque desconocido: {b['tipo']}")


def jsonld_pagina(p: dict) -> str:
    url = url_de(p["ruta"])
    grafo = [
        ORGANIZACION,
        SOFTWARE,
        SITIO_WEB,
        {
            "@type": "WebPage",
            "@id": f"{url}#webpage",
            "url": url,
            "name": p["title"],
            "description": p["description"],
            "inLanguage": "es-AR",
            "isPartOf": {"@id": f"{SITIO}/#website"},
            "about": {"@id": f"{SITIO}/#software"},
            "publisher": {"@id": f"{SITIO}/#organization"},
            "dateModified": ACTUALIZADO,
            "breadcrumb": {"@id": f"{url}#breadcrumb"},
        },
        {
            "@type": "BreadcrumbList",
            "@id": f"{url}#breadcrumb",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": f"{SITIO}/"},
                {"@type": "ListItem", "position": 2, "name": p["miga"], "item": url},
            ],
        },
    ]
    if p.get("faq"):
        grafo.append({
            "@type": "FAQPage",
            "@id": f"{url}#faq",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": sin_html(a)}}
                for q, a in p["faq"]
            ],
        })
    return json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False, indent=2)


def pagina(p: dict) -> str:
    url = url_de(p["ruta"])
    resumen = "".join(f"<li>{x}</li>" for x in p["resumen"])
    bloques = "\n".join(bloque(b, i) for i, b in enumerate(p["bloques"], 1))
    aviso = f'<p class="pg-nota mt-6 max-w-3xl">{p["aviso"]}</p>' if p.get("aviso") else ""
    faq = ""
    if p.get("faq"):
        items = "".join(f"<details><summary>{q}</summary><div>{a}</div></details>" for q, a in p["faq"])
        faq = f'''<section class="px-5 py-16 md:px-8 md:py-20" aria-labelledby="faq-pg">
  <div class="mx-auto max-w-3xl"><h2 id="faq-pg" class="t-display text-3xl text-[#1d1d1f] md:text-5xl">Preguntas frecuentes</h2><div class="pg-faq mt-8 space-y-3">{items}</div></div>
</section>'''
    fuentes = ""
    if p.get("fuentes"):
        lis = "".join(f'<li><a href="{e(u)}" rel="nofollow noopener" target="_blank">{e(t)}</a></li>' for t, u in p["fuentes"])
        fuentes = f'''<section class="px-5 pb-6 md:px-8" aria-labelledby="fuentes">
  <div class="mx-auto max-w-3xl"><h2 id="fuentes" class="text-[13px] font-black uppercase tracking-[0.14em] text-[#1d1d1f]">Fuentes</h2><ul class="pg-nota mt-3 list-disc space-y-1 pl-5">{lis}</ul><p class="pg-nota mt-3">Consultadas el {ACTUALIZADO_TEXTO}.</p></div>
</section>'''
    relacionadas = "".join(
        f'<a href="/{r}" class="pg-tarjeta block transition-colors hover:bg-[#fff1e8]"><h3>{e(TITULOS_CORTOS[r])}</h3><p>Leer más →</p></a>'
        for r in p["relacionadas"]
    )
    return f'''<!DOCTYPE html>
<html lang="es-AR">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>{e(p["title"])}</title>
<meta name="description" content="{e(p["description"])}"/>
<meta name="robots" content="index, follow, max-image-preview:large"/>
<link rel="canonical" href="{url}"/>
<link rel="alternate" hreflang="es-AR" href="{url}"/>
<meta name="theme-color" content="#ff6b1a"/>
<meta property="og:type" content="article"/>
<meta property="og:locale" content="es_AR"/>
<meta property="og:site_name" content="Capta"/>
<meta property="og:title" content="{e(p["title"])}"/>
<meta property="og:description" content="{e(p["description"])}"/>
<meta property="og:url" content="{url}"/>
<meta property="og:image" content="{SITIO}/og-capta.png"/>
<meta property="og:image:width" content="1200"/>
<meta property="og:image:height" content="630"/>
<meta property="article:modified_time" content="{ACTUALIZADO}"/>
<meta name="twitter:card" content="summary_large_image"/>
<meta name="twitter:title" content="{e(p["title"])}"/>
<meta name="twitter:description" content="{e(p["description"])}"/>
<meta name="twitter:image" content="{SITIO}/og-capta.png"/>
<link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png"/>
<link rel="icon" type="image/png" sizes="192x192" href="/assets/favicon-192.png"/>
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&amp;family=Manrope:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="/capta-refresh.css?v={VERSION}"/>
<link rel="stylesheet" href="/assets/paginas.css?v={VERSION}"/>
<link rel="stylesheet" href="/assets/capta.css?v={VERSION}"/>
<script type="application/ld+json">
{jsonld_pagina(p)}
</script>
</head>
<body class="pg">
{nav()}
<main id="contenido">
<section class="pg-hero px-5 pb-14 pt-4 md:px-8 md:pb-20 md:pt-16" aria-labelledby="titulo">
  <div class="mx-auto max-w-6xl">
    <nav aria-label="Migas de pan"><ol class="pg-migas flex flex-wrap"><li><a href="/">Inicio</a></li><li aria-current="page">{e(p["miga"])}</li></ol></nav>
    <p class="t-eyebrow mt-8 text-[#ff6b1a]">{e(p["eyebrow"])}</p>
    <h1 id="titulo" class="pg-h1 mt-5 max-w-4xl">{p["h1"]}</h1>
    <p class="pg-lead mt-6 max-w-3xl">{p["lead"]}</p>
    <div class="mt-9 flex flex-wrap items-center gap-4">
      <a href="/#demo" class="btn-ember inline-flex items-center gap-2 rounded-full px-8 py-4 text-[16px] font-bold">Solicitar una demo</a>
      <a href="/#pricing" class="rounded-full px-6 py-4 text-[16px] font-bold text-[#1d1d1f] underline decoration-[#ffb27a] underline-offset-4">Ver precios</a>
    </div>
    <div class="pg-resumen mt-12 max-w-4xl p-7 md:p-9">
      <p class="text-[13px] font-black uppercase tracking-[0.14em] text-[#1d1d1f]">En resumen</p>
      <ul class="mt-5 space-y-3 text-[16px] font-medium leading-relaxed text-[#3a3a3f]">{resumen}</ul>
    </div>
    {aviso}
  </div>
</section>
{bloques}
{faq}
{fuentes}
<section class="px-5 py-16 md:px-8 md:py-20" aria-labelledby="relacionadas">
  <div class="mx-auto max-w-6xl"><h2 id="relacionadas" class="t-display text-3xl text-[#1d1d1f] md:text-4xl">Seguí leyendo</h2><div class="mt-8 grid gap-4 sm:grid-cols-2 lg:grid-cols-4">{relacionadas}</div></div>
</section>
<section class="px-5 pb-24 md:px-8" aria-labelledby="cta">
  <div class="pg-cta mx-auto max-w-6xl px-8 py-14 text-center md:px-16 md:py-20">
    <h2 id="cta" class="t-display text-3xl md:text-5xl">Probá Capta con tu propio menú.</h2>
    <p class="mx-auto mt-5 max-w-2xl text-[17px] font-medium leading-relaxed text-white/75">Te mostramos cómo atiende, cómo llegan los pedidos y cómo queda tu panel, con los productos de tu local.</p>
    <a href="/#demo" class="btn-ember mt-9 inline-flex items-center gap-2 rounded-full px-10 py-4 text-lg font-bold">Solicitar una demo</a>
  </div>
  <p class="pg-nota mx-auto mt-6 max-w-6xl text-center">Última actualización: {ACTUALIZADO_TEXTO}.</p>
</section>
</main>
{footer()}
<script src="/assets/paginas.js?v={VERSION}" defer></script>
</body>
</html>
'''


# ----------------------------------------------------------------- home

def preguntas_de_la_home(index: str) -> list[tuple[str, str]]:
    """Las preguntas VISIBLES de la home: el JSON-LD sale de aca y nunca dice
    algo que la pagina no muestra."""
    faq = index[index.index('id="faq"'):]
    salida = []
    for m in re.finditer(
        r'<div class="qa">.*?<span class="text-\[16px\][^"]*">(.*?)</span>.*?<div class="qa-body"><div><p[^>]*>(.*?)</p>',
        faq, re.S,
    ):
        salida.append((sin_html(m.group(1)), sin_html(m.group(2))))
    return salida


def jsonld_home(index: str) -> str:
    preguntas = preguntas_de_la_home(index)
    if len(preguntas) < 10:
        raise SystemExit(f"Se leyeron solo {len(preguntas)} preguntas de la home: revisar el formato del FAQ.")
    grafo = [
        ORGANIZACION,
        SITIO_WEB,
        SOFTWARE,
        {
            "@type": "WebPage",
            "@id": f"{SITIO}/#webpage",
            "url": f"{SITIO}/",
            "name": "Capta | Software de gestión gastronómica con IA",
            "inLanguage": "es-AR",
            "isPartOf": {"@id": f"{SITIO}/#website"},
            "about": {"@id": f"{SITIO}/#software"},
            "dateModified": ACTUALIZADO,
        },
        {
            "@type": "FAQPage",
            "@id": f"{SITIO}/#faq",
            "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                for q, a in preguntas
            ],
        },
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": grafo}, ensure_ascii=False, indent=2)


def iconos_de_la_home(index: str) -> list[str]:
    return sorted(set(re.findall(
        r'class="[^"]*material-symbols-outlined[^"]*"[^>]*>\s*([a-z0-9_]+)\s*<', index)))


def link_de_iconos(index: str) -> str:
    """Pide a Google Fonts SOLO los iconos que usa la home. La fuente entera
    pesa 1,1 MB; con la lista, ~14 KB. Si se agrega un icono a la home, se
    suma solo la proxima vez que se corre esto."""
    nombres = ",".join(iconos_de_la_home(index))
    return ('<!-- iconos:inicio --><link href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:'
            f'wght,FILL@100..700,0..1&icon_names={nombres}&display=block" rel="stylesheet"/><!-- iconos:fin -->')


def testimonios_de_la_home() -> str:
    """La seccion de testimonios de la home, antes de los precios."""
    items = "".join(testimonio(t) for t in TESTIMONIOS[:3])
    return f'''<!-- testimonios:inicio (lo escribe scripts/generar_paginas.py) -->
<section id="testimonios" class="scroll-mt-14 bg-white px-5 pt-24 md:px-8 md:pt-32" aria-labelledby="testimonios-heading">
  <div class="mx-auto max-w-6xl">
    <div class="mx-auto max-w-3xl text-center">
      <p class="t-eyebrow text-[#ff6b1a]">Clientes</p>
      <h2 id="testimonios-heading" class="t-display mt-5 text-4xl text-[#1d1d1f] md:text-6xl">Lo que cuentan los locales que usan Capta.</h2>
    </div>
    <div class="mt-14 grid gap-4 md:grid-cols-2">{clientes()}</div>
    <div class="mt-4 grid gap-4 md:grid-cols-3">{items}</div>
    <p class="mt-10 text-center"><a href="/casos-de-exito" class="text-[16px] font-bold text-[#1d1d1f] underline decoration-[#ffb27a] underline-offset-4">Ver casos de éxito y más testimonios →</a></p>
  </div>
</section>
<!-- testimonios:fin -->'''


def actualizar_home() -> int:
    ruta = RAIZ / "index.html"
    index = ruta.read_text(encoding="utf-8")
    if "<!-- testimonios:inicio" in index:
        index = re.sub(r"<!-- testimonios:inicio.*?<!-- testimonios:fin -->", lambda _: testimonios_de_la_home(), index, flags=re.S)
    else:
        index = index.replace('<section id="pricing"', testimonios_de_la_home() + '\n\n<section id="pricing"', 1)
    index = re.sub(r"<!-- iconos:inicio -->.*?<!-- iconos:fin -->", lambda _: link_de_iconos(index), index, flags=re.S)
    inicio = "<!-- jsonld:inicio (lo escribe scripts/generar_paginas.py) -->\n"
    fin = "\n<!-- jsonld:fin -->"
    i = index.index(inicio) + len(inicio)
    j = index.index(fin)
    nuevo = index[:i] + '<script type="application/ld+json">\n' + jsonld_home(index) + "\n</script>" + index[j:]
    ruta.write_text(nuevo, encoding="utf-8")
    return len(preguntas_de_la_home(index))


# ----------------------------------------------------------------- sitemap

def sitemap() -> str:
    urls = [("", "1.0")] + [(p["ruta"], "0.9") for p in PAGINAS if p["ruta"] != "sobre-capta"]
    urls += [("sobre-capta", "0.7"), ("automatizacion-gastronomica.html", "0.6"), ("privacidad.html", "0.2")]
    filas = "\n".join(
        f"  <url>\n    <loc>{url_de(r)}</loc>\n    <lastmod>{ACTUALIZADO}</lastmod>\n    <priority>{prio}</priority>\n  </url>"
        for r, prio in urls
    )
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{filas}\n</urlset>\n'


def pagina_404() -> str:
    """La pagina de error: misma navegacion, enlaces utiles y noindex."""
    enlaces = "".join(
        f'<a href="/{p["ruta"]}" class="pg-tarjeta block transition-colors hover:bg-[#fff1e8]"><h3>{e(p["miga"])}</h3></a>'
        for p in PAGINAS
    )
    return f'''<!DOCTYPE html>
<html lang="es-AR">
<head>
<meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1.0"/>
<title>Página no encontrada | Capta</title>
<meta name="robots" content="noindex, follow"/>
<link rel="icon" type="image/png" sizes="48x48" href="/assets/favicon-48.png"/>
<link rel="icon" type="image/png" sizes="192x192" href="/assets/favicon-192.png"/>
<link rel="apple-touch-icon" href="/assets/apple-touch-icon.png"/>
<link rel="preconnect" href="https://fonts.googleapis.com"/>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin/>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&amp;family=Manrope:wght@400;500;600;700;800&amp;display=swap" rel="stylesheet"/>
<link rel="stylesheet" href="/capta-refresh.css?v={VERSION}"/>
<link rel="stylesheet" href="/assets/paginas.css?v={VERSION}"/>
<link rel="stylesheet" href="/assets/capta.css?v={VERSION}"/>
</head>
<body class="pg">
{nav()}
<main id="contenido">
<section class="pg-hero px-5 pb-20 pt-4 md:px-8 md:pt-16">
  <div class="mx-auto max-w-6xl">
    <p class="t-eyebrow text-[#ff6b1a]">Error 404</p>
    <h1 class="pg-h1 mt-5">Esta página no existe.</h1>
    <p class="pg-lead mt-6 max-w-2xl">Puede que el enlace esté mal escrito o que la página se haya mudado. Estas son las secciones de Capta:</p>
    <div class="mt-10 grid gap-4 sm:grid-cols-2 lg:grid-cols-4"><a href="/" class="pg-tarjeta block transition-colors hover:bg-[#fff1e8]"><h3>Inicio</h3></a>{enlaces}</div>
  </div>
</section>
</main>
{footer()}
<script src="/assets/paginas.js?v={VERSION}" defer></script>
</body>
</html>
'''


def main() -> None:
    for p in PAGINAS:
        carpeta = RAIZ / p["ruta"]
        carpeta.mkdir(exist_ok=True)
        (carpeta / "index.html").write_text(pagina(p), encoding="utf-8")
        print(f"  /{p['ruta']}")
    n = actualizar_home()
    print(f"  home: JSON-LD con {n} preguntas visibles")
    (RAIZ / "404.html").write_text(pagina_404(), encoding="utf-8")
    print("  404.html")
    (RAIZ / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    print("  sitemap.xml")


if __name__ == "__main__":
    main()
