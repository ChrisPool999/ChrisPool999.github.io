from collections import deque

def validPath(n: int, edges: list[list[int]], source: int, destination: int) -> bool:
    graph = [[] for _ in range(n + 1)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u) 

    seen = set()
    to_visit = deque([source])

    while to_visit:
        node = to_visit.popleft()

        if node == destination:
            return True

        if node in seen:
            continue
        seen.add(node)

        for adjacent in graph[node]:
            if adjacent not in seen:
                to_visit.append(adjacent)

    return False

s = "ab#c"
t = "ad#c"

exit()

# Basic tests
print(validPath(3, [[0,1],[1,2],[2,0]], 0, 2)) # expects True
print(validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5)) # expects False

# test n = size 1
print(validPath(1, [[0,1]], 0, 1)) # expects True
print(validPath(1, [[0,1]], 0, 3)) # expects False

# test edges = size 0
print(validPath(1, [], 0, 3)) # expects False
print(validPath(1, [], 0, 0)) # expects True

# test source = destination
print(validPath(1, [], 0, 0)) # expects True
print(validPath(1, [[0,1]], 0, 0)) # expects True

# destination has no edges
print(validPath(6, [[0,1],[0,2],[3,1],[3,4],[4,3]], 0, 5)) # expects False

# source has no edges
print(validPath(6, [[2,1],[4,2],[3,5],[5,4],[4,3]], 0, 5)) # expects False