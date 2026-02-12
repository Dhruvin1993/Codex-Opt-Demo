import random

def gen(path: str = "data.csv", n: int = 200_000, products: int = 2000, seed: int = 7) -> None:
    random.seed(seed)
    with open(path, "w", encoding="utf-8") as f:
        for _ in range(n):
            pid = f"P{random.randint(1, products):04d}"
            qty = random.randint(1, 5)
            price = round(random.random() * 100, 2)
            f.write(f"{pid},{qty},{price}\n")

if __name__ == "__main__":
    gen()
    print("Wrote data.csv")
