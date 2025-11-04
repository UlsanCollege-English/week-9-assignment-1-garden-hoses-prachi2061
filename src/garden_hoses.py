import heapq

def min_cost_connect(lengths):
    """
    Given a list of hose lengths, return the minimal total cost to connect all hoses into one.
    Joining two hoses costs the sum of their lengths.
    """
    if len(lengths) <= 1:
        return 0

    h = list(lengths)  # make a copy so original list isn't modified
    heapq.heapify(h)
    total = 0

    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        cost = a + b
        total += cost
        heapq.heappush(h, cost)

    return total