import { auth } from '../middleware/auth.js';

export default async function meRoutes(app) {
  app.get('/me', { preHandler: auth }, async (req) => req.user);
}