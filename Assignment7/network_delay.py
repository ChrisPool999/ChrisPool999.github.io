import heapq

def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    if n <= 1: 
        return 0

    adjacency_list = [[] for _ in range(n + 1)]

    for u, v, w in times: 
        adjacency_list[u].append((w, v))

    to_visit = [(0, k)]
    seen = {}

    while to_visit:
        time, node = heapq.heappop(to_visit)
        if node in seen: 
            continue

        seen[node] = time

        # use O(log n) to get shortest option (this way we're always taking the shortest path to each node)
        for w, v in adjacency_list[node]: 
            heapq.heappush(to_visit, (time + w, v))

    return -1 if len(seen) != n else max(seen.values())

# size 1:
print(networkDelayTime([1, 2, 1], 1, 1)) # expected: 0

# size 0:
print(networkDelayTime([], 0, 0)) # expected: 0

# disconnect nodes
print(networkDelayTime([[1, 2, 1]], 2, 2)) # expected: -1

# basic
print(networkDelayTime([[1, 2, 1]], 2, 1)) # expected: 1
print(networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2)) # expected: 2

# multiple edges, different weights
print(networkDelayTime([[2, 1, 2], [3, 1, 6], [3, 2, 2], [4, 3, 3]], 4, 4)) # expected: 7

