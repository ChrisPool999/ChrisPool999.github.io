# 1. K most frequent Element

Time - O(N)
Space - O(N)

Approach:

- We use bucket Sort.
- the index of an array will represent the values that occur that many times
- eg index 1, holds all values that appear once, index 10 holds all values occuring 10 times

- Steps:
- get a count of all the numbers using a hashmap
- loop through hashmap and put all values into the bucket array
- going from the highest bucket to lowest (by occurance), take every value until we've reached k

# 2. Find K closest elements

Time - O(N - K)
Space - O(1) - if array is part of output, typically isn't counted as auxiliary space

Approach:

- Find the closest element element possible, if duplicates, use last occurance
- Use two pointer approach to compare which is closer in value, left index or right index, expanding outwards from middle (the closest element)
- expand until we have a range of size k
- reconstruct array using the range, which means it will also be sorted

# 3. K Largest Elements of a Max Heap

Time - O(K log K) - We use a subheap which we call peek() K times. Subheap max size = (k \* 2) because we can have 2 children per node
Space - O(K) - We use auxiliary for the sub heap. We also use auxiliary space to map values to indexes.

Approach:

- Utilize the fact that all subnodes are <= parent nodes
- Use 2i + 1 and 2i + 2 to determine child indexes from parent indexes in our heaps

- Use a max sub-heap to find the max value of possible children nodes
- pop the max children node, and add its children to the sub-heap
- we're only taking the max value, and adding children if its parent's value was used

# 4. Shortest Subarray with Sum at least K

Time - O(N) - One pass
Space - O(N) - Deque implementation used to store monotonic increasing prefixes

Approach:

- Pass through the array, maintaining a sum of all numbers passed by
- We want find the optimal index for the start index of the subarray (the ranges)
- By using monotonic increasing, we ensure the smallest sums are at the begginning, and still index ordered

- For each index:

  - check if sum > k

  - Check the front to see if we can make a sum of K with removing the prefix (handles both negative numbers, and finding shorter subarray's)

    - If yes, can remove from deque. Because since the right index is only growing, this is the smallest the subarray will ever get with this prefix index

  - ensure the deque stays monotonic increasing, delete all elements at the end lower than the current sum
    - only unoptimal values are removed, thus not skipping any correct result
    - we can remove prefix values that are higher, because they occur prior to current.
      - its optimal to remove because the sum is larger, we want to subtrack the smallest prefix sum possible as long as the index is also later, which the monotonic increasing guarentees.

# 5. Kth Smallest Prime Fraction

Time - O(N^2)
Space - O(N^2)

Approach:

- Nested loop to get all possible fractions
- sort
- return fractions[k-1]
