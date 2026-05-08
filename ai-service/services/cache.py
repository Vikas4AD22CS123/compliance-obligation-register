import redis
import hashlib
import json

# Redis connection
r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True
)

# Cache counters
cache_hits = 0
cache_misses = 0


def generate_cache_key(question):
    return hashlib.sha256(question.encode()).hexdigest()


def get_cached_response(question):
    global cache_hits

    key = generate_cache_key(question)

    cached = r.get(key)

    if cached:
        cache_hits += 1
        return json.loads(cached)

    return None


def save_to_cache(question, data):
    global cache_misses

    key = generate_cache_key(question)

    r.setex(
        key,
        900,  # 15 minutes
        json.dumps(data)
    )

    cache_misses += 1