def longestCycle(edges: list[int]) -> int:
    visited = [False] * len(edges)
    result = -1

    for node in range(len(edges)):
        if node in visited:
            continue

        curr = node
        path = {}
        distance = 0

        while curr != -1:
            if curr in path:  
                result = max(result,  distance - path[curr])
                break
            if visited[curr]:
                break

            visited[curr] = True
            path[curr] = distance
            curr = edges[curr]
            distance += 1

    return result

# test basic
print(longestCycle([3,3,4,2,3])) # expects: 3  (3, 4, 2)
print(longestCycle([2,-1,3,1])) # expects: -1
print(longestCycle([1, 2, 0])) # expects: 3   (1, 2, 0)

# test no cycle
print(longestCycle([2, -1, -1])) # expects: -1

# test larger input
print(longestCycle([1, 2, 3, 4, 5, 6, 7, 3])) # expects: 5  (3, 4, 5, 6, 7)

# test no edges
print(longestCycle([-1])) # expects: -1
