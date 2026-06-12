const RESEND_API_URL = 'https://api.resend.com/emails';
const DEFAULT_TO_EMAIL = 'ventas@coreon.com.ar';
const DEFAULT_FROM_EMAIL = 'capta <forms@neurorest.com.ar>';

function escapeHtml(value = '') {
  return String(value)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function buildEmailPayload(body) {
  if (body.type === 'newsletter') {
    const phone = escapeHtml(body.phone || '');

    return {
      subject: 'Nuevo lead desde newsletter - capta',
      html: `
        <h2>Nuevo registro desde el newsletter</h2>
        <p><strong>Teléfono:</strong> ${phone}</p>
      `,
      text: `Nuevo registro desde el newsletter\n\nTeléfono: ${body.phone || ''}`,
    };
  }

  const name = escapeHtml(body.name || '');
  const restaurant = escapeHtml(body.restaurant || '');
  const phone = escapeHtml(body.phone || '');

  return {
    subject: 'Nueva solicitud desde la landing de capta',
    html: `
      <h2>Nueva solicitud de contacto</h2>
      <p><strong>Nombre:</strong> ${name}</p>
      <p><strong>Restaurante:</strong> ${restaurant}</p>
      <p><strong>Teléfono:</strong> ${phone}</p>
    `,
    text:
      `Nueva solicitud de contacto\n\n` +
      `Nombre: ${body.name || ''}\n` +
      `Restaurante: ${body.restaurant || ''}\n` +
      `Teléfono: ${body.phone || ''}`,
  };
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ error: 'Method not allowed' });
  }

  if (!process.env.RESEND_API_KEY) {
    return res.status(500).json({ error: 'Missing RESEND_API_KEY' });
  }

  let body;

  try {
    body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body;
  } catch (error) {
    return res.status(400).json({ error: 'Invalid JSON body' });
  }

  if (!body?.type || !body?.phone) {
    return res.status(400).json({ error: 'Missing required fields' });
  }

  if (body.type === 'contact' && (!body?.name || !body?.restaurant)) {
    return res.status(400).json({ error: 'Missing required contact fields' });
  }

  const emailContent = buildEmailPayload(body);

  const resendResponse = await fetch(RESEND_API_URL, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${process.env.RESEND_API_KEY}`,
      'Content-Type': 'application/json',
      'User-Agent': 'capta-landing-page/1.0',
    },
    body: JSON.stringify({
      from: process.env.FORMS_FROM_EMAIL || DEFAULT_FROM_EMAIL,
      to: [process.env.FORMS_TO_EMAIL || DEFAULT_TO_EMAIL],
      subject: emailContent.subject,
      html: emailContent.html,
      text: emailContent.text,
    }),
  });

  if (!resendResponse.ok) {
    const errorText = await resendResponse.text();
    return res.status(502).json({
      error: 'Email provider error',
      detail: errorText,
      hint: 'Verifica RESEND_API_KEY y que el dominio del remitente esté validado en Resend.',
    });
  }

  return res.status(200).json({ ok: true });
};
