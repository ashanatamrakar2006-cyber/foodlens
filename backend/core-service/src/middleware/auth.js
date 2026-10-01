const VALID_ROLES = ['consumer', 'business', 'authority', 'admin'];

// TEMPORARY: header se user padhta hai. Supabase aane par sirf is file ko badalna hai.
export async function auth(req, reply) {
  const userId = req.headers['x-mock-user'];
  const role = req.headers['x-mock-role'];

  if (!userId || !role) {
    return reply.code(401).send({ error: 'Unauthorized: x-mock-user and x-mock-role headers required' });
  }
  if (!VALID_ROLES.includes(role)) {
    return reply.code(400).send({ error: `Invalid role. Use one of: ${VALID_ROLES.join(', ')}` });
  }

  req.user = { id: userId, role };
}

export function requireRole(...roles) {
  return async (req, reply) => {
    if (!req.user) {
      return reply.code(401).send({ error: 'Unauthorized' });
    }
    if (!roles.includes(req.user.role)) {
      return reply.code(403).send({ error: 'Forbidden: insufficient role' });
    }
  };
}