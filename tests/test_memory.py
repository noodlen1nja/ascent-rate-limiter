
from app.limiter.memory import InMemoryTokenBucket


def test_bucket_allows_requests_up_to_capacity():
    limiter = InMemoryTokenBucket(
        capacity=10,
        refill_rate=2,
    )

    results = [
        limiter.allow_request("client-1")
        for _ in range(10)
    ]

    assert all(results)


def test_bucket_rejects_when_empty():
    limiter = InMemoryTokenBucket(
        capacity=10,
        refill_rate=2,
    )

    for _ in range(10):
        assert limiter.allow_request("client-1")

    assert limiter.allow_request("client-1") is False


def test_clients_have_independent_quotas():
    limiter = InMemoryTokenBucket(
        capacity=2,
        refill_rate=1,
    )

    assert limiter.allow_request("alice")
    assert limiter.allow_request("alice")
    assert not limiter.allow_request("alice")

    assert limiter.allow_request("bob")
