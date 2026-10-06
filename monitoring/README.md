# Monitoring & Observability

A self-contained, detailed tutorial on monitoring and observability with Prometheus, Grafana, and logging. Covers the three pillars, PromQL, alerting, Loki, instrumentation, real-world case studies, and a capstone that monitors a Node.js application.

## What you'll learn

- The difference between monitoring and observability
- Metrics, logs, and traces concepts
- Prometheus architecture, scrape model, and metric types
- PromQL: filtering, aggregation, histograms, recording rules
- Grafana dashboard design (RED, USE, four golden signals)
- Alertmanager routing, grouping, and notification receivers
- Logging fundamentals: levels, structured logs, best practices
- Loki log aggregation and LogQL
- Distributed tracing overview and OpenTelemetry
- Exporters and application instrumentation
- Real-world usage at SoundCloud, DigitalOcean, Grab, Ubisoft, ING, and GitLab

## Open the tutorial

Open `index.html` directly in any modern browser.

## Start the capstone

```bash
cd monitoring-capstone
docker-compose up -d
```

Then open Grafana at `http://localhost:3000` (admin / admin), Prometheus at `http://localhost:9090`, and generate traffic to the app at `http://localhost:3000` and `http://localhost:3000/error`.

## Covered topics

1. Introduction
2. The Three Pillars
3. Metrics with Prometheus
4. PromQL Deep Dive
5. Visualization with Grafana
6. Alerting
7. Logging Fundamentals
8. Log Aggregation with Loki
9. Tracing Overview
10. Exporters & Instrumentation
11. Real-World Systems
12. Capstone: Monitor a Node.js App

## Capstone acceptance criteria

- Node.js app exposes Prometheus metrics on `/metrics`.
- Prometheus scrapes the app and evaluates alert rules.
- Grafana dashboard shows RED-method panels (rate, errors, duration).
- Alertmanager routes HighErrorRate alerts to a webhook.
- Promtail ships application logs to Loki.
- Grafana can query Loki logs correlated by request ID.

## Real-world examples

- SoundCloud: early Prometheus production user and recording rules
- DigitalOcean: federated Prometheus for multi-region visibility
- Grab: Grafana Loki for ride-hailing log aggregation at scale
- Ubisoft: Grafana dashboards for game backend launches
- ING Bank: standardized RED/USE metrics across teams
- GitLab: Prometheus, Thanos, and Grafana for engineering and business dashboards

## Run the local server

```bash
python3 -m http.server 8092
```

Then visit `http://localhost:8092/monitoring/index.html`.
