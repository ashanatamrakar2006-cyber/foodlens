import { notifications } from '../mock/data.js';

export async function createNotification(userId, { type, message, refId }) {
  const n = {
    id: String(notifications.length + 1),
    userId,
    type,
    message,
    refId: refId || null,
    read: false,
    createdAt: new Date().toISOString(),
  };
  notifications.push(n);
  return n;
}

export async function listNotifications(userId) {
  return notifications
    .filter((n) => n.userId === userId)
    .sort((a, b) => b.createdAt.localeCompare(a.createdAt));
}

export async function markRead(id, userId) {
  const n = notifications.find((x) => x.id === id);
  if (!n) return { error: 'not_found' };
  if (n.userId !== userId) return { error: 'forbidden' };
  n.read = true;
  return { notification: n };
}