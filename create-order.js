// api/create-order.js
// This runs on Vercel's server, never in the browser.
// It uses RAZORPAY_KEY_SECRET, which must NEVER be exposed to the frontend.

import Razorpay from 'razorpay';

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const instance = new Razorpay({
      key_id: process.env.RAZORPAY_KEY_ID,
      key_secret: process.env.RAZORPAY_KEY_SECRET,
    });

    // amount should be sent in paise (e.g. ₹499 = 49900)
    const { amount, plan } = req.body || {};

    if (!amount || typeof amount !== 'number' || amount <= 0) {
      return res.status(400).json({ error: 'Invalid amount' });
    }

    const order = await instance.orders.create({
      amount,
      currency: 'INR',
      receipt: 'receipt_' + Date.now(),
      notes: { plan: plan || 'membership' },
    });

    return res.status(200).json(order);
  } catch (err) {
    console.error('Razorpay order creation failed:', err);
    return res.status(500).json({ error: 'Could not create order' });
  }
}
