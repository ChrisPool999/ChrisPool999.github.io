#1 **Convert Sorted List to Binary Search Tree**

**Time** - O(N log n) - log n levels. N work each time.

**Space** - O(log n) - Stack space for the number of maximum recursion calls

**Approach**:

- The middle of the range of sorted values should be the root node since it has equal elements to the left and right
- Fast and slow pointer are used for finding the middle of a list. Simple as moving the fast pointer 2x as fast.
- We use a divide and conqueror approach where we can pass array ranges as args  
   to break the problem down into subproblems, recursively solving it.

- EXAMPLE:
- root = middle
- root.left = recursion call but range = (start, mid)
- root.right = recursion call but range = (mid + 1, end)

---

#2 **Construct Binary Tree from Preorder and Inorder Traversal**

**Time** - O(N) - Need to go through the entire array to construct a node for each index
**Space** - O(N) - Extra space needed for map to get inorder index positions in O(1) time

**Approach** -

- In order indexes tells us which direction a node is in relation to another node
- We use a map so we can check this in O(1) time

- We build the tree using preorder traversal.

- The only problem with preorder is we dont know when a node has null children
- in order will tell us this. I.E if the next node in preorder, is NOT left of the last node (using inorder), then the left child of the last node would be null

---

#3 **Binary Tree Maximum Path Sum**

**Time** - O(N) - Just need to traverse the entire tree
**Space** - O(N) - Stack space for recursive calls. Worse cast, max depth could be size N if the tree only splits in a single direction.

**Approach**

- path sum = left child path + root.val + right child path
- We can use in order traversal and return the path sum as we go up, adding the values of the nodes we visit.
- Since the max path can appear anywhere (due to negative values), we must check every node.
- I used a reference in the arguments, so that we can keep track of both the max value, and the current path value as we traverse.

- Since we can only take one path when we return, we want to take the highest path between left and right. (if we took more than one going up, it's no longer a single path, but one that branches into 3 directions)

---

#4 **Find largest value in each Tree row**

**Time** - O(N) - Traverse entire tree in BSF
**Space** - (N) - Extra space used for deque

**Approach**

- I used a pretty standard BSF algorithm with a deque.
- Basically where you start with a tree row all placed inside a deque (typically starting as just the root) Going from the deque from front to back, adding each nodes children to the back of the deque, and after removing that parent node.
- This gives you left to right, and top to bottom traversal, AKA BSF

- I made some slight varations such as being able to tell when new rows start by saving the intial row size each time.
- After completing a row, I would add the maximum value I found to the result, and then reset it for the next row.

---

#5 **Balance a Binary Search Tree**

**Time** O(N) - Need to create every node
**Space** O(N) - We use extra space as we convert the BST to an array

**Approach**:
I reused the same logic on problem #1, by converting the BST to a sorted array, then back to a BST

For converting the BST to an array, I used inorder traversal.

Instead of actually reusing the code, I used an array implementation became you can find the middle in O(1), reducing the time complexity to O(N).
