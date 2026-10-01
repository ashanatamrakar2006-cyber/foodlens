import { businesses } from '../mock/data.js';

function distanceKm(lat1, lng1, lat2, lng2) {
  const R = 6371;
  const toRad = (d) => (d * Math.PI) / 180;
  const dLat = toRad(lat2 - lat1);
  const dLng = toRad(lng2 - lng1);
  const a = Math.sin(dLat / 2) ** 2 +
    Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * Math.sin(dLng / 2) ** 2;
  return 2 * R * Math.asin(Math.sqrt(a));
}

export async function searchBusinesses({ q = '', category }) {
  return businesses.filter((b) =>
    b.name.toLowerCase().includes(q.toLowerCase()) &&
    (!category || b.category === category));
}

export async function getBusiness(id) {
  return businesses.find((b) => b.id === id) || null;
}

export async function nearbyBusinesses({ lat, lng, radius }) {
  return businesses
    .map((b) => ({ ...b, distanceKm: +distanceKm(lat, lng, b.lat, b.lng).toFixed(2) }))
    .filter((b) => b.distanceKm <= radius)
    .sort((a, b) => a.distanceKm - b.distanceKm);
}