# Agent Guide

This document summarizes the conventions, structure, and workflows for working on the **interactive technology tutorial collection** in this repository.

## Project Overview

A set of self-contained, browser-based tutorials. Each tutorial is a single HTML file with its own sidebar table of contents, dark mode toggle, copyable code blocks, a capstone project, and a knowledge-check quiz. No build step is required.

## Directory Layout

```text
/
├── index.html                    # Landing page: hero, filters, progress, tutorial grid, paths
├── README.md                     # Human-facing overview, badge, tutorial table
├── AGENTS.md                     # This file
├── assets/
│   ├── styles.css                # Shared stylesheet, Tailwind utility overrides, themes
│   ├── favicons/                 # Per-tutorial favicon SVGs/PNGs used in cards
│   └── svg/                      # Larger/copyable SVG illustrations when needed
├── TUTORIAL_NAME/                # Lowercase, kebab-case directory
│   └── index.html                # Single tutorial page
└── ...
```

## Tutorial Conventions

### File Naming

- Tutorial directory: lowercase words separated by hyphens, e.g. `nodejs-express`, `secure-authentication`.
- Tutorial page: always `index.html` inside that directory.
- Favicon: `assets/favicons/{tutorial-id}.svg` (PNG only when a proper SVG is unavailable).
- Large SVG: `assets/svg/{tutorial-id}.svg` when the landing page or tutorial needs a bigger brand illustration.

### Tutorial Page Structure

Every `index.html` should include:

1. **Head**
   - `<meta charset="UTF-8">`, viewport meta.
   - `<title>` matching the tutorial name.
   - Link to `../assets/styles.css` (one level up from the tutorial directory).
   - Tailwind CDN script.
   - Favicon link if applicable.

2. **Body**
   - Fixed left sidebar with an accordion table of contents (`<nav class="sidebar">`).
   - Main content area with a top nav bar containing:
     - Theme toggle button.
     - Back to home link.
     - Progress status controls (Start / Mark Complete / Reset).
   - Sections using semantic headings (`<section>`, `<h1>`, `<h2>`, `<h3>`).
   - Code blocks wrapped in:
     ```html
     <div class="code-block">
       <button class="copy-btn" ...>Copy</button>
       <pre><code class="language-...">...</code></pre>
     </div>
     ```
   - A capstone project with exactly 5 numbered phases.
   - A knowledge-check quiz (usually 8 multiple-choice questions).
   - Footer with `Open directly in any browser. No build step required.`

3. **Scripts**
   - Theme persistence in `localStorage` using key `tutorials-theme`.
   - Tutorial progress persistence using key `tutorial-{id}-status`.
   - Copy-to-clipboard handler for `.copy-btn`.
   - Quiz scoring/feedback handler.

### Tutorial Content Guidelines

- Keep explanations practical and include real-world examples.
- Use copyable, runnable code snippets.
- Avoid single-line code blocks longer than ~120 characters; wrap or use `pre` formatting.
- Each tutorial should feel like a complete mini-course.

## Landing Page (`index.html`) Conventions

- Tutorial cards are generated as plain HTML inside `#tutorial-grid`.
- Each card uses:
  - `data-id="{tutorial-id}"`
  - `data-category="{foundation|frontend|backend|devops|security}"`
  - `data-duration="{N} hrs"`
  - Sequential `#N` badge from `#1` to the current highest number.
- Category pills must use `category-{category}` class names; those colors are defined in `assets/styles.css`.
- Progress tracking relies on the `TUTORIALS` array in the page script; every new tutorial must be added there (including AI-track tutorials).
- Filter buttons must match the set of `data-category` values exactly. The AI / ML / LLM track uses category `ai` and sequential badge labels `AI-1`, `AI-2`, etc.

## Stylesheet (`assets/styles.css`) Conventions

- CSS variables for light and dark themes.
- Category color variables must exist in both `:root` (light) and `.dark` scopes:
  ```css
  :root {
    --frontend: #3b82f6;
    --backend: #10b981;
    --devops: #f59e0b;
    --foundation: #8b5cf6;
    --security: #ef4444;
    /* ... */
  }
  ```
- `.category-*` classes set `color: #ffffff` so pills are readable on colored backgrounds.
- Brand classes (`.brand-*`) are added for each tutorial when a unique brand accent is needed.

## Numbering & Sequencing

When adding a new tutorial:

1. Assign the next sequential number.
2. Add the card to `index.html` in the same numeric order.
3. Add the tutorial object to the `TUTORIALS` JavaScript array.
4. Update the hero text, badge, and `README.md` table to reflect the new total count.
5. Add a favicon under `assets/favicons/` and, if needed, an SVG under `assets/svg/`.

## Quality Checks

Before considering a change complete:

- Validate `index.html` parses without unclosed tags.
- Verify every tutorial card has a matching entry in the `TUTORIALS` array.
- Verify filter categories match card categories.
- Verify the new tutorial page returns HTTP 200 and its stylesheet loads.
- Run a quick check that no single-line code block exceeds ~200 characters.

## Common Commands

Serve the site locally for smoke tests:

```bash
python3 -m http.server 8000
```

Then open `http://localhost:8000`.

## Communication Notes

- Keep changes minimal and consistent with existing code style.
- Do not commit unless explicitly asked.
- Update `README.md` and `AGENTS.md` when structure or conventions change.
