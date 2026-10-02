import { auth } from '../middleware/auth.js';
import { listNotifications, markRead } from '../services/notificationService.js';

export default async function notificationRoutes(app) {
  app.get('/notifications', { preHandler: auth }, async (req) => {
    const items = await listNotifications(req.user.id);
    return { notifications: items, unread: items.filter((n) => !n.read).length };
  });

  app.patch('/notifications/:id/read', { preHandler: auth }, async (req, reply) => {
    const result = await markRead(req.params.id, req.user.id);
    if (result.error === 'not_found') return reply.code(404).send({ error: 'Notification not found' });
    if (result.error === 'forbidden') return reply.code(403).send({ error: 'Not your notification' });
    return result.notification;
  });
}