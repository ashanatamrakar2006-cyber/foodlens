import { businesses, reviews } from '../mock/data.js';

export async function createReview(userId, { businessId, foodRating, hygieneRating, valueRating, comment }) {
  const b = businesses.find((x) => x.id === businessId);
  if (!b) return { error: 'business_not_found' };

  // Ek user ek business pe ek hi review de sakta hai
  if (reviews.some((r) => r.userId === userId && r.businessId === businessId)) {
    return { error: 'duplicate' };
  }

  const review = {
    id: String(reviews.length + 1),
    businessId,
    userId,
    foodRating,
    hygieneRating,
    valueRating,
    comment: comment || '',
    verified: false, // bill verify hone par true hoga
    response: null,
    createdAt: new Date().toISOString(),
  };
  reviews.push(review);
  return { review };
}

export async function listReviews(businessId) {
  return reviews
    .filter((r) => r.businessId === businessId)
    .sort((a, b) => b.createdAt.localeCompare(a.createdAt));
}

export async function respondToReview(reviewId, ownerId, text) {
  const review = reviews.find((r) => r.id === reviewId);
  if (!review) return { error: 'review_not_found' };

  const b = businesses.find((x) => x.id === review.businessId);
  if (!b || b.ownerId !== ownerId) return { error: 'forbidden' };

  review.response = { text, respondedAt: new Date().toISOString() };
  return { review };
}