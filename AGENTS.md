## How to run
- Install deps: `pip install -r requirements.txt`
- Tests: `pytest -q`
- Generate benchmark data: `python generate_data.py`
- Benchmark: `python bench.py`

## Goal
Optimize `top_products_by_revenue` in `slow_aggregate.py` for speed and memory without changing behavior.
