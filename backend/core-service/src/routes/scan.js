import { lookupBarcode } from '../services/scanService.js';

export default async function scanRoutes(app) {
  app.get('/scan/barcode/:code', async (req, reply) => {
    const { code } = req.params;

    // Validation: sirf digits, 8 se 14 length
    if (!/^\d{8,14}$/.test(code)) {
      return reply.code(400).send({ error: 'Barcode must be 8 to 14 digits' });
    }

    try {
      const product = await lookupBarcode(code);
      if (!product) {
        return reply.code(404).send({ error: 'Product not found' });
      }
      return product;
    } catch (err) {
      req.log.error(err);
      return reply.code(502).send({ error: 'Product lookup service unavailable' });
    }
  });
}