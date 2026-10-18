# FastAPI Distributed Rate Limiter

A high-performance, concurrency-safe API rate limiter built using **FastAPI, Python, and Redis**.

This project implements the **token bucket algorithm** to control API request rates and prevent clients from exceeding configured quotas.

## Features

- In-memory token bucket with concurrency protection
- Distributed rate limiting using Redis and atomic Lua scripts
- Configurable request capacity and token refill rate
- HTTP 429 responses when rate limits are exceeded
- Explicit Redis failure handling policy
- Automated concurrency and correctness tests
- Reproducible load tests measuring throughput and p95 latency
- Docker-based local development

## Tech Stack

Python · FastAPI · Redis · Lua · Pytest · Docker

## Project Goals

1. Implement a correct token bucket algorithm.
2. Prevent quota violations under concurrent requests.
3. Support distributed rate limiting across multiple API workers.
4. Document system behavior during Redis outages.
5. Benchmark performance and explain architectural trade-offs.