# Python Fundamentals

A beginner-to-intermediate, single-page interactive tutorial covering Python programming from the basics through advanced concepts.

## What's Included

- **Single HTML file**: `index.html` — open directly in any modern browser.
- **Sleek responsive layout**: left sidebar navigation, right content area.
- **Light & Dark themes**: Light is the default; toggle via the top-right button.
- **Google Font**: Outfit.
- **Tailwind CSS**: styling with a custom design, no build step required.
- **Syntax highlighting**: Highlight.js for code snippets.
- **Copy-to-clipboard buttons** on all code blocks.
- **Interactive in-browser code playgrounds** where you can run Python-like snippets (using Brython or simulated output).
- **Interactive elements**:
  - Checkpoints with self-check questions
  - Quizzes with instant feedback
  - "Try it yourself" exercises
- **Next / Previous navigation** at the bottom of each section.
- **Capstone project**: A small interactive project built chapter by chapter.

## Topics Covered

### Basics
1. Introduction
2. What is Python?
3. Installing Python & Running Code
4. Variables and Data Types
5. Strings, Numbers, and Booleans
6. Operators
7. Conditionals
8. Loops
9. Functions
10. Lists and Tuples
11. Dictionaries and Sets
12. String Formatting
13. File Handling
14. Error Handling
15. Modules and Packages

### Intermediate / Advanced
16. List Comprehensions
17. Lambda Functions
18. Map, Filter, and Reduce
19. Object-Oriented Programming
20. Inheritance and Polymorphism
21. Iterators
22. Generators
23. Decorators
24. Context Managers
25. Virtual Environments
26. Using uv as a Package Manager (advanced)

### Capstone
27. Build a Small Project
28. Best Practices and Resources

## Capstone Project

By the end, students will build a real command-line **Smart Expense Tracker**. The tutorial walks through requirements and design first, then provides a complete single-file solution. A fully modular version is also included in the `expense_tracker/` folder, applying variables, functions, file handling, error handling, dictionaries, modules, and clean separation of concerns.

## How to Use

1. Open `python-basics/index.html` in any modern web browser.
2. Use the left sidebar to jump between topics.
3. Toggle light/dark mode using the moon/sun icon in the header.
4. Work through checkpoints and quizzes to test your understanding.
5. Copy code blocks and run them in your local Python environment for practice.

## Files

```
python-basics/
├── index.html              # The complete interactive tutorial
├── README.md               # This file
└── expense_tracker/        # Modular capstone project
    ├── main.py
    ├── storage.py
    ├── models.py
    ├── operations.py
    ├── reports.py
    └── README.md
```

## No Server Required

All resources (Tailwind, fonts, icons, syntax highlighter) are loaded via CDN. You can open the file directly from your file system.

## Customization

If you'd like to add more topics or change colors:
- Edit the `<style>` block in `index.html` for custom CSS overrides.
- Add new `<section>` elements following the existing pattern.

Happy teaching and learning!
