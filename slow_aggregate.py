from __future__ import annotations

def top_products_by_revenue(csv_path: str, k: int = 10) -> list[tuple[str, float]]:
    """
    CSV rows: product_id, qty(int), price(float)
    Returns top-k (product_id, revenue) sorted desc.

    Intentionally slow baseline:
    - reads entire file
    - builds rows list
    - for each product, scans all rows again (O(n * unique_products))
    """
    with open(csv_path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f.read().splitlines() if ln.strip()]

    rows: list[tuple[str, int, float]] = []
    for ln in lines:
        pid, qty, price = ln.split(",")
        rows.append((pid, int(qty), float(price)))

    product_ids = sorted({pid for pid, _, _ in rows})

    totals: list[tuple[str, float]] = []
    for pid in product_ids:
        rev = 0.0
        for rpid, qty, price in rows:
            if rpid == pid:
                rev += qty * price
        totals.append((pid, rev))

    totals.sort(key=lambda x: x[1], reverse=True)
    return totals[:k]
