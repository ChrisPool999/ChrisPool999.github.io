K_largest
Time - O(N)
Space - (1)

Approach: The problem is solved with the algorithm quick select. Quick select is a partial sorting algorithm.
Using swaps, we can get one index, the pivot, to be in its correct sorted position. However, all values to the left/right of the pivot will be lower/higher. Instead of doing what quick sort does, and repeating both both sides, we just recursively do quick select on the partition where k is, leading to less work.

majority_eleme  nt
Time - O(N)
Space - O(1)

Approach: The idea is to partition the elements. We start by building the partition one element at a time, the first number being the "major" element. The second it's no longer the majority element, we delete the first partition and repeat. The idea is if there are 3 x's and 3 y's, that must mean that the majority element must appear more times in the 2nd partition since it doesn't appear more times in the first.
