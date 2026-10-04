# 📚 Teachings

A collection of beginner-friendly interactive technology tutorials.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Tutorials](https://img.shields.io/badge/tutorials-11-green.svg)
![HTML](https://img.shields.io/badge/HTML-5-orange?logo=html5)
![CSS](https://img.shields.io/badge/CSS-3-blue?logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-ES2022-yellow?logo=javascript)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Node.js](https://img.shields.io/badge/Node.js-18+-green?logo=node.js)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6?logo=typescript)
![Docker](https://img.shields.io/badge/Docker-latest-2496ED?logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?logo=postgresql)

## 🚀 Quick Start

Open `index.html` in your browser, or run a local server:

```bash
python -m http.server 8000
```

Then visit: [http://localhost:8000](http://localhost:8000)

## 📖 Available Tutorials

| # | 🎓 Tutorial | 📝 Description | 🔗 Link |
|---|-----------|----------------|---------|
| 1 | 🐧 [Linux Command Line](linux/) | Master the terminal: files, permissions, processes, networking, SSH, scripting, and systemd. | [Open tutorial](linux/index.html) |
| 2 | 🌐 [HTML & CSS Fundamentals](html-css/) | A complete beginner guide to modern HTML5, CSS3, Flexbox, Grid, responsive design, and a portfolio project. | [Open tutorial](html-css/index.html) |
| 3 | ⚡ [JavaScript Basics](javascript-basics/) | A beginner-friendly guide to JavaScript fundamentals with interactive playgrounds and a to-do list app. | [Open tutorial](javascript-basics/index.html) |
| 4 | 🐍 [Python Fundamentals](python-basics/) | Master Python from syntax to advanced features and build a CLI expense tracker. | [Open tutorial](python-basics/index.html) |
| 5 | 🟢 [Node.js & Express](nodejs-express/) | Build REST APIs with Node.js, Express, PostgreSQL, JWT authentication, and automated tests. | [Open tutorial](nodejs-express/index.html) |
| 6 | 🐙 [Git & GitHub](github/) | Complete beginner guide to version control with Git and collaboration on GitHub. | [Open tutorial](github/index.html) |
| 7 | 🐘 [SQL & Databases](sql-databases/) | Learn SQL with PostgreSQL using a real online store database: joins, analytics, transactions, and indexes. | [Open tutorial](sql-databases/index.html) |
| 8 | 🐳 [Docker: Containers to Production](docker/) | Advanced guide to containers: Linux OS, PostgreSQL, Nginx, Dockerfiles, Compose, and CI/CD. | [Open tutorial](docker/index.html) |
| 9 | ⚛️ [React: Modern Frontend](react/) | Build user interfaces with components, hooks, routing, and a Kanban task board. | [Open tutorial](react/index.html) |
| 10 | 🔷 [TypeScript](typescript/) | Add static types to JavaScript with real-world React and Node.js examples; capstone: typed e-commerce cart. | [Open tutorial](typescript/index.html) |
| 11 | 🚀 [DevOps CI/CD](devops-cicd/) | Automate software delivery with GitHub Actions, Docker, environments, deployment strategies, monitoring, and IaC. | [Open tutorial](devops-cicd/index.html) |

## 🛠️ How to Use

### ✅ Option 1: Open directly in a browser

1. Open `index.html` in the root folder to see all available tutorials.
2. Each tutorial is self-contained in its own folder.
3. Tutorials use Tailwind CSS via CDN, Google Fonts, and work directly in any modern browser — no build step required.
4. Use the [Glossary](glossary.html) for definitions of common terms across all tutorials.

### 🐍 Option 2: Run with Python's built-in web server

If you prefer to view the tutorials through a local web server (useful for testing or when file-protocol restrictions apply), run one of the following commands inside the project folder:

#### Python 3

```bash
python -m http.server 8000
```

#### Python 2 (legacy)

```bash
python -m SimpleHTTPServer 8000
```

Then open your browser and visit:

```text
http://localhost:8000
```

The root `index.html` will load automatically, and every tutorial will open in a new tab.

## 📥 Run locally from Git

Clone the repository and start the local server:

```bash
# Clone the repository
git clone <repository-url>

# Enter the project folder
cd teachings

# Start a local web server with Python
python -m http.server 8000
```

Then open `http://localhost:8000` in your browser.

## 🗺️ Recommended Learning Paths

- 🎨 **Frontend developer:** Linux → HTML/CSS → JavaScript → React → TypeScript → GitHub
- 🖥️ **Backend developer:** Linux → JavaScript → Node.js & Express → SQL → Docker → TypeScript → DevOps
- 🌟 **Full-stack developer:** Follow the numbered order from #1 to #11.
- ⚙️ **DevOps / Platform engineer:** Linux → Git & GitHub → SQL → Docker → Node.js → TypeScript → DevOps CI/CD

## ✨ Features

- 📄 Self-contained HTML files with sidebar navigation
- 🌙 Dark mode toggle
- 📋 Copyable code blocks
- 📊 Interactive diagrams
- ❓ Quizzes with instant feedback
- 🏗️ Capstone projects
- 📈 Local progress tracking
- 📖 Shared glossary

## 🧭 Project Structure

```text
te/
├── index.html              # Root landing page with all tutorials
├── glossary.html           # Shared glossary of common terms
├── README.md               # Project documentation
├── LICENSE                 # MIT License
├── CONTRIBUTING.md         # Contribution guidelines
├── assets/
│   └── favicons/           # Icons used across all tutorials
├── linux/
├── html-css/
├── javascript-basics/
├── python-basics/
├── nodejs-express/
├── github/
├── sql-databases/
├── docker/
├── react/
├── typescript/
└── devops-cicd/
```

## 🤝 Adding More Tutorials

When a new tutorial is added, both `README.md` and `index.html` at the root level are updated to include it.

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

🎉 Happy learning!
