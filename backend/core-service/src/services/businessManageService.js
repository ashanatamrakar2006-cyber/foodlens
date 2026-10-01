import { businesses } from '../mock/data.js';

export async function createBusiness(ownerId, { name, category, lat, lng }) {
  const business = {
    id: String(businesses.length + 1),
    name,
    category,
    lat,
    lng,
    rating: 0,
    ownerId,
    claimed: true,
  };
  businesses.push(business);
  return business;
}

export async function claimBusiness(id, ownerId) {
  const b = businesses.find((x) => x.id === id);
  if (!b) return { error: 'not_found' };
  if (b.ownerId && b.ownerId !== ownerId) return { error: 'already_claimed' };
  b.ownerId = ownerId;
  b.claimed = true;
  return { business: b };
}

export async function updateBusiness(id, ownerId, fields) {
  const b = businesses.find((x) => x.id === id);
  if (!b) return { error: 'not_found' };
  if (b.ownerId !== ownerId) return { error: 'forbidden' };

  // Sirf in fields ko update hone do (ownerId, rating, id nahi)
  for (const key of ['name', 'category', 'lat', 'lng']) {
    if (fields[key] !== undefined) b[key] = fields[key];
  }
  return { business: b };
}

export async function getOwnedBusinesses(ownerId) {
  return businesses.filter((b) => b.ownerId === ownerId);
}