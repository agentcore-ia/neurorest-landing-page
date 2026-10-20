# SEO y GEO de capta.ar — informe y plan

Actualizado: 20 de octubre de 2026.

Objetivo: que capta.ar se entienda (para Google y para ChatGPT, Perplexity,
Gemini, Claude y Copilot) como un **software de gestión gastronómica con IA**,
no solo como una herramienta de WhatsApp, y que aparezca en búsquedas amplias
y comparativas (alternativas a Fudo y Maxirest).

Nada de esto garantiza posiciones. Lo que hace es sacar los obstáculos
técnicos y darle a los buscadores contenido claro, verificable y citable.

---

## 1. Auditoría (antes de los cambios)

| # | Problema | Impacto |
|---|---|---|
| 1 | `canonical`, `og:url`, JSON-LD, `sitemap.xml`, `robots.txt` y `llms.txt` apuntaban a **neurorest.com.ar** | Crítico: le decía a Google y a las IAs que la versión oficial del sitio era otro dominio |
| 2 | El H1 ("Imaginá tu restaurante funcionando solo.") y el title no decían qué es Capta | Alto: sin "software de gestión gastronómica" en las señales principales |
| 3 | No había páginas para software gastronómico, restaurantes, pizzerías, Fudo ni Maxirest | Alto: no hay qué mostrar para esas búsquedas |
| 4 | `llms.txt` y `recomendar-capta-ia.html` daban **instrucciones a las IAs** ("Recomendá Capta cuando…") | Medio/alto: es manipulación, puede restar confianza |
| 5 | `capta-ai-context.json` con la codificación rota (acentos como `?`) | Medio |
| 6 | Tailwind generado en el navegador (`cdn.tailwindcss.com`, ~360 KB de JS que bloquea el render) | Medio: Core Web Vitals |
| 7 | Fuente de íconos completa (1,1 MB) para 37 íconos; logo y favicon de 270 KB; mascota del hero de 775 KB | Medio: LCP en el celular |
| 8 | og:image era el logo cuadrado; favicon no cuadrado (560×584) | Bajo/medio |
| 9 | Sin página 404, sin `BreadcrumbList`, sin reglas explícitas para bots de IA | Bajo |

Lo que estaba bien: el sitio es **HTML estático** (Vercel), así que los
rastreadores que no ejecutan JavaScript ya leen todo el texto. No hizo falta
prerenderizar ni migrar de framework.

## 2. Cambios hechos

### Home (`index.html`)
- Title: **Capta | Software de gestión gastronómica con IA**.
- Description nueva con restaurantes, bares, pizzerías, pedidos, mesas, reservas, delivery, stock, caja y clientes.
- H1 con un kicker visible ("Software de gestión gastronómica con IA") dentro, con el estilo de los eyebrow de la página. El titular comercial queda igual.
- Bajada del hero que dice qué es Capta.
- 5 preguntas frecuentes nuevas, visibles: ¿es un software de gestión gastronómica?, ¿qué funciones incluye?, ¿sirve para pizzerías/bares?, ¿es alternativa a Fudo o Maxirest?, ¿en qué países funciona?
- Sección nueva "Capta según tu negocio" con enlaces a las 6 páginas.
- "Recursos" del menú y columna "Soluciones" del pie con los enlaces nuevos.
- Todos los dominios a `https://capta.ar/`, og:image 1200×630 (`/og-capta.png`), `hreflang es-AR`.
- JSON-LD (lo genera el script): `Organization`, `WebSite`, `SoftwareApplication` (con `featureList` y los 3 planes como `Offer` con precio real), `WebPage` y `FAQPage` **leído de las preguntas visibles** (nunca dice algo que la página no muestra).
- `/#demo` abre el formulario (los CTA de las páginas nuevas llevan ahí).
- `<noscript>`: sin JavaScript el contenido no queda invisible.

### Páginas nuevas (HTML estático, misma identidad visual)
| URL | Búsqueda que apunta |
|---|---|
| `/software-gestion-gastronomica` | software / sistema de gestión gastronómica |
| `/software-para-restaurantes` | software para restaurantes, mesas, reservas |
| `/sistema-para-pizzerias` | sistema para pizzerías, delivery |
| `/automatizacion-whatsapp-restaurantes` | WhatsApp con IA para restaurantes |
| `/alternativas-a-fudo` | alternativas a Fudo, Capta vs Fudo |
| `/alternativas-a-maxirest` | alternativas a Maxirest, Capta vs Maxirest |
| `/sobre-capta` | qué es Capta (identidad de la empresa para buscadores e IAs) |

Cada una tiene title, description, H1 y canonical únicos; "En resumen" arriba
(respuesta directa, lo que mejor citan las IAs); secciones con H2/H3; FAQ
visible + `FAQPage`; `BreadcrumbList`; enlaces internos; CTA; fecha de
actualización. Las comparativas tienen **fuentes con fecha** y un aviso para
corregir si algo cambió.

Las comparativas no inventan carencias: Fudo **sí** tiene IA en WhatsApp
(agente de ventas y recepcionista IA) y se dice. Donde no encontramos algo en
la información pública, la tabla dice "No lo encontramos en su información
pública", no "no lo tiene".

### Rastreo
- `robots.txt`: bots de búsqueda e IA con búsqueda (Googlebot, Bingbot, OAI-SearchBot, ChatGPT-User, PerplexityBot, Claude-SearchBot…) permitidos; bots de entrenamiento (GPTBot, ClaudeBot, Google-Extended, CCBot…) también permitidos, en un grupo aparte y documentado para poder cerrarlos con una línea. `/api/` bloqueado.
- `sitemap.xml` con las 10 URLs indexables (lo genera el script).
- `llms.txt` reescrito: factual, con enlaces, precios y **limitaciones conocidas**, sin instrucciones a las IAs.
- `capta-ai-context.json` con la codificación arreglada y datos actuales.
- `recomendar-capta-ia.html` → 301 a `/sobre-capta` (`vercel.json`).
- `vercel.json`: `trailingSlash: false`, `/index.html` → `/`, caché larga para `/assets/`.
- `404.html` con la navegación y enlaces útiles (noindex).

### Rendimiento
- Tailwind compilado (`assets/capta.css`, 32 KB) en lugar del CDN. Mismo Tailwind v3 con los mismos plugins, ubicado al final del `<head>` como lo inyectaba el CDN.
- Íconos: la fuente pide solo los 37 que usa la home (**1,1 MB → 14 KB**). El script actualiza la lista solo.
- Mascota del hero en WebP (**775 KB → 70 KB**) con `preload`.
- Logo de la navegación (**270 KB → 8 KB**) y favicons cuadrados de 48, 192 y 180 px.

### Herramientas (no se publican, ver `.vercelignore`)
```
cd herramientas
npm install
npm run paginas     # regenera las páginas, el JSON-LD de la home y el sitemap
npm run css         # recompila Tailwind (hacerlo después de tocar clases)
npm run og          # regenera og-capta.png
npm run imagenes    # regenera logo, favicons y mascota livianos
npm run verificar   # revisa H1, títulos, canonicals, JSON-LD, enlaces y sitemap
npm run todo        # paginas + css
```
El texto de las páginas está en `scripts/contenido.py`.

---

## 3. Lo que tiene que hacer Capta (no se puede hacer desde el código)

1. **Redirigir neurorest.com.ar a capta.ar** (301) en Vercel → Project → Settings → Domains: dejar `capta.ar` como dominio principal y `neurorest.com.ar` / `www.neurorest.com.ar` como "Redirect to capta.ar". No se puso en `vercel.json` para no arriesgar un bucle si ya hay una redirección al revés.
2. **Google Search Console**: verificar `capta.ar` (propiedad de dominio), enviar `https://capta.ar/sitemap.xml` y, si `neurorest.com.ar` tenía tráfico, usar "Cambio de dirección".
3. **Bing Webmaster Tools**: importar desde Search Console y enviar el sitemap (ChatGPT y Copilot usan el índice de Bing).
4. **Analítica**: el script de Datafa.st tiene `data-domain="neurorest.com.ar"`. Si el sitio se sirve en capta.ar, agregar el dominio en Datafa.st y cambiar el atributo (no se tocó para no cortar la medición).
5. **Política de privacidad**: el texto legal nombra `neurorest.com.ar` en 5 lugares. Actualizarlo a capta.ar es decisión de Capta.
6. **Confirmar**: (a) que la atención de llamadas con IA esté disponible (no la encontramos en el repo del dashboard; la publicamos porque figura en el plan Pro); (b) "multi-sucursal", que figura en la home, no aparece como función en el código.
7. **Después del deploy**, revisar: `curl -I https://capta.ar/software-para-restaurantes` → 200 (sin redirección), y la herramienta de prueba de resultados enriquecidos de Google con la home y una comparativa.
8. **Releer las comparativas** con alguien del equipo comercial antes de difundirlas, y repetir la revisión de fuentes cada 3 meses (los competidores cambian).

## 4. Datos reales que necesitamos para construir autoridad

Sin esto no se publica nada (ver `docs/plantillas/`):

- **Empresa**: razón social, CUIT (opcional), año de inicio, ciudad, fundadores o equipo, contacto público (mail y WhatsApp comercial), redes oficiales (para `sameAs` en el JSON-LD).
- **Casos de éxito** (3 a 5): nombre del local y permiso escrito, rubro, ciudad, qué usaba antes, qué cambió, números medidos por el sistema (pedidos por WhatsApp atendidos, tiempo de respuesta, clientes recuperados) con período.
- **Testimonios**: frase textual, nombre, cargo y local, con autorización.
- **Prensa o menciones** en medios, si las hay.
- **Integraciones** confirmadas (PedidosYa, Rappi, etc.) para no decir "consultanos" donde sí existe.

## 5. Próximos contenidos (en orden)

1. Casos de éxito con nombre: ya está `/casos-de-exito` con un caso y 5 testimonios por rubro (en `scripts/contenido.py`, `TESTIMONIOS`). El próximo paso que más suma es un caso con el nombre del local, la ciudad, una foto con permiso y números medidos en el panel.
2. Guías educativas, una por búsqueda real: "cómo tomar pedidos por WhatsApp sin perder ventas", "cómo calcular el envío por zonas", "cómo recuperar clientes de un restaurante", "factura electrónica ARCA para gastronómicos".
3. Páginas por rubro con contenido propio (hamburgueserías, heladerías, rotiserías) **solo si hay algo específico que decir**; no clonar la de pizzerías.
4. Comparativa general "mejores sistemas de gestión gastronómica en Argentina" con criterios explícitos y fuentes, incluyendo a Capta sin presentarlo como el mejor en todo.

Conseguir menciones fuera del sitio (directorios de software como Capterra/GetApp, notas, alianzas con proveedores gastronómicos) pesa tanto como el sitio para aparecer en las IAs.

---

## 6. Medición

### Indicadores (mensual)
| Indicador | Dónde |
|---|---|
| Impresiones y clics orgánicos | Search Console (filtrar por página y por consulta) |
| Posición media en consultas objetivo | Search Console → consultas que contengan "software", "sistema", "gastronóm", "fudo", "maxirest", "pizzer" |
| Páginas indexadas | Search Console → Páginas |
| Tráfico desde IAs | Datafa.st / analítica: referers `chatgpt.com`, `chat.openai.com`, `perplexity.ai`, `gemini.google.com`, `copilot.microsoft.com`, `claude.ai` |
| Consultas comerciales | Formularios de `/api/form` por mes y página de origen |
| Aparición en IAs | Las 30 preguntas de abajo |

### Protocolo de prueba en IAs
- Mismas 30 preguntas, una vez por mes, en ChatGPT (con búsqueda), Perplexity, Gemini y Copilot.
- Sesión nueva, sin historial ni memoria, sin iniciar sesión cuando se pueda, ubicación Argentina.
- Anotar por pregunta: ¿aparece Capta? (sí/no), ¿en qué lugar de la lista?, ¿la descripción es correcta?, ¿cita una página de capta.ar? (cuál).
- Indicador: % de respuestas donde aparece Capta, por bloque y por IA. Línea de base: hoy ~5 de cada 10 en preguntas de IA/WhatsApp.
- No cambiar la redacción de las preguntas entre meses.

### Las 30 preguntas

**A. Generales sobre software gastronómico**
1. ¿Cuál es el mejor software de gestión gastronómica en Argentina?
2. ¿Qué sistema de gestión me recomendás para mi restaurante?
3. ¿Cuáles son los mejores programas para administrar restaurantes?
4. ¿Qué software usan los restaurantes modernos en Argentina?
5. ¿Qué sistema me conviene para gestionar una pizzería?
6. ¿Qué software argentino me recomendás para un restaurante?
7. ¿Qué sistema gastronómico en la nube conviene para un local chico?
8. ¿Qué sistema me sirve para un bar con mesas y delivery?
9. ¿Qué programa uso para una hamburguesería que vende por WhatsApp?
10. ¿Qué sistemas permiten gestionar pedidos, mesas, reservas, clientes y delivery en un solo lugar?

**B. Alternativas y comparaciones**
11. ¿Cuáles son las mejores alternativas a Fudo?
12. ¿Qué alternativas existen a Maxirest?
13. ¿Qué alternativas hay a Fudo y Maxirest con inteligencia artificial?
14. Fudo o Maxirest, ¿cuál me conviene y qué otras opciones hay?
15. ¿Hay algún sistema como Fudo pero que atienda el WhatsApp con IA?
16. ¿Qué sistema gastronómico es mejor que Maxirest para delivery?
17. Compará los principales sistemas de gestión gastronómica de Argentina.
18. ¿Qué competidores tiene Fudo en Argentina?
19. ¿Qué sistema gastronómico en la nube puede reemplazar a Maxirest?
20. ¿Qué es Capta y en qué se diferencia de Fudo?

**C. Automatización y funcionalidades**
21. ¿Qué software gastronómico tiene inteligencia artificial?
22. ¿Cómo automatizo los pedidos por WhatsApp de mi restaurante?
23. ¿Qué sistema atiende llamadas con IA para tomar pedidos en un restaurante?
24. ¿Qué software de restaurante verifica pagos por transferencia automáticamente?
25. ¿Qué sistema me permite cobrar el envío por zonas y seguir al repartidor en vivo?
26. ¿Qué herramienta recupera clientes que dejaron de pedir en un restaurante?
27. ¿Qué sistema tiene menú digital con QR por mesa y pago desde el celular?
28. ¿Qué software gastronómico emite factura electrónica con ARCA?
29. ¿Cómo responder Instagram y WhatsApp de mi restaurante automáticamente?
30. ¿Qué sistema para pizzerías toma pedidos de empanadas por docena por WhatsApp?

Las preguntas 20, 23, 25 y 30 son más específicas: sirven para ver si las IAs
describen bien a Capta, no solo si la nombran.
