import requests
import time
import statistics

BASE_URL = "http://127.0.0.1:5000"

results = {}

def benchmark_endpoint(name, method, endpoint, payload=None):

    times = []

    print(f"\nTesting {name}...")

    for i in range(50):

        start = time.time()

        if method == "POST":
            requests.post(
                f"{BASE_URL}{endpoint}",
                json=payload
            )

        else:
            requests.get(
                f"{BASE_URL}{endpoint}"
            )

        end = time.time()

        response_time = (end - start) * 1000
        times.append(response_time)

        print(f"Request {i+1}: {round(response_time, 2)} ms")

    times.sort()

    p50 = round(statistics.median(times), 2)
    p95 = round(times[int(0.95 * len(times)) - 1], 2)
    p99 = round(times[int(0.99 * len(times)) - 1], 2)

    results[name] = {
        "p50_ms": p50,
        "p95_ms": p95,
        "p99_ms": p99
    }

benchmark_endpoint(
    "categorise",
    "POST",
    "/categorise",
    {"text": "Environmental safety rules"}
)

benchmark_endpoint(
    "query",
    "POST",
    "/query",
    {"question": "What are environmental rules?"}
)

benchmark_endpoint(
    "health",
    "GET",
    "/health"
)

print("\n===== FINAL PERFORMANCE REPORT =====\n")

for endpoint, metrics in results.items():

    print(f"{endpoint.upper()}")

    print(f"P50: {metrics['p50_ms']} ms")
    print(f"P95: {metrics['p95_ms']} ms")
    print(f"P99: {metrics['p99_ms']} ms")

    print("-" * 40)