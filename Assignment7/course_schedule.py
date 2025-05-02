def canFinish(num_courses: int, pre_reqs: list[list[int]]) -> bool:
    adjacency_list = [[] for _ in range(num_courses)]
    for course, req in pre_reqs:
        adjacency_list[course].append(req)

    checked = set()
    path = set()

    for course, req in pre_reqs:
        if has_cycle(req, path, checked, adjacency_list):
            return False

    return True

def has_cycle(curr: int, path: set[int], checked: set[int], adjacency_list: list[list[int]]) -> bool:
    if curr in path:
        return True

    if curr in checked:
        return False

    path.add(curr)

    for req in adjacency_list[curr]:
        # will always return all the way up to root
        if has_cycle(req, path, checked, adjacency_list):
            return True

    # remove when backtracking   
    path.remove(curr)

    checked.add(curr)
    return False

# no cycle
print(canFinish(2, [[1, 0]])) # expected: True

# cycle
print(canFinish(2, [[1, 0], [0, 1]])) # expected: False

# no pre_reqs
print(canFinish(1, [])) # expected: True
print(canFinish(100, [])) # expected: True

# disconnected
print(canFinish(4, [[1, 0], [2, 3]])) # expected: True
