# Cloud Providers

A self-contained tutorial comparing Amazon Web Services (AWS), Microsoft Azure, and Google Cloud Platform (GCP). Covers compute, storage, networking, IAM, databases, serverless, observability, security, pricing, real-world case studies, and a capstone that deploys the same application on two providers.

## What you'll learn

- Regions, availability zones, and global networks
- IAM concepts and how they map across AWS, Azure, and GCP
- Compute services: VMs, autoscaling, Kubernetes, serverless, containers
- Storage services: object, block, file, archive
- Networking: VPCs, subnets, load balancers, DNS, firewalls, VPNs
- Managed databases: relational and NoSQL
- Serverless functions, event buses, messaging, and workflow orchestration
- Observability, security, and cost management tools
- Real-world usage at Netflix, HSBC, Spotify, Epic Games, Snap, and Toyota

## Open the tutorial

Open `index.html` directly in any modern browser.

## Start the capstone

```bash
# Install the provider CLIs
# AWS: https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html
# Azure: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
# GCP: https://cloud.google.com/sdk/docs/install

# Deploy the same "Hello Cloud" stack on AWS and GCP (or Azure)
# Follow the step-by-step CLI commands in the tutorial.
```

## Covered topics

1. Introduction
2. Regions, Availability Zones & Global Networks
3. Identity & Access Management
4. Compute Services
5. Storage Services
6. Networking Services
7. Managed Databases
8. Serverless & Containers
9. Observability & Security
10. Pricing & Cost Management
11. Real-World Systems
12. Capstone: Deploy on Two Providers

## Capstone acceptance criteria

- Create a VPC/VNet and public subnet on each chosen provider.
- Launch a VM and install a web server accessible over HTTP.
- Create an object storage bucket and upload an asset.
- Configure a firewall / security group rule for HTTP.
- Document the differences in CLI flow, naming, and console experience.
- Delete all resources to avoid ongoing charges.

## Real-world examples

- Netflix on AWS: elastic encoding and global CDN for streaming
- HSBC on Azure: enterprise identity, hybrid, and compliance
- Spotify on GCP: data analytics, BigQuery, Pub/Sub, GKE
- Epic Games multi-cloud: AWS bursting + private infrastructure for real-time gaming
- Snap on GCP: App Engine and fully managed services for rapid scale
- Toyota on AWS: connected car telemetry, analytics, and ML

## Run the local server

```bash
python3 -m http.server 8092
```

Then visit `http://localhost:8092/cloud-providers/index.html`.
