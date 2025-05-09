def find_order_helper(course: int, graph: list[list[int]], result: list[int], taken: list[int], depth: int = 0):
    if taken[course]:
        return True
    
    # cycle detection
    if depth > len(graph):
        return False
    
    for i in range(len(graph[course])):
        pre_req = graph[course][i]
        if not find_order_helper(pre_req, graph, result, taken, depth + 1):
            return False

    result.append(course)
    taken[course] = True
    return True 

def find_order(num_courses: int, pre_reqs: list[list[int]]) -> list[int]:
    graph = [[] for _ in range(num_courses)]
    for pair in pre_reqs:
        graph[pair[0]].append(pair[1])

    result = []
    taken = [False] * num_courses

    for i in range(num_courses):
        if (not find_order_helper(i, graph, result, taken)):
            return []
    
    return result

# BASIC / CAN FINISH
print(find_order(2, [[1, 0]])) # expects: [0, 1]
print(find_order(4, [[1, 0],[2, 0],[3, 1],[3, 2]])) # expects: [0, 1, 2, 3]

# CYCLE / CAN NOT FINISH
print(find_order(4, [[1, 0],[2, 3],[3, 1],[3, 2]])) # expects: []

# SIZE 1
print(find_order(0, [])) # expects: [0]

# NO PRE_REQ
print(find_order(3, [])) # expects: [0, 1, 2]
