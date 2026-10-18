
import threading
import time
from dataclasses import dataclass


@dataclass
class Bucket:
    tokens: float
    last_refill: float


class InMemoryTokenBucket:
    def __init__(
        self,
        capacity: int = 10,
        refill_rate: float = 2.0,
    ):
        if capacity <= 0 or refill_rate <= 0:
            raise ValueError("Capacity and refill rate must be positive")

        self.capacity = capacity
        self.refill_rate = refill_rate
        self.buckets: dict[str, Bucket] = {}
        self.lock = threading.Lock()

    def allow_request(self, client_id: str) -> bool:
        with self.lock:
            now = time.monotonic()

            if client_id not in self.buckets:
                self.buckets[client_id] = Bucket(
                    tokens=float(self.capacity),
                    last_refill=now,
                )

            bucket = self.buckets[client_id]

            elapsed = max(0.0, now - bucket.last_refill)

            bucket.tokens = min(
                self.capacity,
                bucket.tokens + elapsed * self.refill_rate,
            )
            bucket.last_refill = now

            if bucket.tokens >= 1:
                bucket.tokens -= 1
                return True

            return False
