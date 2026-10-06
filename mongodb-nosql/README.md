# MongoDB & NoSQL

A self-contained, hands-on tutorial covering MongoDB installation, document modeling, CRUD operations, aggregation pipelines, indexing, replica sets, and sharding.

## What you'll build

A food delivery analytics backend with three collections:

- `restaurants` — cuisine, location, rating, embedded menu
- `orders` — references to restaurants and users, embedded item snapshots
- `customers` — profile and order history references

You'll run real queries that report revenue, popular cuisines, and daily order trends.

## Open the tutorial

Open `index.html` directly in any modern browser.

## Install MongoDB first

### Docker (recommended)

```bash
docker run -d --name mongodb \
  -p 27017:27017 \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=secret \
  mongo:7
```

### macOS Homebrew

```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

### MongoDB Atlas

Create a free M0 cluster at [mongodb.com/atlas](https://mongodb.com/atlas), whitelist your IP, and copy the connection string.

## Connect

```bash
mongosh "mongodb://admin:secret@localhost:27017"
use food_delivery
```

## Covered topics

1. Introduction to NoSQL and MongoDB
2. Install and connect
3. Documents and BSON
4. CRUD in the shell
5. Document modeling: embed vs reference
6. Aggregation pipeline
7. Indexing strategies
8. Replica sets and sharding
9. Capstone: food delivery analytics

## Sample data included

The tutorial includes ready-to-copy `insertOne`, `insertMany`, and aggregation starter queries. Paste them into `mongosh` and run them immediately.

## Real-world systems mentioned

- Netflix content catalog and personalization metadata
- UPS package tracking and delivery routes
- Forbes content management system
- Food delivery apps for real-time order and menu data

## Run the local server

```bash
python3 -m http.server 8084
```

Then visit `http://localhost:8084/mongodb-nosql/index.html`.
