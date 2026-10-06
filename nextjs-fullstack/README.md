# Next.js Full-Stack

A self-contained tutorial on building production-ready React apps with Next.js: routing, SSR, SSG, ISR, data fetching, API routes, dynamic routes, and deployment.

## What you'll build

A full-stack e-commerce store called **Modern Mart** with:

- **Homepage** with hero section and featured products
- **Product listing page** at `/products` with category filtering and price sorting
- **Dynamic product detail pages** at `/products/[id]`
- **Static generation** for the top 20 products plus ISR fallback
- **Client-side cart** with localStorage persistence, quantity updates, and remove item
- **Checkout page** with Zod validation and server-side total verification
- **Order API route** at `/api/orders` that validates stock, guards against tampering, and stores orders
- **Search page** at `/search?q=...` using query parameters
- **Shared layout** with responsive navigation, cart count badge, and footer
- **Deployment to Vercel** with preview URLs and environment variables

## Open the tutorial

Open `index.html` directly in any modern browser.

## Start the project

```bash
npx create-next-app@latest my-shop
# Select TypeScript, ESLint, Tailwind CSS, App Router

cd my-shop
npm install zod
npm run dev
```

Then visit `http://localhost:3000`.

## Project structure

```
app/
├── layout.tsx              # root layout with cart provider
├── page.tsx                # homepage
├── products/
│   ├── page.tsx            # product listing
│   └── [id]/
│       └── page.tsx        # product detail
├── cart/
│   └── page.tsx            # cart page
├── checkout/
│   └── page.tsx            # checkout page
├── search/
│   └── page.tsx            # search results
├── api/
│   ├── products/
│   │   └── route.ts        # GET /api/products
│   └── orders/
│       └── route.ts        # POST /api/orders
components/
├── Navbar.tsx              # navigation + cart count
├── ProductCard.tsx         # reusable card
├── CartProvider.tsx        # context + localStorage
├── AddToCartButton.tsx     # client interactivity
└── CheckoutForm.tsx        # form + validation
lib/
├── products.ts             # product data helpers
└── validation.ts           # Zod schemas
```

## Covered topics

1. Introduction to Next.js
2. Setup and first app
3. File-based routing with the App Router
4. SSR, SSG, and ISR rendering modes
5. Server and Client Components
6. API routes with Route Handlers
7. Dynamic routes and `generateStaticParams`
8. Deployment to Vercel
9. Capstone: full e-commerce store

## Capstone acceptance criteria

- Homepage loads in under 2 seconds and shows at least 4 featured products.
- Product listing supports category filtering and price sorting.
- Dynamic product pages use `generateStaticParams` for the top 20 products and ISR for the rest.
- Cart persists across page reloads using localStorage.
- Checkout validates customer data and rejects mismatched totals.
- Order API stores orders server-side and returns a unique order ID.
- Search page reads query parameters and filters results.
- App is deployed to Vercel with a live URL.

## Real-world examples

- TikTok marketing pages
- Netflix consumer surfaces
- GitHub Copilot docs
- Stripe documentation
- Hulu, Twitch, Nike storefronts

## Run the local server

```bash
python3 -m http.server 8084
```

Then visit `http://localhost:8084/nextjs-fullstack/index.html`.
