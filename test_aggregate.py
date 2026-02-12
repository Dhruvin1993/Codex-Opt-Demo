from slow_aggregate import top_products_by_revenue

def test_small():
    path = "tiny.csv"
    with open(path, "w", encoding="utf-8") as f:
        f.write("A,2,10.0\n")
        f.write("B,1,100.0\n")
        f.write("A,1,10.0\n")

    assert top_products_by_revenue(path, k=2) == [("B", 100.0), ("A", 30.0)]
