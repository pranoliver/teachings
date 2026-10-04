# DevOps CI/CD

A self-contained, interactive tutorial for learning DevOps principles and building real CI/CD pipelines.

## What you'll learn

- DevOps culture and the software delivery lifecycle
- CI/CD pipeline stages and best practices
- Git workflows for team collaboration
- GitHub Actions workflows for test, build, and deploy
- Docker image build and push in CI
- Managing environments and secrets
- Deployment strategies: rolling, blue/green, canary
- Monitoring, alerting, and rollbacks
- Infrastructure as Code with Docker Compose and Terraform basics

## Structure

- `index.html` — Complete tutorial in a single file with sidebar navigation, dark mode, copyable code blocks, diagrams, and quizzes.
- `README.md` — This file.

## How to use

Open `index.html` directly in any modern web browser. No local server, build step, or internet is required after the page loads.

## Topics covered

1. Introduction
2. What is DevOps?
3. CI/CD Pipeline
4. Git Workflow
5. GitHub Actions
6. Automated Testing
7. Docker in CI/CD
8. Environments & Secrets
9. Deployment Strategies
10. Monitoring & Rollbacks
11. Infrastructure as Code
12. Capstone: Node.js CI/CD

## Capstone

The final project is a complete **Node.js CI/CD pipeline** that:

- Runs tests on every push to `main`
- Builds a production Docker image tagged with the commit SHA
- Pushes the image to Docker Hub
- Deploys the container to a remote server via SSH
- Uses GitHub secrets and a `/health` endpoint for monitoring

## Required tools

- A GitHub account and repository
- Node.js and npm
- Docker installed locally
- A remote server (VPS, EC2, DigitalOcean Droplet, etc.) for deployment practice
- Optional: Docker Hub account for image registry

## Run the capstone locally

```bash
cd my-api
npm install
npm test
docker build -t myuser/my-api:latest .
docker run -d -p 3000:3000 --name my-api myuser/my-api:latest
curl http://localhost:3000/health
```

---

Part of the interactive teaching collection.
