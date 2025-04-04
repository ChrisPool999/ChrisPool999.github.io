# 2 Maximum Absolute Difference in BST

Time - O(N) - turn bst to array + loop through array comparing adjacent values
Space - O(N) - turn bst to array
Approach:

- BST is naturally sorted using DSF.
- turn to array for easier comparison
- compare adjacent nodes since, if sorted, adjacent nodes are closest in value

# 4 Binary Tree Maximum Path Sum

Time - O(N) - DSF
Space - O(N) - Stack space for recursive calls
Approach:

- DSF, checking every node
- path_sum = left_path + right_path + current node
- can only split in one direction, so return the max of left and right path as we go up
- if a path is negative, dont use the value, use 0 instead.
- Record best using pass by reference, checking each nodes path against the best

# 5 Lexicographical Numbers

Time - O(N) - Only generates correct numbers, 1 - N
Space - O(log_10 n) - Result array is not considered in space. log 10 is for recursion space
Approach:

- Use (n \* 10) + digit to append digits in O(1) time
- Use a recursive approach with a for loop to explore every path, then backtrack once we've gone over n
  - eg 10 -> 100 -> backtrack.. -> 11 -> 111 -> backtrack.. -> 12 -> 122
