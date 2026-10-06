# Terraform

A self-contained tutorial on provisioning cloud infrastructure as code with Terraform. Covers providers, resources, state, modules, variables, outputs, workspaces, backends, loops, real-world case studies, and a capstone multi-tier AWS stack.

## What you'll learn

- Infrastructure-as-code concepts and the declarative model
- Installing and configuring Terraform
- Providers for AWS, Azure, GCP, Kubernetes, GitHub, Cloudflare, and more
- Resources, state files, and remote backends
- Modules, variables, outputs, and validation
- Workspaces and environment isolation
- Loops, conditionals, and dynamic blocks
- Real-world usage at Slack, Netflix, Robinhood, Lyft, GitHub, and Cloudflare

## Open the tutorial

Open `index.html` directly in any modern browser.

## Start the capstone

```bash
# Install Terraform
brew install hashicorp/tap/terraform

# Create a working directory
mkdir terraform-aws-stack && cd terraform-aws-stack

# Copy the module structure from the tutorial, then:
terraform init
terraform workspace new dev
terraform plan
terraform apply
```

## Covered topics

1. Introduction
2. Infrastructure as Code
3. Installing Terraform
4. Providers
5. Resources & State
6. Modules
7. Variables & Outputs
8. Workspaces & Backends
9. Loops, Conditionals & Dynamic Blocks
10. Real-world systems
11. Capstone: Multi-Tier AWS Stack

## Capstone acceptance criteria

- Remote S3 backend with DynamoDB locking is configured.
- A reusable network module creates a VPC, public/private subnets, and an internet gateway.
- A compute module deploys an ALB and autoscaling group in private subnets.
- A database module provisions RDS PostgreSQL with secure subnet grouping.
- A storage module creates a private S3 bucket.
- Workspaces separate dev and prod state automatically.
- `terraform plan` and `terraform apply` run without errors.

## Real-world examples

- Slack: remote state and module ownership across many AWS accounts
- Netflix: Terraform + Spinnaker for immutable infrastructure and deployments
- Robinhood: Terraform modules for security baselines and least-privilege IAM
- Lyft: internal module catalog for self-service infrastructure
- GitHub: GitHub provider to manage organizations, teams, and access controls
- Cloudflare: DNS, firewall rules, and Zero Trust policies as code

## Run the local server

```bash
python3 -m http.server 8092
```

Then visit `http://localhost:8092/terraform/index.html`.
