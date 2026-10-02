import reviewRoutes from './routes/reviews.js';
import businessManageRoutes from './routes/businessManage.js';
import scanRoutes from './routes/scan.js';
import meRoutes from './routes/me.js';
import businessRoutes from './routes/businesses.js';
import Fastify from 'fastify';
import cors from '@fastify/cors';
import 'dotenv/config';

const app = Fastify({ logger: true });
await app.register(cors, { origin: (process.env.CORS_ORIGINS || '').split(',') });

app.get('/health', async () => ({ status: 'ok' }));
await app.register(businessRoutes);
await app.register(meRoutes);
await app.register(scanRoutes);
await app.register(businessManageRoutes);
await app.register(reviewRoutes);
app.setErrorHandler((err, req, reply) => {
  req.log.error(err);
  reply.status(err.statusCode || 500).send({ error: err.message });
});

await app.listen({ port: process.env.PORT || 4000, host: '0.0.0.0' });