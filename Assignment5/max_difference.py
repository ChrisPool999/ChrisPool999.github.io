class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bst_to_arr(root: TreeNode, lst: list[int]) -> None:
    if not root: return
    
    bst_to_arr(root.left, lst)
    lst.append(root.val)
    bst_to_arr(root.right, lst)

def min_difference(root: TreeNode) -> int:
    lst = []
    bst_to_arr(root, lst)

    if len(lst) == 1:
        return None
    
    best = abs(lst[0] - lst[1])
    for i in range(1, len(lst) - 1):
        difference = abs(lst[i] - lst[i+1])
        best = min(best, difference)

    return best

# size 1
node = TreeNode(5)
node.left = TreeNode(3)
node.right = TreeNode(8)
assert min_difference(TreeNode(5)) == None

# check basic
node = TreeNode(5)
node.left = TreeNode(3)
node.right = TreeNode(8)
assert min_difference(node) == 2

# no right child
node1 = TreeNode(4)
node1.left = TreeNode(2)
assert min_difference(node1) == 2

# tree contains negatives
node2 = TreeNode(-8)
node2.left = TreeNode(-11)
node2.left.right = TreeNode(-12)
node2.left.left = TreeNode(-13)
node2.right = TreeNode(-5)
node2.right.right = TreeNode(7)
assert min_difference(node2) == 1

# result is from negatives
node3 = TreeNode(0)
node3.left = TreeNode(-7)
node3.left.left = TreeNode(-8)
node3.right = TreeNode(3)
assert min_difference(node3) == 1

# duplicates
node4 = TreeNode(1)
node4.left = TreeNode(1)
assert min_difference(node4) == 0