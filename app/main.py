
from fastapi import FastAPI, HTTPException, Request

from app.limiter.memory import InMemoryTokenBucket


app = FastAPI(
    title="Distributed Rate Limiter",
    version="0.1.0",
)

limiter = InMemoryTokenBucket(
    capacity=10,
    refill_rate=2.0,
)


@app.get("/")
async def root():
    return {"message": "FastAPI Rate Limiter"}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/limited")
async def limited(request: Request):
    client_id = request.client.host if request.client else "unknown"

    if not limiter.allow_request(client_id):
        raise HTTPException(
            status_code=429,
            detail="Rate limit exceeded",
            headers={"Retry-After": "1"},
        )

    return {"message": "Request allowed"}
