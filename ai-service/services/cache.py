import hashlib
import time

cache_store = {}
cache_hits = 0
cache_misses = 0

def get_cache_key(text):
    return hashlib.sha256(text.encode()).hexdigest()

def get_from_cache(key):
    global cache_hits, cache_misses

    if key in cache_store:
        data, expiry = cache_store[key]

        if time.time() < expiry:
            cache_hits += 1
            print("CACHE HIT")   # debug
            return data
        else:
            del cache_store[key]

    cache_misses += 1
    print("CACHE MISS")   # debug
    return None

def set_cache(key, value):
    expiry_time = time.time() + 900
    cache_store[key] = (value, expiry_time)