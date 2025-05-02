def find(x, parents):
    if x != parents[x]:
        parents[x] = find(parents[x], parents)

    return parents[x]

def union(x, y, parents):
    root1 = find(x, parents)
    root2 = find(y, parents)

    if root1 != root2:
        parents[root2] = root1
        return True
    
    return False

def water_distribution(n: int, wells: list[int], pipes: list[list[int]]) -> int:
    costs = []

    # switch pipes from 1-indexed to 0-indexed
    for u, v, c in pipes: 
        costs.append((c, u-1, v-1))

    # house n acts as dummy node since houeses range from  0 - (n-1)
    for i, c in enumerate(wells): 
        costs.append((c, i, n))

    costs.sort()

    result = 0
    parents = list(range(n+1))
    for c, u, v in costs:
        if union(u, v, parents): 
            result += c

    return result

# basic
print(water_distribution(3, [1, 2, 2], [[1, 2, 1], [2, 3, 1]])) # expects: 3

# pipes more expensive than wells
print(water_distribution(3, [1, 1, 1], [[1, 2, 4], [2, 3, 4]])) # expects: 3

# wells more expensive than pipes
print(water_distribution(3, [10, 10, 10], [[1, 2, 4], [2, 3, 4]])) # expects: 18

# no pipes exist / all houses must rely on wells
print(water_distribution(3, [5, 5, 5], [])) # expects: 15