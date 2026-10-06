# Kubernetes

A self-contained tutorial on Kubernetes fundamentals and production patterns. Covers cluster architecture, pods, deployments, services, ConfigMaps, Secrets, Helm charts, real-world case studies, and a capstone e-commerce deployment.

## What you'll learn

- Kubernetes control plane and worker node architecture
- Pods and multi-container patterns
- Deployments, ReplicaSets, and rolling updates
- Services: ClusterIP, NodePort, LoadBalancer, and Ingress
- ConfigMaps and Secrets for configuration and credentials
- Helm package management and templating
- Production patterns from Spotify, Airbnb, Goldman Sachs, Reddit, and Ticketmaster

## Open the tutorial

Open `index.html` directly in any modern browser.

## Start the capstone

```bash
# Create a local cluster
minikube start --driver=docker
# or
kind create cluster --name k8s-dev

# Build the Helm chart from the tutorial and install it
helm install my-shop ./shop
```

## Covered topics

1. Introduction to Kubernetes
2. Cluster architecture
3. Pods
4. Deployments
5. Services and Ingress
6. ConfigMaps and Secrets
7. Helm
8. Real-world systems
9. Capstone: e-commerce stack

## Capstone acceptance criteria

- Helm chart installs web, API, and PostgreSQL components.
- Pods reach Ready state and pass health probes.
- Service DNS resolves inside the cluster.
- Ingress routes /api traffic to the API service and / to the web service.
- Rolling update replaces pods without downtime.
- Rollback restores the previous chart revision.

## Real-world examples

- Spotify: thousands of microservices across multi-region clusters
- Airbnb: unified batch and streaming data platform on Kubernetes
- Goldman Sachs: regulated workloads with strict multi-tenancy
- Reddit: service mesh, canary deployments, observability
- Ticketmaster: autoscaling for ticket sale traffic spikes
- Samsung: global device firmware update services

## Run the local server

```bash
python3 -m http.server 8092
```

Then visit `http://localhost:8092/kubernetes/index.html`.
