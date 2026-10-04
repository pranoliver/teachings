# Docker: From Containers to Production

An advanced, single-page interactive tutorial covering Docker fundamentals through real-world production patterns.

## What's Included

- **Single HTML file**: `index.html` — open directly in any modern browser.
- **Sleek responsive layout**: left sidebar navigation, right content area.
- **Light & Dark themes**: Light default; toggle via the top-right button.
- **Google Font**: Outfit.
- **Tailwind CSS**: styling with a custom design, no build step required.
- **Syntax highlighting**: Highlight.js for bash, Dockerfile, YAML, Python, SQL, and Nginx snippets.
- **Copy-to-clipboard buttons** on all code blocks.
- **Interactive quizzes** with instant feedback.
- **Next / Previous navigation** at the bottom of each section.
- **SVG diagrams** comparing containers vs. VMs and reverse-proxy architecture.

## Topics Covered

1. Introduction
2. What is Docker?
3. Installing Docker
4. Images vs. Containers
5. Your First Container
6. Running a Linux OS Container (Ubuntu)
7. Running PostgreSQL in Docker
8. Running Nginx Web Server
9. Volumes & Networks
10. Writing a Dockerfile
11. Docker Compose
12. Full-Stack App: App + DB + Proxy
13. Registries & CI/CD
14. Security Best Practices
15. Production Considerations
16. Command Cheat Sheet

## Key Realistic Examples

- **OS container**: Persistent Ubuntu `devbox` with package installs and mounted script folders.
- **Database container**: PostgreSQL 16 with named volumes, table creation, and data persistence across restarts.
- **Web server container**: Nginx serving a static site and acting as a reverse proxy.
- **Multi-service stack**: Python Flask API + PostgreSQL + Nginx orchestrated with Docker Compose, including health checks and initialization scripts.
- **CI/CD**: GitHub Actions workflow for building and pushing Docker images.

## How to Use

1. Open `docker/index.html` in any modern web browser.
2. Use the left sidebar to jump between topics.
3. Toggle light/dark mode using the moon/sun icon in the header.
4. Work through checkpoints and quizzes to test your understanding.
5. Copy code blocks and run the commands in your local Docker environment.

## Files

```
docker/
├── index.html   # The complete interactive tutorial
└── README.md    # This file
```

## No Server Required

All resources (Tailwind, fonts, icons, syntax highlighter) are loaded via CDN. You can open the file directly from your file system.

## Prerequisites

Students should have Docker Desktop (macOS/Windows) or Docker Engine (Linux) installed. The tutorial includes installation commands and links.

## Customization

If you'd like to add more topics or change colors:
- Edit the `<style>` block in `index.html` for custom CSS overrides.
- Add new `<section>` elements following the existing pattern.

Happy teaching and learning!
