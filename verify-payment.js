// api/verify-payment.js
// Confirms a payment is genuine before you mark someone as a paying member.
// Never trust the frontend alone — always verify server-side.

import crypto from 'crypto';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const {
      razorpay_order_id,
      razorpay_payment_id,
      razorpay_signature,
    } = req.body || {};

    if (!razorpay_order_id || !razorpay_payment_id || !razorpay_signature) {
      return res.status(400).json({ error: 'Missing payment details' });
    }

    const body = razorpay_order_id + '|' + razorpay_payment_id;
    const expectedSignature = crypto
      .createHmac('sha256', process.env.RAZORPAY_KEY_SECRET)
      .update(body)
      .digest('hex');

    const isValid = expectedSignature === razorpay_signature;

    if (!isValid) {
      return res.status(400).json({ verified: false, error: 'Invalid signature' });
    }

    // Payment is genuine here.
    // TODO: mark the user as a paying member in your database (e.g. Supabase)
    // using razorpay_order_id / razorpay_payment_id to look up who paid.

    return res.status(200).json({ verified: true });
  } catch (err) {
    console.error('Payment verification failed:', err);
    return res.status(500).json({ error: 'Verification failed' });
  }
}
