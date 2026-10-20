"""Revisa el SEO tecnico de capta.ar sin publicar nada.

    cd herramientas && npm run verificar

Falla (codigo 1) si encuentra algo que romperia la indexacion: paginas sin H1
o con mas de uno, titulos o descripciones repetidos, canonicals a otro
dominio, JSON-LD invalido, preguntas del JSON-LD que no se ven en la pagina,
enlaces internos rotos o URLs del sitemap que no existen.
"""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

RAIZ = Path(__file__).resolve().parent.parent
SITIO = "https://capta.ar"
DOMINIO_VIEJO = "neurorest.com.ar"
# La analitica y los textos legales de la politica de privacidad nombran el
# dominio viejo a proposito: los cambia Capta cuando lo decida.
PERMITIDO_VIEJO = {"index.html": 1, "privacidad.html": 5}

errores: list[str] = []
avisos: list[str] = []


def texto(s: str) -> str:
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s))).strip()


def archivo_de(ruta: str) -> Path | None:
    """La ruta publica /x a un archivo del repo, como la sirve Vercel."""
    ruta = ruta.split("#")[0].split("?")[0]
    if ruta in ("", "/"):
        return RAIZ / "index.html"
    rel = ruta.lstrip("/")
    for candidato in (RAIZ / rel, RAIZ / rel / "index.html", RAIZ / f"{rel}.html"):
        if candidato.is_file():
            return candidato
    return None


paginas = sorted(
    [p for p in RAIZ.glob("*.html")] + [p for p in RAIZ.glob("*/index.html") if p.parent.name not in ("herramientas", "scripts", "docs", "node_modules")]
)
titulos: dict[str, str] = {}
descripciones: dict[str, str] = {}

for p in paginas:
    nombre = str(p.relative_to(RAIZ))
    s = p.read_text(encoding="utf-8")
    noindex = re.search(r'<meta name="robots" content="noindex', s) is not None

    # Dominio viejo
    viejas = s.count(DOMINIO_VIEJO)
    if viejas > PERMITIDO_VIEJO.get(nombre, 0):
        errores.append(f"{nombre}: nombra {DOMINIO_VIEJO} {viejas} veces")

    if noindex:
        continue

    # H1
    h1s = re.findall(r"<h1\b[^>]*>(.*?)</h1>", s, re.S)
    if len(h1s) != 1:
        errores.append(f"{nombre}: tiene {len(h1s)} H1")

    # Title y description
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    d = re.search(r'<meta name="description" content="([^"]*)"', s)
    if not t or not d:
        errores.append(f"{nombre}: falta title o description")
    else:
        tt, dd = html.unescape(t.group(1)).strip(), html.unescape(d.group(1)).strip()
        if tt in titulos:
            errores.append(f"{nombre}: title repetido con {titulos[tt]}")
        if dd in descripciones:
            errores.append(f"{nombre}: description repetida con {descripciones[dd]}")
        titulos[tt], descripciones[dd] = nombre, nombre
        if len(tt) > 65:
            avisos.append(f"{nombre}: title de {len(tt)} caracteres (Google corta cerca de 60)")
        if not 110 <= len(dd) <= 165:
            avisos.append(f"{nombre}: description de {len(dd)} caracteres (ideal 120-160)")

    # Canonical
    c = re.search(r'<link rel="canonical" href="([^"]+)"', s)
    if not c or not c.group(1).startswith(SITIO):
        errores.append(f"{nombre}: canonical ausente o fuera de {SITIO}")
    elif c and archivo_de(urlparse(c.group(1)).path) is None:
        errores.append(f"{nombre}: el canonical {c.group(1)} no existe")

    # JSON-LD
    visibles = texto(s)
    for bloque in re.findall(r'<script type="application/ld\+json">(.*?)</script>', s, re.S):
        try:
            datos = json.loads(bloque)
        except json.JSONDecodeError as ex:
            errores.append(f"{nombre}: JSON-LD invalido ({ex})")
            continue
        for nodo in datos.get("@graph", [datos]):
            if nodo.get("@type") == "FAQPage":
                for q in nodo["mainEntity"]:
                    if q["name"] not in visibles:
                        errores.append(f"{nombre}: la pregunta del JSON-LD no se ve en la pagina: {q['name']}")
                    respuesta = q["acceptedAnswer"]["text"]
                    if respuesta[:60] not in visibles:
                        errores.append(f"{nombre}: la respuesta del JSON-LD no coincide con la visible: {q['name']}")

    # Imagenes sin alt
    for img in re.findall(r"<img\b[^>]*>", s):
        if "alt=" not in img:
            errores.append(f"{nombre}: imagen sin alt: {img[:80]}")

    # Enlaces internos
    for href in re.findall(r'href="(/[^"]*)"', s):
        if href.startswith("//"):
            continue
        if archivo_de(href) is None:
            errores.append(f"{nombre}: enlace roto {href}")

# Sitemap
mapa = (RAIZ / "sitemap.xml").read_text(encoding="utf-8")
urls = re.findall(r"<loc>([^<]+)</loc>", mapa)
for u in urls:
    if not u.startswith(SITIO):
        errores.append(f"sitemap: URL fuera del dominio: {u}")
    elif archivo_de(urlparse(u).path) is None:
        errores.append(f"sitemap: no existe {u}")

# robots
robots = (RAIZ / "robots.txt").read_text(encoding="utf-8")
if f"Sitemap: {SITIO}/sitemap.xml" not in robots:
    errores.append("robots.txt: no apunta al sitemap de capta.ar")

for archivo in ("capta-ai-context.json", "vercel.json"):
    try:
        json.loads((RAIZ / archivo).read_text(encoding="utf-8"))
    except json.JSONDecodeError as ex:
        errores.append(f"{archivo}: JSON invalido ({ex})")

print(f"Paginas revisadas: {len(paginas)} | URLs en el sitemap: {len(urls)}")
for a in avisos:
    print(f"  aviso: {a}")
for e in errores:
    print(f"  ERROR: {e}")
if errores:
    sys.exit(1)
print("Todo en orden.")
