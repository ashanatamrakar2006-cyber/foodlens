import { searchBusinesses, getBusiness, nearbyBusinesses } from '../services/businessService.js';

export default async function businessRoutes(app) {
  app.get('/businesses/search', async (req) => {
    const { q, category } = req.query;
    return searchBusinesses({ q, category });
  });

  app.get('/businesses/nearby', async (req, reply) => {
    const lat = parseFloat(req.query.lat);
    const lng = parseFloat(req.query.lng);
    const radius = parseFloat(req.query.radius || '5');
    if (Number.isNaN(lat) || Number.isNaN(lng)) {
      return reply.code(400).send({ error: 'lat and lng are required numbers' });
    }
    return nearbyBusinesses({ lat, lng, radius });
  });

  app.get('/businesses/:id', async (req, reply) => {
    const b = await getBusiness(req.params.id);
    return b || reply.code(404).send({ error: 'Business not found' });
  });
}