# Microservices Basics

A self-contained tutorial on microservice architecture: service boundaries, inter-service communication, data ownership, API gateways, resilience patterns, sagas, and observability.

## What you'll build

A food delivery backend with an API gateway, four services, and an event broker:

- **Restaurants service** — menus and availability
- **Orders service** — cart, pricing, order lifecycle
- **Payments service** — card charges and refunds
- **Delivery service** — driver assignment and tracking
- **Event broker** — RabbitMQ or Redis Streams
- **API gateway** — auth, routing, timeout/fallback, status aggregation

## Open the tutorial

Open `index.html` directly in any modern browser.

## Covered topics

1. Monolith vs microservices trade-offs
2. Designing service boundaries by business capability
3. Synchronous REST/gRPC/GraphQL calls
4. Asynchronous event-driven messaging
5. Database-per-service and eventual consistency
6. API gateway routing and cross-cutting concerns
7. Circuit breaker, retry, timeout, fallback patterns
8. Distributed transactions with sagas
9. Observability: logs, metrics, traces
10. Capstone: food delivery system

## Prerequisites

- Node.js and Express
- HTTP, REST, and JSON fundamentals
- Basic Docker and database knowledge

## Real-world examples used

- Amazon's retail team independence
- Netflix playback, recommendations, billing, and search services
- Uber's move from monolith to dispatch, payments, maps, and pricing services
- DoorDash / Deliveroo order, restaurant, delivery, and payment separation

## Run the local server

```bash
python3 -m http.server 8084
```

Then visit `http://localhost:8084/microservices-basics/index.html`.
