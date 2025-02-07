# 1 Two Sum

https://chrispool999.github.io/Assignment1/two_sum.py

Time - O(N) - must atleast pass over the full array to search for any combination, E.g the combination could be at the end
Space - O(N) - Auxilary space needed to store the numbers seen

Approach - The approach is just to use a hashmap to store any seen numbers. When passing through the array, we just check the map to see if
we've seen the compliment. The compliment just being the difference between the target and current number we're on in the loop.

# 2 Find First and Last Position of Element in Sorted Array

https://chrispool999.github.io/Assignment1/first_and_last.py

Time - O(log n) - we use binary search to split the array in half every interation
Space - O(1) - no extra space used

Approach - We use a variation of binary search were we can always find the first or last occurance of a number (depending on args given)
Then we can just that bin. search twice to find the start, and then the end

# 3

# 4 Remove Nth Node From End of List

https://chrispool999.github.io/Assignment1/remove_nth.py

Time - O(N) - must pass through the entire list if we want to remove the end
space - O(1) - No extra auxilary space used. We use a two pointer approach.

Approach - We use a two pointer approach with a fast and slow. We keep fast **n** elements ahead of slow.
We can then increment both fast and slow until fast is at the end.
Since slow is **n** elements behind fast, slow will be **n** elements away from the end
Then we can remove using conditional logic depending on what node we're removing

# 5
