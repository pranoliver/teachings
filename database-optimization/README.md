# Database Optimization

A hands-on tutorial on making databases fast: indexing, reading query execution plans, partitioning, and practical query tuning.

## What you'll practice

You will optimize a realistic e-commerce database with four tables:

- `customers` — 10,000 rows
- `products` — 500 rows
- `orders` — 50,000 rows
- `order_items` — 150,000 rows

All exercises run inside a Docker PostgreSQL container. Every query is copy-paste ready.

## Open the tutorial

Open `index.html` directly in any modern browser.

## Install first

```bash
# Start PostgreSQL
docker run -d --name postgres-opt \
  -e POSTGRES_USER=admin \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=shop \
  -p 5432:5432 \
  postgres:16

# Connect
docker exec -it postgres-opt psql -U admin -d shop
```

The tutorial contains the full `CREATE TABLE` and seed data script.

## Covered topics

1. Why database optimization matters
2. PostgreSQL setup and sample e-commerce database
3. Indexing deep dive (B-tree, composite, partial, covering, expression)
4. Query execution plans with `EXPLAIN` and `EXPLAIN ANALYZE`
5. Table partitioning by range, list, and hash
6. Practical tuning workflow
7. Monitoring with `pg_stat_statements` and `pg_stat_user_indexes`
8. Capstone: optimize a slow e-commerce store

## Real-world systems mentioned

- Shopify flash-sale indexing strategies
- GitHub time-based partitioning of event tables
- Stripe composite indexes for transaction lookups
- Uber range partitioning of trip data by city and date

## Run the local server

```bash
python3 -m http.server 8084
```

Then visit `http://localhost:8084/database-optimization/index.html`.
