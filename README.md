# Personal Knowledge Engine (PKE)

Personal Knowledge Engine is a backend service that collects web content, processes it 
asynchronously and builds a searchable knowledge base.

## Problem

Important articles, blog posts and resources are scattered across the web and difficult to 
organize or search later.

## Solution

PKE allows users to submit URLs which are processed in the background:

1. Fetch the webpage
2. Extract the main content
3. Store structured documents
4. Build a searchable knowledge base

## Architecture

Client → API → Redis Queue → Worker → PostgreSQL

## Stack

- Python
- FastAPI
- PostgreSQL
- Redis
- Docker
- SQLAlchemy
- Alembic
- pytest

## Project status

🚧 Early development (MVP in progress)
