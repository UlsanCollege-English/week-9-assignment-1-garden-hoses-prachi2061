[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/_bJjxmyt)
# HW01 — Garden Hoses: Minimal Join Cost

**Story intro (new theme):**  
You have many short **garden hoses**. Each join costs the **sum** of the two hose lengths. You want **one long hose** with **minimal total cost**.

**Technical description**  
- **Input:** a list of positive integers `lengths` (hose lengths).  
- **Output:** an integer: minimal total cost to join all hoses into one.  
- **Rules:**  
  - If `lengths` has 0 or 1 item, the cost is `0`.  
  - All lengths are positive integers.  
- **Expected complexity:** **Time** `O(n log n)` using a **min-heap**; **Space** `O(n)`.

---

## 8 Steps scaffold (ESL)
**Steps 1–5 (explicit)**
1. **Read & Understand:** We join two smallest hoses each time. Why?  
2. **Re-phrase:** Keep taking the two **shortest**, add their sum to the **total**, push back the sum, repeat.  
3. **Inputs/Outputs/Vars:** Input list, output cost, vars: `heap`, `total`.  
4. **Break down:** While heap size > 1: pop two, add, push sum.  
5. **Pseudocode:**
~~~
if n <= 1: return 0
heapify(lengths)
total = 0
while heap has 2+ items:
a = heappop()
b = heappop()
s = a + b
total += s
heappush(s)
return total
~~~

**Steps 6–8 (hints)**

6. **Code:** Use `heapq.heapify`, `heappop`, `heappush`.  
7. **Debug:** Print heap after each join for a small input.  
8. **Optimize:** This is already optimal with a min-heap (Huffman-like).

---

## Hints (not spoilers)
- Use `heapq.heapify` once at the start.  
- Pop **two** items each loop.  
- If the list is empty or size 1, return `0`.

---

## How to run tests
python -m pytest -q

markdown
Copy code

---

## FAQ
- **Q:** Python version? **A:** 3.10 or 3.11.  
- **Q:** Do I read from stdin? **A:** No. Implement a function that tests will call.  
- **Q:** What Big-O is expected? **A:** `O(n log n)` time, `O(n)` space.  
- **Q:** What if input is empty or length 1? **A:** Return `0`.  
- **Q:** Can I sort each time? **A:** No, that is too slow. Use a heap.  
- **Q:** How do I read pytest failures? **A:** Look for the **expected** vs **actual** line in the assertion.  
- **Q:** Grading? **A:** We run the tests. Passing tests earn full credit.
