# SQL &amp; Databases: From Basics to Advanced

A single-page interactive tutorial teaching SQL through PostgreSQL and a realistic e-commerce sample database.

## What's Included

- **Single HTML file**: `index.html` — open directly in any modern browser.
- **Sleek responsive layout**: left sidebar navigation, right content area.
- **Light & Dark themes**: Light default; toggle via the top-right button.
- **Google Font**: Outfit.
- **Tailwind CSS**: styling with a custom design, no build step required.
- **Syntax highlighting**: Highlight.js for SQL and bash snippets.
- **Copy-to-clipboard buttons** on all code blocks.
- **Interactive quizzes** with instant feedback.
- **Next / Previous navigation** at the bottom of each section.
- **SVG diagrams** showing relational structure and ERD.
- **Real-world analytics** on a sample `online_store` database.

## Topics Covered

1. Introduction
2. Why SQL?
3. Setting Up PostgreSQL
4. Sample Database: Online Store
5. Creating Tables (DDL)
6. CRUD Operations
7. SELECT Queries
8. Joins
9. Aggregation &amp; Grouping
10. Subqueries &amp; CTEs
11. Indexes &amp; Performance
12. Constraints &amp; Relationships
13. Transactions &amp; ACID
14. Views &amp; Functions
15. Advanced PostgreSQL (JSONB, full-text search, CASE)
16. Real-World Analytics
17. Cheat Sheet

## Sample Database

The tutorial builds an `online_store` database with:

- `customers`
- `categories`
- `products`
- `orders`
- `order_items`

Students run real queries for sales analytics, inventory checks, customer lifetime value, and monthly revenue trends.

## How to Use

1. Open `sql-databases/index.html` in any modern web browser.
2. Use the left sidebar to jump between topics.
3. Toggle light/dark mode using the moon/sun icon in the header.
4. Work through checkpoints and quizzes to test your understanding.
5. Copy SQL blocks and run them in a local or Docker PostgreSQL instance.

## Files

```
sql-databases/
├── index.html   # The complete interactive tutorial
└── README.md    # This file
```

## No Server Required

All resources (Tailwind, fonts, icons, syntax highlighter) are loaded via CDN. You can open the file directly from your file system.

## Prerequisites

- A running PostgreSQL instance (local, Docker, or cloud).
- Basic familiarity with the command line is helpful.
- The [Linux Command Line](../linux/) tutorial is a good companion.

## Customization

If you'd like to add more topics or change colors:
- Edit the `<style>` block in `index.html` for custom CSS overrides.
- Add new `<section>` elements following the existing pattern.

Happy teaching and learning!
