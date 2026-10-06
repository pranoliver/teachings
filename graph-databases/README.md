# Graph Databases with Neo4j

A hands-on, self-contained interactive tutorial for learning graph databases using Neo4j.

## What you'll learn

- Why graph databases matter for connected data
- How to install and run Neo4j with Docker
- Cypher query language fundamentals
- Creating nodes, labels, properties, and relationships
- Pattern matching, filtering, and variable-length paths
- Aggregation and ordering
- Indexes and constraints for performance and integrity
- Connecting to Neo4j from Node.js
- Building a movie recommendation graph

## Structure

- `index.html` — Complete tutorial in a single file with sidebar navigation, dark mode, copyable code blocks, quizzes, and a capstone project.
- `README.md` — This file.

## How to use

Open `index.html` directly in any modern web browser. No local server, build step, or internet is required after the page loads.

## Topics covered

1. Introduction
2. Why Graph Databases?
3. Installing Neo4j
4. Cypher Basics
5. Creating Nodes
6. Relationships
7. Querying Patterns
8. Aggregations
9. Indexes & Constraints
10. Neo4j from Node.js
11. Capstone: Movie Network

## Capstone

The final project is a **Movie Network** built in Neo4j and queried from Node.js. It demonstrates:

- Modeling people and movies as nodes
- ACTED_IN and DIRECTED relationships
- Co-actor queries
- A recommendation engine based on shared actors

## Required tools

- Docker (recommended) or Neo4j Desktop / AuraDB
- Node.js and npm for the driver chapter
- Neo4j Browser to run Cypher queries

## Quick start

```bash
# Start Neo4j
docker run -d --name neo4j -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/password123 neo4j:latest

# Open Neo4j Browser
open http://localhost:7474
```

---

Part of the interactive teaching collection.
