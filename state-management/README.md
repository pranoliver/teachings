# State Management

A self-contained tutorial on managing state in modern React applications. Covers three industry-standard tools: Redux Toolkit, Zustand, and React Query (TanStack Query), plus real-world examples and a capstone dashboard project.

## What you'll learn

- When to use Redux Toolkit vs Zustand vs React Query
- Slices, reducers, and actions with Redux Toolkit
- Minimal stores and selectors with Zustand
- Caching, background refetching, and mutations with React Query
- Server state vs client state separation
- Real-world architecture decisions from Instagram, Vercel, Netflix, Stripe, and Linear

## Open the tutorial

Open `index.html` directly in any modern browser.

## Start the capstone project

```bash
npx create-vite@latest dashboard --template react-ts
cd dashboard
npm install @reduxjs/toolkit react-redux zustand @tanstack/react-query
npm run dev
```

Then visit `http://localhost:5173`.

## Covered topics

1. Introduction to state management
2. Why state management: local, global, and server state
3. Redux Toolkit for predictable global state
4. Zustand for lightweight stores
5. React Query for server state
6. Choosing the right tool for each state layer
7. Real-world systems and architecture
8. Capstone: analytics dashboard combining all three tools

## Capstone acceptance criteria

- Products are fetched with React Query and cached across components.
- Filters are stored in Zustand and update the product list instantly.
- Cart and wishlist are managed by Redux Toolkit with actions and selectors.
- Multiple providers are composed correctly in the React tree.
- Cart summary badge updates when items are added or removed.
- Wishlist toggle reflects state immediately without refetching products.

## Real-world examples

- Instagram (Redux Toolkit for feed and notification state)
- Vercel and Excalidraw (Zustand for lightweight UI state)
- Netflix and Stripe dashboards (React Query for server data)
- Linear (normalized local cache + lightweight global store)
- GitHub Copilot interface (combination of server caches and UI stores)

## Run the local server

```bash
python3 -m http.server 8090
```

Then visit `http://localhost:8090/state-management/index.html`.
