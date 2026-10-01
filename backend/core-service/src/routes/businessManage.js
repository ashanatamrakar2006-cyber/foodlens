import { auth, requireRole } from '../middleware/auth.js';
import {
  createBusiness, claimBusiness, updateBusiness, getOwnedBusinesses,
} from '../services/businessManageService.js';

const CATEGORIES = ['restaurant', 'cafe', 'street_food', 'shop', 'other'];

function validBusinessBody(b, partial = false) {
  if (!b || typeof b !== 'object') return 'Body required';
  if (!partial || b.name !== undefined) {
    if (typeof b.name !== 'string' || b.name.trim().length < 2) return 'name must be at least 2 characters';
  }
  if (!partial || b.category !== undefined) {
    if (!CATEGORIES.includes(b.category)) return `category must be one of: ${CATEGORIES.join(', ')}`;
  }
  if (!partial || b.lat !== undefined) {
    if (typeof b.lat !== 'number' || b.lat < -90 || b.lat > 90) return 'lat must be a number between -90 and 90';
  }
  if (!partial || b.lng !== undefined) {
    if (typeof b.lng !== 'number' || b.lng < -180 || b.lng > 180) return 'lng must be a number between -180 and 180';
  }
  return null;
}

export default async function businessManageRoutes(app) {
  const onlyBusiness = [auth, requireRole('business')];

  app.post('/businesses', { preHandler: onlyBusiness }, async (req, reply) => {
    const err = validBusinessBody(req.body);
    if (err) return reply.code(400).send({ error: err });
    const business = await createBusiness(req.user.id, req.body);
    return reply.code(201).send(business);
  });

  app.post('/businesses/:id/claim', { preHandler: onlyBusiness }, async (req, reply) => {
    const result = await claimBusiness(req.params.id, req.user.id);
    if (result.error === 'not_found') return reply.code(404).send({ error: 'Business not found' });
    if (result.error === 'already_claimed') return reply.code(409).send({ error: 'Business already claimed by another owner' });
    return result.business;
  });

  app.patch('/businesses/:id', { preHandler: onlyBusiness }, async (req, reply) => {
    const err = validBusinessBody(req.body, true);
    if (err) return reply.code(400).send({ error: err });
    const result = await updateBusiness(req.params.id, req.user.id, req.body);
    if (result.error === 'not_found') return reply.code(404).send({ error: 'Business not found' });
    if (result.error === 'forbidden') return reply.code(403).send({ error: 'You do not own this business' });
    return result.business;
  });

  app.get('/business/dashboard', { preHandler: onlyBusiness }, async (req) => {
    const owned = await getOwnedBusinesses(req.user.id);
    return { businesses: owned, count: owned.length };
  });
}