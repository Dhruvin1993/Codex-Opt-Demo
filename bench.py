import time
from slow_aggregate import top_products_by_revenue

def bench(path: str = "data.csv", k: int = 10, runs: int = 3) -> None:
    t0 = time.perf_counter()
    out = None
    for _ in range(runs):
        out = top_products_by_revenue(path, k=k)
    t1 = time.perf_counter()
    print(f"Top[0]={out[0] if out else None}")
    print(f"Elapsed: {(t1 - t0):.3f}s for {runs} runs")

if __name__ == "__main__":
    bench()
