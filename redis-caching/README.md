# 🟥 Redis & Caching

Speed up real-world applications with Redis. This tutorial covers caching strategies, session management, rate limiting, and a capstone e-commerce cache.

## What you'll learn

- Core Redis data structures: strings, hashes, lists, sets, sorted sets
- Cache-aside and write-through caching patterns
- Session stores with TTL expiration
- Sliding-window rate limiting
- Eviction, invalidation, and real-world caching strategies
- Building a cached e-commerce API with Express

## Quick Start

Run Redis with Docker:

```bash
docker run -d --name redis -p 6379:6379 redis:latest
redis-cli ping
```

Then run the example server:

```bash
cd redis-caching
npm install express ioredis express-session connect-redis pg
node server.js
```

## Recommended prerequisites

- [Node.js & Express](../nodejs-express/)
- [SQL & Databases](../sql-databases/)

## License

Same as the parent project: MIT.
