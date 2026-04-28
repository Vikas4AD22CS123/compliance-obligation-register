import requests
import time
import statistics

URL = "http://127.0.0.1:5000/query"

times = []

for i in range(50):
    start = time.time()

    res = requests.post(URL, json={"question": f"Explain tax rules for companies {i}?"})
    

    end = time.time()

    times.append((end - start) * 1000)  # ms

p50 = statistics.median(times)
p95 = sorted(times)[int(0.95 * len(times)) - 1]
p99 = sorted(times)[int(0.99 * len(times)) - 1]

print("p50:", round(p50, 2), "ms")
print("p95:", round(p95, 2), "ms")
print("p99:", round(p99, 2), "ms")