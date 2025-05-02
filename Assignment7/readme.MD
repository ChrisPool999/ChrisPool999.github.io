1. Course Schedule

Time - O(N) We check each pre_req, caching the value to stop any duplicate work.
Space - O(N) We use multiple data structures, and recursive space, but never need more than the amount of pre_reqs in a single one

Approach:

- The only instance you couldn't finish all courses is if a course needed to take itself (a cycle)
- For each pre_req, we go through the chain of pre_req's needed (EXAMPLE: Class 3 --> Needs class 2 --> needs class 1 --> no pre_req's)
  - If a pre_req has no other pre_req's, that means all courses in the path are completable
  - If a pre_req needs a course that has appeared in the path, it's impossible to take. Because both courses need each other.

Code:

- To detect cycles, we keep maintain a path. We add nodes visited at the start of the function, and delete at the end (after exploring other pre_reqs)
 
- we use a DSF recursive algorithm, exploring until we hit a node we already visited (cycle), or recursion ends (course has no pre_reqs)
- all courses in the path that has ended, are marked as completable

- we use this completed DS as a cache to store any nodes already checked and verified, stopping any duplicate work
- we run this checkCycle function on every pre_req given

- No cycles found = completable
- Cycle? = not completable

- NOTE: disconnected nodes don't matter because they must start from somewhere, indicating either a cycle or a viable path

# _______________________________________________________________________________________________________________________________________________
2. Network Delay Time

Time - O(N * log N)
Space - O(N)

Approach:
- We use dijkstra's algorithm to search for paths from source to target node. 
- We use a heap implementation because it's more optimal than scanning linearly throughout every vertices ( O(log n) vs O(N) )
  - use a heap to store the possible exploration paths
  - use a min heap, because we always want to explore the path with the shortest path next.
  - This is a greedy style approach, where it means the first time we visit a node, it will always be the fastest path to that node.
  - removes alot of duplicate work and unnessary checks.
  - only need to go to each node once. 

# ________________________________________________________________________________________________________________________________________________
3. Optimize Water Distribution in a Village

Time - O( (N+E) log (N+E) )
Space - O(N+E)

Approach:
- Represent wells as edges from a dummy node to each house (cost = well cost)
- Add all edges (pipes + dummy node edges), sort by cost
- Use Union-Find to connect components:
    - Only add an edge if it connects two separate components 
    - This ensures no cycles and prioritizes cheaper connections 

#
________________________________________________________________________________________________________________________________________________