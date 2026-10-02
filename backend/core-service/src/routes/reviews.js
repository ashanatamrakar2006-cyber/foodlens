import { createNotification } from '../services/notificationService.js';
import { auth, requireRole } from '../middleware/auth.js';
import { createReview, listReviews, respondToReview } from '../services/reviewService.js';

const isRating = (n) => Number.isInteger(n) && n >= 1 && n <= 5;

export default async function reviewRoutes(app) {
  app.post('/reviews', { preHandler: [auth, requireRole('consumer')] }, async (req, reply) => {
    const b = req.body || {};
    if (typeof b.businessId !== 'string') return reply.code(400).send({ error: 'businessId is required' });
    for (const f of ['foodRating', 'hygieneRating', 'valueRating']) {
      if (!isRating(b[f])) return reply.code(400).send({ error: `${f} must be an integer from 1 to 5` });
    }
    if (b.comment !== undefined && (typeof b.comment !== 'string' || b.comment.length > 1000)) {
      return reply.code(400).send({ error: 'comment must be text up to 1000 characters' });
    }

    const result = await createReview(req.user.id, b);
    if (result.error === 'business_not_found') return reply.code(404).send({ error: 'Business not found' });
    if (result.error === 'duplicate') return reply.code(409).send({ error: 'You already reviewed this business' });
    return reply.code(201).send(result.review);
  });

  app.get('/businesses/:id/reviews', async (req) => listReviews(req.params.id));

  app.post('/reviews/:id/respond', { preHandler: [auth, requireRole('business')] }, async (req, reply) => {
    const text = req.body?.text;
    if (typeof text !== 'string' || text.trim().length < 2 || text.length > 1000) {
      return reply.code(400).send({ error: 'text must be 2 to 1000 characters' });
    }
    const result = await respondToReview(req.params.id, req.user.id, text.trim());
    if (result.error === 'review_not_found') return reply.code(404).send({ error: 'Review not found' });
    if (result.error === 'forbidden') return reply.code(403).send({ error: 'You do not own this business' });
        await createNotification(result.review.userId, {
      type: 'review_response',
      message: 'A business responded to your review',
      refId: result.review.id,
    });
    return result.review;
  });
}