# tests/test_hw01.py

import heapq
import importlib.util
import pathlib

# Load garden_hoses.py from src/
ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("main", ROOT / "src" / "garden_hoses.py")
main = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(main)

min_cost_connect = main.min_cost_connect

# Reference implementation for comparison
def ref_cost(arr):
    if not arr or len(arr) == 1:
        return 0
    h = list(arr)
    heapq.heapify(h)
    total = 0
    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        s = a + b
        total += s
        heapq.heappush(h, s)
    return total

# --- normal tests (4) ---
def test_small_known_1():
    assert min_cost_connect([1, 2, 3, 4]) == 19

def test_small_known_2():
    assert min_cost_connect([5, 2, 4]) == 17  # ✅ Corrected expected value

def test_small_known_3():
    assert min_cost_connect([8, 4, 6, 12]) == 58

def test_small_known_4():
    assert min_cost_connect([20, 4, 8, 2]) == 54

# --- edge cases (3) ---
def test_empty():
    assert min_cost_connect([]) == 0

def test_single():
    assert min_cost_connect([7]) == 0

def test_all_ones():
    assert min_cost_connect([1, 1, 1, 1]) == 8

# --- more-complex (3) ---
def test_descending_many():
    arr = [10, 9, 8, 7, 6]
    assert min_cost_connect(arr) == ref_cost(arr)

def test_mixed_values():
    arr = [31, 12, 7, 18, 3, 25]
    assert min_cost_connect(arr) == ref_cost(arr)

def test_larger_specific():
    arr = [6, 5, 4, 3, 2, 7, 8, 9, 1]
    assert min_cost_connect(arr) == ref_cost(arr)