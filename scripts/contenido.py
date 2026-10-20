# Contenido de las paginas de soluciones y comparativas de capta.ar.
#
# REGLAS para editar esto (son las que hacen que una pagina sirva):
#
#   * Nada de Capta que no exista en el producto. Si una funcion es de un plan,
#     se dice de que plan.
#   * Nada de un competidor que no este en SU sitio o en una fuente citada, con
#     fecha. No se inventan carencias: si no sabemos si algo lo tiene, no se
#     dice que no lo tiene.
#   * Ni testimonios, ni cifras de clientes, ni premios que no existan.
#   * Cada pagina responde una busqueda distinta: no copiar parrafos de una a
#     otra.
#
# Los textos admiten HTML simple (<a>, <strong>). Despues de editar:
#   cd herramientas && npm run todo

ACTUALIZADO = "2026-10-20"
ACTUALIZADO_TEXTO = "20 de octubre de 2026"

PRECIOS_TEXTO = (
    "Los planes publicados en capta.ar son Base ($50.000 por mes), Growth ($65.000 por mes) "
    "y Pro ($85.000 por mes, más $150 por minuto de llamada atendida por la IA)."
)

FUENTES_FUDO = [
    ("Fudo: software para restaurantes, bares y cafés (sitio oficial, Argentina)", "https://fu.do/es-ar/"),
    ("Fudo: Agentes IA", "https://lp.fu.do/agentes-ia"),
    ("Blog de Fudo: lanzamiento del chatbot para WhatsApp", "https://blog.fu.do/fudo-lanza-su-chatbot-para-whatsapp-toma-pedidos-y-cobra-automaticamente"),
    ("Blog de Fudo: recepcionista IA para reservas", "https://blog.fu.do/recepcionista-ia-para-restaurantes-como-tomar-reservas-por-whatsapp-sin-depender-del-telefono"),
]

FUENTES_MAXIREST = [
    ("Maxirest (sitio oficial, Argentina)", "https://maxirest.com.ar/"),
    ("Maxirest: características", "https://uy.maxirest.com/caracteristicas/"),
    ("Maxirest: quiénes somos", "https://uy.maxirest.com/quienes-somos/"),
    ("Maxirest Manager", "https://maxirest.com/manager"),
    ("Maxirest: términos y condiciones (soporte con IA)", "https://maxirest.com.ar/terminos-y-condiciones/"),
]

PAGINAS = [
    # ------------------------------------------------------------------
    {
        "ruta": "software-gestion-gastronomica",
        "title": "Software de gestión gastronómica con IA | Capta",
        "description": "Qué es un software de gestión gastronómica, qué tiene que resolver y cómo lo hace Capta: pedidos, mesas, reservas, delivery, caja, stock y clientes con IA.",
        "miga": "Software de gestión gastronómica",
        "eyebrow": "Guía",
        "h1": "Software de gestión gastronómica con inteligencia artificial",
        "lead": "Un sistema gastronómico reúne en un solo lugar lo que hoy está repartido entre el WhatsApp, el cuaderno de pedidos, la caja y la planilla de stock. Capta hace eso y además atiende a tus clientes con IA.",
        "resumen": [
            "Un <strong>software de gestión gastronómica</strong> organiza pedidos, salón, cocina, caja, stock y clientes de un negocio de comida.",
            "<strong>Capta</strong> es un sistema de gestión gastronómica hecho en Argentina que suma atención automática con IA por WhatsApp, Instagram y llamadas.",
            "Sirve para restaurantes, pizzerías, bares, cafeterías, hamburgueserías, rotiserías y heladerías, con salón, take away o delivery.",
            "Funciona en la nube: se usa desde la computadora, la tablet o el celular, sin instalar nada.",
        ],
        "bloques": [
            {"tipo": "prosa", "h2": "Qué es un software de gestión gastronómica", "parrafos": [
                "Es el sistema donde vive la operación diaria de un negocio de comida. Recibe los pedidos, los manda a cocina, registra cómo se cobró cada uno, descuenta lo que se usó del stock y guarda quién compró qué. Al cierre del día, te dice cuánto vendiste, qué salió más y cuánta plata tiene que haber en la caja.",
                "Durante años estos sistemas fueron, sobre todo, un punto de venta: una pantalla para cargar pedidos que llegaban por otro lado. Hoy la mayoría de los pedidos llegan por WhatsApp, por Instagram, por teléfono o desde un menú digital, y alguien tiene que contestar cada mensaje. Ahí es donde cambia lo que conviene pedirle a un sistema.",
            ]},
            {"tipo": "tarjetas", "h2": "Qué problemas tiene que resolver", "intro": "Si tu negocio tiene alguno de estos, un sistema gastronómico se paga solo en tiempo y en pedidos que no se pierden.", "items": [
                ("Mensajes sin responder en hora pico", "Mientras se arma un pedido, entran otros cinco por WhatsApp. El que tarda en contestar, pierde la venta."),
                ("Pedidos mal tomados", "Una docena que se anota como una empanada, una dirección incompleta, un adicional que nadie vio. Cada error es plata y un cliente enojado."),
                ("Pagos que no se pueden verificar", "Un comprobante de transferencia no prueba que la plata entró. Revisarlo a mano frena el despacho."),
                ("Caja y stock a ojo", "Sin registro de cada venta, el cierre de caja es una suma a mano y el stock se descubre cuando falta."),
                ("Delivery desordenado", "Precios de envío que cambian según quién atiende, repartidores sin asignar y clientes que llaman para saber dónde está su pedido."),
                ("Clientes que no vuelven", "Nadie sabe quién dejó de pedir hace un mes, y nadie tiene tiempo de escribirle."),
            ]},
            {"tipo": "tarjetas", "h2": "Qué incluye Capta", "intro": "Todo esto está en el mismo panel, conectado entre sí: el pedido que toma la IA es el mismo que llega a cocina, a la caja y al historial del cliente.", "items": [
                ("Pedidos de todos los canales", "WhatsApp, Instagram, llamadas, menú digital y mesas con QR entran ordenados al mismo tablero."),
                ("Atención con IA", "Responde consultas, arma el pedido con variantes y adicionales, toma reservas y confirma el pago. Ver <a class=\"pg-link\" href=\"/automatizacion-whatsapp-restaurantes\">automatización de WhatsApp</a>."),
                ("Salón y mesas con QR", "Cada mesa tiene su QR: el cliente ve el menú, pide, consulta la cuenta y paga desde el celular."),
                ("Cocina y comandas", "Las comandas se imprimen solas o se ven en la pantalla de cocina, separadas por sector."),
                ("Caja, stock y facturación", "Ingresos y egresos, control de stock e insumos, y factura electrónica con ARCA."),
                ("Delivery", "Precios por zona dibujados en el mapa, asignación de repartidores, liquidaciones y link de seguimiento en vivo para el cliente."),
                ("Clientes y marketing", "Historial de cada cliente, programa de puntos y campañas automáticas para recuperar a los que dejaron de pedir."),
                ("Analíticas y Gerente IA", "Ventas, productos y clientes en tiempo real, y un asistente al que le preguntás cómo viene el negocio."),
            ]},
            {"tipo": "pasos", "h2": "Cómo elegir un sistema gastronómico", "intro": "Antes de comparar marcas, conviene tener claras estas preguntas. La respuesta cambia según el negocio.", "items": [
                ("¿Por dónde entran tus pedidos?", "Si la mayoría llega por mensajes y llamadas, la atención automática importa tanto como el punto de venta."),
                ("¿Tenés salón, delivery o las dos cosas?", "Mesas, comandas y división de cuentas por un lado; zonas, repartidores y seguimiento por el otro."),
                ("¿Necesitás funcionar sin internet?", "Algunos sistemas se instalan en una computadora y siguen andando sin conexión. Los sistemas en la nube, como Capta, necesitan conexión pero no instalación."),
                ("¿Quién va a usarlo?", "Un sistema que el equipo no entiende en un día termina sin usarse. Pedí una demo con tus propios productos."),
                ("¿Cuánto cuesta de verdad?", "Sumá el plan, los costos por uso y lo que hoy perdés en pedidos sin responder."),
            ]},
            {"tipo": "prosa", "h2": "Capta frente a otros sistemas gastronómicos", "parrafos": [
                "En Argentina hay sistemas de gestión gastronómica con mucha trayectoria, como Fudo y Maxirest, que son muy completos en punto de venta, salón e integraciones. Capta pone el foco en otra parte del día: atender y vender por los canales donde hoy escriben los clientes, sin que nadie tenga que estar pendiente del celular, y ordenar el delivery de punta a punta.",
                "Si estás comparando, armamos dos comparativas con información pública de cada uno: <a href=\"/alternativas-a-fudo\">Capta y Fudo</a> y <a href=\"/alternativas-a-maxirest\">Capta y Maxirest</a>.",
            ]},
            {"tipo": "prosa", "h2": "Cuánto cuesta", "parrafos": [PRECIOS_TEXTO + " Todos incluyen el panel central; los planes más altos suman marketing automático, el Gerente IA y la atención de llamadas. <a href=\"/#pricing\">Ver qué incluye cada plan</a>."]},
        ],
        "faq": [
            ("¿Qué es un software de gestión gastronómica?", "Es el sistema que organiza la operación de un negocio de comida: pedidos, salón y mesas, cocina, caja, stock, delivery y clientes, con reportes para tomar decisiones."),
            ("¿Capta es un software de gestión gastronómica?", "Sí. Capta reúne pedidos, mesas con QR, reservas, cocina, caja, stock, facturación con ARCA, delivery y clientes en un solo panel, y suma atención automática con IA por WhatsApp, Instagram y llamadas."),
            ("¿Tengo que instalar algo?", "No. Capta funciona en la nube y se usa desde el navegador. Para imprimir comandas automáticamente se instala un programa liviano en la computadora del local."),
            ("¿Sirve para un negocio chico?", "Sí. El plan Base cubre la atención automática, los pedidos, las reservas, las mesas y el panel central. Se puede crecer de plan después."),
        ],
        "relacionadas": ["software-para-restaurantes", "sistema-para-pizzerias", "alternativas-a-fudo", "alternativas-a-maxirest"],
    },
    # ------------------------------------------------------------------
    {
        "ruta": "software-para-restaurantes",
        "title": "Software para restaurantes: pedidos, mesas y reservas | Capta",
        "description": "Software para restaurantes con salón y delivery: mesas con QR, reservas, comandas a cocina, caja, stock y atención automática por WhatsApp con Capta.",
        "miga": "Software para restaurantes",
        "eyebrow": "Restaurantes",
        "h1": "Software para restaurantes que ordena el salón, la cocina y los mensajes",
        "lead": "Un restaurante trabaja en tres frentes a la vez: las mesas, la cocina y el celular que no para de sonar. Capta los conecta para que un pedido pase de uno a otro sin que nadie lo vuelva a escribir.",
        "resumen": [
            "Mesas con QR: el cliente ve el menú, pide, consulta la cuenta y paga desde la mesa.",
            "Reservas tomadas por la IA en WhatsApp o por teléfono, con los datos del cliente en el panel.",
            "Comandas que salen solas a la impresora o a la pantalla de cocina.",
            "Caja, stock, facturación con ARCA y analíticas en el mismo sistema.",
        ],
        "bloques": [
            {"tipo": "tarjetas", "h2": "Un día de servicio con Capta", "intro": "Lo que pasa en un restaurante desde que abre hasta que cierra la caja.", "items": [
                ("Antes de abrir", "La IA ya contestó las consultas de la mañana y tomó las reservas del día. Las ves en el panel, con nombre, cantidad de personas y horario."),
                ("Servicio de mediodía", "Los clientes escanean el QR de su mesa, piden desde el celular y la comanda llega a cocina. El mozo atiende en vez de anotar."),
                ("Pedidos para llevar", "Mientras tanto, los pedidos por WhatsApp e Instagram entran armados, con la forma de pago y el horario de retiro."),
                ("La cuenta", "El cliente pide la cuenta desde la mesa, la divide si quiere y paga con Mercado Pago. La mesa se libera en el panel."),
                ("Cierre", "La caja suma cada venta por forma de pago, el stock descuenta lo que se usó y las analíticas te muestran qué se vendió más."),
            ]},
            {"tipo": "tarjetas", "h2": "Lo que necesita un restaurante, en un solo sistema", "items": [
                ("Menú digital con tu identidad", "Logo, colores y categorías propias, con fotos, variantes y adicionales. El mismo menú sirve para la mesa y para el delivery."),
                ("Reservas", "Por chat o por llamada, directo al panel, sin cuaderno ni planilla."),
                ("Mesas y salón", "El estado de cada mesa y lo que lleva consumido, en tiempo real."),
                ("Cocina", "Comandas impresas o en pantalla, separadas por sector."),
                ("Caja y facturación", "Ingresos, egresos, formas de pago y factura electrónica con ARCA."),
                ("Clientes", "Quién viene, qué pide y cada cuánto. Y campañas para los que dejaron de venir."),
            ]},
            {"tipo": "prosa", "h2": "Por qué la atención automática importa en un restaurante", "parrafos": [
                "Un restaurante con salón lleno no tiene a nadie libre para contestar el WhatsApp. Las consultas de horario, de menú sin gluten o de si hay lugar para ocho personas quedan sin responder, y esas personas reservan en otro lado.",
                "La IA de Capta contesta esas preguntas con la información real de tu local (menú, horarios, precios, disponibilidad) y, si el cliente quiere pedir o reservar, lo deja anotado en el panel. Si una conversación necesita a una persona, la podés tomar vos en cualquier momento. Más detalle en <a href=\"/automatizacion-whatsapp-restaurantes\">automatización de WhatsApp para restaurantes</a>.",
            ]},
            {"tipo": "prosa", "h2": "Planes", "parrafos": [PRECIOS_TEXTO + " La toma de reservas y el control de mesas están desde el plan Base. <a href=\"/#pricing\">Ver los planes</a>."]},
        ],
        "faq": [
            ("¿Capta sirve para un restaurante con salón y delivery a la vez?", "Sí. Las mesas con QR, las reservas y la cocina conviven con los pedidos de WhatsApp, Instagram y el menú digital en el mismo panel."),
            ("¿Los clientes pueden pagar desde la mesa?", "Sí. Desde el QR de la mesa pueden ver la cuenta, dividirla y pagar con Mercado Pago."),
            ("¿Cómo se toman las reservas?", "La IA consulta la disponibilidad y toma la reserva por chat o, en el plan Pro, por teléfono. Queda registrada en el panel con los datos del cliente."),
            ("¿Puedo seguir usando mozos?", "Claro. Capta ayuda al equipo, no lo reemplaza: los mozos pueden cargar pedidos y el QR es una opción más para el cliente."),
        ],
        "relacionadas": ["software-gestion-gastronomica", "automatizacion-whatsapp-restaurantes", "sistema-para-pizzerias", "alternativas-a-fudo"],
    },
    # ------------------------------------------------------------------
    {
        "ruta": "sistema-para-pizzerias",
        "title": "Sistema para pizzerías con pedidos por WhatsApp | Capta",
        "description": "Sistema para pizzerías: pedidos por WhatsApp tomados por IA, empanadas por docena, zonas de delivery, repartidores, seguimiento en vivo y caja en Capta.",
        "miga": "Sistema para pizzerías",
        "eyebrow": "Pizzerías",
        "h1": "Sistema para pizzerías: pedidos, delivery y caja sin perder un mensaje",
        "lead": "En una pizzería el viernes a la noche se decide el mes. Los pedidos entran todos juntos, casi todos por WhatsApp y casi todos para delivery. Capta está pensado para ese momento.",
        "resumen": [
            "La IA toma pedidos por WhatsApp con cantidades, variantes y adicionales, incluidas las empanadas por docena y media docena.",
            "El envío se calcula solo según la zona de la dirección, dibujada en el mapa.",
            "Los pedidos se asignan a repartidores y el cliente recibe un link para seguirlo en vivo.",
            "Caja, comandas a cocina y facturación con ARCA, en el mismo sistema.",
        ],
        "bloques": [
            {"tipo": "tarjetas", "h2": "Lo que más le cuesta a una pizzería", "items": [
                ("Hora pico concentrada", "El 80% del trabajo entra en dos o tres horas. Si el teléfono y el WhatsApp dependen de una persona, se forma la cola."),
                ("Pedidos con muchas variantes", "Mitad de una, mitad de otra, sin cebolla, una docena surtida. Cada detalle mal anotado es un pedido para rehacer."),
                ("El envío", "Cuánto se cobra a cada barrio, quién lleva qué pedido y cuánto tarda."),
                ("Clientes que preguntan dónde está su pedido", "Cada llamada para preguntar es una llamada que no es un pedido nuevo."),
            ]},
            {"tipo": "pasos", "h2": "Un pedido por WhatsApp, de punta a punta", "items": [
                ("El cliente escribe", "“¿Me mandás una grande de muzza y una docena de empanadas de carne?”"),
                ("La IA arma el pedido", "Toma cada producto con su cantidad y sus opciones, pregunta lo que falta (dirección, forma de pago) y le confirma el total con el envío de su zona."),
                ("El pedido llega a la cocina", "Entra al panel y la comanda se imprime sola."),
                ("Sale el delivery", "Se asigna a un repartidor. El cliente recibe el link para seguirlo en el mapa."),
                ("Se cobra y se registra", "La caja anota cómo se pagó; si fue por transferencia, Capta verifica que la plata haya entrado."),
            ]},
            {"tipo": "prosa", "h2": "Delivery propio o con Capta Delivery", "parrafos": [
                "Si tenés repartidores propios, Capta les asigna los pedidos, calcula lo que le corresponde a cada uno y le manda al cliente el seguimiento. Las zonas y los precios de envío los dibujás vos en el mapa.",
                "En las ciudades donde opera, <strong>Capta Delivery</strong> suma una red de repartidores que toman los pedidos de los locales adheridos, y una app de pedidos donde los clientes de la ciudad encuentran tu pizzería. Consultanos si está disponible en tu ciudad.",
            ]},
            {"tipo": "prosa", "h2": "Planes", "parrafos": [PRECIOS_TEXTO + " <a href=\"/#pricing\">Ver qué incluye cada plan</a>."]},
        ],
        "faq": [
            ("¿La IA entiende pedidos como “una docena y media de empanadas”?", "Sí. Capta interpreta cantidades por docena, media docena y docena y media, y las asigna a cada gusto, no al pedido entero."),
            ("¿Cómo se calcula el envío?", "Dibujás las zonas de entrega en el mapa con su precio. Capta ubica la dirección del cliente y le cobra la de su zona."),
            ("¿Puedo usar mis propios repartidores?", "Sí. Capta asigna los pedidos a tus repartidores, lleva las liquidaciones y envía el seguimiento al cliente."),
            ("¿Las comandas se imprimen solas?", "Sí. Con el programa de impresión instalado en la computadora del local, cada pedido confirmado sale por la impresora de cocina."),
        ],
        "relacionadas": ["automatizacion-whatsapp-restaurantes", "software-gestion-gastronomica", "software-para-restaurantes", "alternativas-a-maxirest"],
    },
    # ------------------------------------------------------------------
    {
        "ruta": "automatizacion-whatsapp-restaurantes",
        "title": "Automatización de WhatsApp para restaurantes con IA | Capta",
        "description": "Cómo Capta automatiza el WhatsApp de un restaurante: la IA responde consultas, toma pedidos y reservas, verifica pagos y deja todo ordenado en el panel.",
        "miga": "Automatización de WhatsApp",
        "eyebrow": "WhatsApp",
        "h1": "Automatización de WhatsApp para restaurantes, con inteligencia artificial",
        "lead": "No es un menú de opciones ni una respuesta automática. Es un agente de IA que conversa como alguien del local, conoce tu carta y deja cada pedido listo en el sistema.",
        "resumen": [
            "La IA de Capta responde en tu número de WhatsApp con la información real del local: menú, precios, horarios, zonas de envío.",
            "Arma pedidos completos (productos, variantes, cantidades, entrega y pago) y los manda al panel y a cocina.",
            "Toma reservas, envía el link de pago de Mercado Pago y verifica las transferencias.",
            "Podés tomar cualquier conversación a mano cuando quieras.",
        ],
        "bloques": [
            {"tipo": "tarjetas", "h2": "Qué hace la IA en el WhatsApp de tu local", "items": [
                ("Responde consultas", "Horarios, si hay opciones sin gluten, cuánto sale el envío a un barrio, si aceptan tarjeta."),
                ("Toma pedidos", "Productos, variantes y adicionales, cantidades, retiro o envío, dirección y forma de pago."),
                ("Retoma pedidos", "Si el cliente quiere cambiar algo de un pedido que ya confirmó, lo edita sin empezar de cero."),
                ("Toma reservas", "Consulta la disponibilidad y deja la reserva registrada en el panel."),
                ("Cobra", "Envía el link de pago y, si pagan por transferencia, verifica que la plata haya entrado antes de confirmar."),
                ("Entiende audios y fotos", "Transcribe los audios y lee las imágenes que manda el cliente."),
            ]},
            {"tipo": "prosa", "h2": "Por qué no es un bot de respuestas automáticas", "parrafos": [
                "Los bots de opciones (“escribí 1 para ver el menú”) obligan al cliente a adaptarse al bot. La IA de Capta entiende lo que el cliente escribe como lo escribiría a una persona y le contesta igual.",
                "Para que eso no termine en pedidos mal tomados, la IA no inventa: trabaja con el menú cargado en Capta y con reglas que controlan cantidades, precios y productos. Si el cliente pide algo que no está en la carta, se lo dice.",
            ]},
            {"tipo": "tarjetas", "h2": "También en Instagram y por teléfono", "items": [
                ("Instagram", "Los mensajes directos de Instagram se atienden igual que el WhatsApp, y los pedidos llegan al mismo panel."),
                ("Llamadas con IA", "En el plan Pro, la IA atiende el teléfono: responde consultas, toma pedidos y agenda reservas, incluso con varias llamadas a la vez."),
                ("Menú digital", "Para el cliente que prefiere elegir solo, el menú digital y las mesas con QR mandan los pedidos al mismo lugar."),
            ]},
            {"tipo": "prosa", "h2": "Qué necesitás para empezar", "parrafos": [
                "Tu número de WhatsApp, el menú con precios, los horarios, las formas de pago y las zonas de entrega. Con eso se configura Capta para que empiece a atender.",
                PRECIOS_TEXTO + " La atención automática por WhatsApp e Instagram está desde el plan Base. <a href=\"/#pricing\">Ver los planes</a>.",
            ]},
        ],
        "faq": [
            ("¿Puedo usar mi número de WhatsApp actual?", "Sí. Capta se conecta al número de WhatsApp del local, así los clientes siguen escribiendo al mismo lugar."),
            ("¿Qué pasa si la IA no sabe responder algo?", "Podés tomar la conversación desde el panel en cualquier momento y contestar vos."),
            ("¿La IA puede equivocarse con un pedido?", "Como cualquier persona, puede pasar. Por eso trabaja solo con tu menú, controla cantidades y precios con reglas, y te muestra cada pedido en el panel antes de prepararlo."),
            ("¿Funciona con mensajes de voz?", "Sí. Capta transcribe los audios y los responde como cualquier otro mensaje."),
        ],
        "relacionadas": ["software-para-restaurantes", "sistema-para-pizzerias", "software-gestion-gastronomica", "alternativas-a-fudo"],
    },
    # ------------------------------------------------------------------
    {
        "ruta": "alternativas-a-fudo",
        "title": "Alternativas a Fudo: comparación con Capta | Capta",
        "description": "¿Buscás alternativas a Fudo? Comparamos Capta y Fudo con información pública de cada uno: funciones, IA, delivery y cuándo conviene cada sistema.",
        "miga": "Alternativas a Fudo",
        "eyebrow": "Comparativa",
        "h1": "Alternativas a Fudo: cómo se compara Capta",
        "lead": "Fudo es uno de los sistemas de gestión gastronómica más usados en Argentina. Si estás evaluando alternativas, acá tenés en qué se parece Capta, en qué se diferencia y cuándo conviene cada uno.",
        "resumen": [
            "Fudo y Capta son sistemas de gestión gastronómica en la nube, con pedidos, mesas, cocina, caja, stock y facturación con ARCA.",
            "Los dos tienen IA para atender WhatsApp. Según su sitio, Fudo ofrece un agente de ventas y una recepcionista IA para reservas.",
            "Capta además atiende Instagram y llamadas con IA, y suma delivery propio con zonas, repartidores y seguimiento, más campañas para recuperar clientes.",
            "Fudo tiene una terminal de cobro propia e integraciones con apps de delivery como PedidosYa, Rappi y Uber Eats, según su sitio.",
        ],
        "aviso": "Esta comparación usa información pública de Fudo publicada en su sitio y su blog, consultada el " + ACTUALIZADO_TEXTO + ". Los productos cambian: confirmá cualquier dato con cada empresa antes de decidir. Si ves algo desactualizado, escribinos y lo corregimos.",
        "bloques": [
            {"tipo": "tabla", "h2": "Capta y Fudo, función por función", "caption": "Según la información pública de cada empresa al " + ACTUALIZADO_TEXTO + ".",
             "columnas": ["", "Capta", "Fudo (según su sitio)"],
             "filas": [
                ("Tipo de sistema", "En la nube, desde el navegador", "En la nube (software online)"),
                ("Salón, mesas y comandas", "Mesas con QR, comandas impresas o en pantalla de cocina", "Mapa de salas y mesas, pantalla de cocina (KDS) e impresora"),
                ("Caja y stock", "Caja, ingresos y egresos, stock e insumos", "Arqueo de caja, recetas que descuentan insumos, alertas de stock"),
                ("Facturación electrónica", "Sí, con ARCA", "Sí, con ARCA"),
                ("IA en WhatsApp", "Agente que responde, toma pedidos, reservas y verifica pagos", "Agente de ventas que toma pedidos y envía el link de pago; recepcionista IA para reservas"),
                ("IA en Instagram y llamadas", "Sí (llamadas en el plan Pro)", "No lo encontramos en su información pública"),
                ("Cobros", "Mercado Pago y verificación de transferencias", "Terminal de cobro propia, varios medios de pago, división de cuentas"),
                ("Integraciones con apps de delivery", "Consultanos según tu caso", "PedidosYa, Rappi y Uber Eats"),
                ("Delivery propio", "Zonas en el mapa, repartidores, liquidaciones y seguimiento en vivo", "Gestión de delivery y tienda online"),
                ("Recuperar clientes", "Campañas automáticas a clientes que dejaron de pedir, puntos", "No lo encontramos en su información pública"),
             ]},
            {"tipo": "dos", "h2": "Cuándo conviene cada uno", "izquierda": ("Puede convenirte Capta si…", [
                "La mayoría de tus pedidos entra por WhatsApp, Instagram o teléfono y querés que una IA los atienda de punta a punta.",
                "Hacés delivery con repartidores propios y querés zonas, asignación y seguimiento en vivo para el cliente.",
                "Querés campañas automáticas para recuperar a los clientes que dejaron de pedir.",
                "Querés preguntarle al sistema cómo viene el negocio (Gerente IA).",
             ]), "derecha": ("Puede convenirte Fudo si…", [
                "Querés una terminal de cobro integrada al sistema.",
                "Recibís muchos pedidos por PedidosYa, Rappi o Uber Eats y necesitás que entren directo.",
                "Buscás una plataforma con una base grande de negocios en la región.",
             ])},
            {"tipo": "prosa", "h2": "Lo que conviene probar antes de cambiar de sistema", "parrafos": [
                "Pedí una demo de cada uno con tu propio menú y un caso real: un pedido complicado por WhatsApp, una reserva para un grupo y un cierre de caja. Ahí se ve la diferencia más que en cualquier tabla.",
                "Preguntá también cuánto cuesta el total por mes con lo que vas a usar. " + PRECIOS_TEXTO,
            ]},
        ],
        "faq": [
            ("¿Capta es una alternativa a Fudo?", "Puede serlo. Los dos son sistemas de gestión gastronómica en la nube. Capta pone más foco en la atención automática con IA en WhatsApp, Instagram y llamadas, y en el delivery propio; Fudo, en el punto de venta, su terminal de cobro y las integraciones con apps de delivery."),
            ("¿Fudo tiene inteligencia artificial?", "Sí. Según su sitio y su blog, Fudo ofrece un agente de IA para WhatsApp que toma pedidos y envía el link de pago, y una recepcionista IA para reservas."),
            ("¿Puedo pasar mi menú de Fudo a Capta?", "Sí. Para empezar con Capta alcanza con tu menú, precios, horarios, formas de pago y zonas de entrega. Te ayudamos a cargarlos."),
        ],
        "fuentes": FUENTES_FUDO,
        "relacionadas": ["alternativas-a-maxirest", "software-gestion-gastronomica", "automatizacion-whatsapp-restaurantes", "software-para-restaurantes"],
    },
    # ------------------------------------------------------------------
    {
        "ruta": "alternativas-a-maxirest",
        "title": "Alternativas a Maxirest: comparación con Capta | Capta",
        "description": "¿Buscás alternativas a Maxirest? Comparamos Capta y Maxirest: sistema instalado o en la nube, atención con IA, delivery y cuándo conviene cada uno.",
        "miga": "Alternativas a Maxirest",
        "eyebrow": "Comparativa",
        "h1": "Alternativas a Maxirest: cómo se compara Capta",
        "lead": "Maxirest es un software gastronómico con más de treinta años en el mercado. Si estás pensando en una alternativa, la pregunta de fondo es otra: ¿querés un sistema instalado en tu computadora o uno en la nube, y cuánto pesa la atención de mensajes en tu negocio?",
        "resumen": [
            "Maxirest desarrolla software para gastronomía desde 1991, según su sitio. Su punto de venta (Maxirest Pro) se instala en Windows y puede seguir funcionando sin internet.",
            "Capta es un sistema en la nube: no se instala, se usa desde el navegador y necesita conexión.",
            "Los dos cubren salón, mostrador, delivery, caja y facturación electrónica.",
            "Capta suma atención automática con IA por WhatsApp, Instagram y llamadas, delivery propio con seguimiento en vivo y campañas para recuperar clientes.",
        ],
        "aviso": "Esta comparación usa información pública de Maxirest publicada en sus sitios, consultada el " + ACTUALIZADO_TEXTO + ". Confirmá cualquier dato con cada empresa antes de decidir. Si ves algo desactualizado, escribinos y lo corregimos.",
        "bloques": [
            {"tipo": "tabla", "h2": "Capta y Maxirest, función por función", "caption": "Según la información pública de cada empresa al " + ACTUALIZADO_TEXTO + ".",
             "columnas": ["", "Capta", "Maxirest (según su sitio)"],
             "filas": [
                ("Tipo de sistema", "En la nube, desde el navegador", "Punto de venta instalado en Windows 10/11 Pro de 64 bits"),
                ("Sin internet", "Necesita conexión", "Puede operar sin conexión (el soporte y las integraciones la requieren)"),
                ("Salón, mostrador y delivery", "Sí", "Sí"),
                ("Comandas a cocina", "Impresas o en pantalla de cocina", "Monitores de cocina (Maxirest Kitchen)"),
                ("Facturación electrónica", "Sí, con ARCA", "Sí, integrada"),
                ("Monitoreo a distancia", "Panel web y Gerente IA", "App Maxirest Manager"),
                ("Atención de clientes con IA", "WhatsApp, Instagram y llamadas (llamadas en el plan Pro)", "No lo encontramos en su información pública (su IA está en el soporte y en alertas para el negocio)"),
                ("Integraciones", "Mercado Pago; apps de delivery: consultanos", "PedidosYa, Rappi, Mercado Pago y Alax, entre otras"),
                ("Delivery propio", "Zonas en el mapa, repartidores, liquidaciones y seguimiento en vivo", "Gestión de delivery"),
                ("Toma de pedidos por mozos", "Desde el celular, en el navegador", "App de pedidos para Android 8 o superior"),
             ]},
            {"tipo": "dos", "h2": "Cuándo conviene cada uno", "izquierda": ("Puede convenirte Capta si…", [
                "No querés instalar ni mantener un sistema en una computadora del local.",
                "Muchos pedidos te llegan por WhatsApp, Instagram o teléfono y querés que una IA los atienda.",
                "Hacés delivery y querés zonas, repartidores y seguimiento en vivo para el cliente.",
                "Querés usar el sistema desde cualquier dispositivo, también desde iPhone.",
             ]), "derecha": ("Puede convenirte Maxirest si…", [
                "Necesitás que el punto de venta siga funcionando aunque se corte internet.",
                "Preferís un sistema instalado en tu computadora.",
                "Valorás una empresa con más de treinta años en el rubro y su red de soporte.",
             ])},
            {"tipo": "prosa", "h2": "Qué tener en cuenta si venís de un sistema instalado", "parrafos": [
                "Un sistema en la nube cambia algunas costumbres: los datos no están en la computadora del local sino en el servidor, se puede entrar desde cualquier lado y no hay que hacer copias de seguridad a mano. A cambio, necesita conexión estable en el local.",
                "Antes de cambiar, armá una lista de lo que usás todos los días en tu sistema actual y pedí una demo de Capta con esos casos. " + PRECIOS_TEXTO,
            ]},
        ],
        "faq": [
            ("¿Capta es una alternativa a Maxirest?", "Puede serlo, sobre todo si buscás un sistema en la nube con atención automática con IA y delivery propio. Si necesitás que el sistema funcione sin internet, Maxirest tiene esa ventaja."),
            ("¿Capta funciona sin internet?", "No. Capta funciona en la nube y necesita conexión. A cambio, no hay que instalarlo y se puede usar desde cualquier dispositivo."),
            ("¿Maxirest tiene inteligencia artificial?", "Según sus términos y su sitio, Maxirest usa IA en su soporte (un chatbot para consultas de uso) y en alertas y consejos para el negocio. No encontramos información pública sobre IA que atienda a los clientes del restaurante."),
        ],
        "fuentes": FUENTES_MAXIREST,
        "relacionadas": ["alternativas-a-fudo", "software-gestion-gastronomica", "software-para-restaurantes", "sistema-para-pizzerias"],
    },
    # ------------------------------------------------------------------
    {
        "ruta": "sobre-capta",
        "title": "Sobre Capta: qué es, qué ofrece y para quién es | Capta",
        "description": "Capta es un software de gestión gastronómica con IA hecho en Argentina. Qué productos ofrece, para qué negocios es, en qué mercado opera y cómo contactarnos.",
        "miga": "Sobre Capta",
        "eyebrow": "Sobre Capta",
        "h1": "Sobre Capta",
        "lead": "Capta es una plataforma de gestión gastronómica con inteligencia artificial, hecha en Argentina para restaurantes, bares, pizzerías y locales de comida.",
        "resumen": [
            "<strong>Qué es:</strong> un software de gestión gastronómica en la nube que suma atención automática con IA.",
            "<strong>Para quién:</strong> restaurantes, pizzerías, hamburgueserías, rotiserías, heladerías, cafeterías y bares, con salón, take away o delivery.",
            "<strong>Dónde:</strong> hecho en Argentina, para negocios gastronómicos de Argentina.",
            "<strong>Sitio oficial:</strong> <a class=\"pg-link\" href=\"https://capta.ar/\">capta.ar</a>. Panel de clientes: <a class=\"pg-link\" href=\"https://app.capta.ar/\">app.capta.ar</a>.",
        ],
        "bloques": [
            {"tipo": "tarjetas", "h2": "Productos", "items": [
                ("Capta (plataforma)", "El sistema de gestión: pedidos de todos los canales, mesas con QR, reservas, cocina, caja, stock, facturación con ARCA, clientes, marketing y analíticas."),
                ("Atención con IA", "Agente que atiende WhatsApp e Instagram y, en el plan Pro, llamadas telefónicas."),
                ("Menú digital", "Menús con la identidad de cada local, para mesas con QR y pedidos online."),
                ("Capta Delivery", "En las ciudades donde opera: red de repartidores, seguimiento en vivo y una app de pedidos con los locales adheridos."),
                ("Gerente IA", "Asistente para el dueño: le preguntás cómo vienen las ventas y te responde con los datos del negocio."),
            ]},
            {"tipo": "prosa", "h2": "Qué problema resuelve", "parrafos": [
                "Los negocios gastronómicos venden cada vez más por mensajes y llamadas, pero siguen operando con herramientas separadas: el celular para atender, un cuaderno o un sistema de punto de venta para los pedidos, una planilla para el stock. Capta reúne todo en un sistema y automatiza la parte más repetitiva, que es atender y tomar pedidos.",
            ]},
            {"tipo": "prosa", "h2": "Precios", "parrafos": [PRECIOS_TEXTO + " <a href=\"/#pricing\">Ver qué incluye cada plan</a>."]},
            {"tipo": "prosa", "h2": "Más información", "parrafos": [
                "Guías: <a href=\"/software-gestion-gastronomica\">software de gestión gastronómica</a>, <a href=\"/software-para-restaurantes\">software para restaurantes</a>, <a href=\"/sistema-para-pizzerias\">sistema para pizzerías</a> y <a href=\"/automatizacion-whatsapp-restaurantes\">automatización de WhatsApp</a>. Comparativas: <a href=\"/alternativas-a-fudo\">Capta y Fudo</a>, <a href=\"/alternativas-a-maxirest\">Capta y Maxirest</a>. Datos para sistemas automáticos: <a href=\"/llms.txt\">llms.txt</a>.",
            ]},
        ],
        "faq": [
            ("¿Qué es Capta?", "Capta es un software de gestión gastronómica con inteligencia artificial, hecho en Argentina. Centraliza pedidos, mesas, reservas, delivery, caja, stock y clientes, y atiende WhatsApp, Instagram y llamadas con IA."),
            ("¿Capta utiliza inteligencia artificial?", "Sí. La IA atiende a los clientes por WhatsApp, Instagram y teléfono, toma pedidos y reservas, arma campañas de marketing y responde las consultas del dueño en el Gerente IA."),
            ("¿Para qué tipo de negocio conviene Capta?", "Para negocios gastronómicos que reciben muchos pedidos o consultas por mensajes y llamadas, o que hacen delivery y quieren ordenarlo de punta a punta."),
        ],
        "relacionadas": ["software-gestion-gastronomica", "alternativas-a-fudo", "alternativas-a-maxirest", "automatizacion-whatsapp-restaurantes"],
    },
]
