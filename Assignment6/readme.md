# 1. Find if Path Exists in Graph

- Time Complexity - O(N) (worse case visit every node)
- Space Complexity - O(N) (Space used to create adjacency list)

Approach:

- Use edges to create an adjacent list (our graph)
- starting from source, add every adjacent node to our be_visited deque
- add visisted nodes into a set, to prevent cycles and unnecessary work

  - we'll return early if a node has already been visisted

- go through our deque, from the front, adding all new nodes into the back

  - we'll pop nodes from the deque after use

- check if each new node is destination, returning true if yes. If we go through every node, return false

# -------------------------------------------------------------------------------------------------

# 2. Longest Cycle in a Graph

- Time Complexity - O(N) (each node only visited once)
- Space Complexity - O(N) (extra space used to store both visited, and current path)

Approach:

- for each node, we will do DSF, either until the path ends, or we hit a cycle
- we can use a map to represent a path, in order to see if a node is in the cycle
  - value of map can store distance for easy calculation once cycle is found
- we keep a visited map outside of the node loop
  - no reason to revisit a node, as its either a cycle we seen (not bigger), or leads nowhere

# -------------------------------------------------------------------------------------------------

# 4. All Paths From Source to Target

- Time Complexity - O(N^M) N = number of nodes, M = avg number of edges per node
- Space Complexity - O(N^M) Represents all possible paths,

Explaination:

- since each edge represents a different path, it can grow exponentially since a path can branch 6 times, then in each of those new paths, it can branch another x amount of times...

Approach:

- We use recursive DSF but using backtracking to explore every option
- each edge in a for loop, represents a different path we can take
- for each possible path, we copy the current path (a list), passing the edge and the copy path as args
- We use a top down method of recursion, adding the numbers to each list as we go deeper, NOT while we return up

  - (since the numbers need to be added in order of being seen)

- if a path reaches node n-1, we then add that path to the result.
- Using a reference arg to the result, to be able to add it anywhere in the recursion stack

# -------------------------------------------------------------------------------------------------

# 5. Pow (x,n)

- Time Complexity - O(log N) (logarithmic, we save unnecessary work since 2^5 \* 2^5 == 2^10)
- Space Complexity - O(log N) (Stack space used since recursive implementation)

Approach:

- Recursive approach where we find pow(x, n / 2), since 2^5 \* 2^5 == 2^10

  - This lets us cut the down the amount of work in half each time
  - we also save pow(x, n / 2) into a var, saving the work for the 2nd time used

- If exponent is odd, we truncate the exponent division, but add an additional \* x when returning

  - truncate example: 13 // 2 = 6

- base cases:

  - exponent = 0: return 1
  - exponent = 1: return x

- handling negative exponents:

  - caculate the total, and at the end we use simply return 1/total, instead

- edge case:
  - If num == 0, and exp is negative, that would lead to 1/0, which is zero division, can handle accordingly
