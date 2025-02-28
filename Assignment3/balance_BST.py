from classes import TreeNode
from classes import DSF
from classes import BSF

# helper
def bst_to_arr(root: TreeNode, arr: list[int]) -> list[int]:
    if not root: return

    bst_to_arr(root.left, arr)
    arr.append(root.val)
    bst_to_arr(root.right, arr)

# helper
def arr_to_bst(arr: list[int], start: int, end: int) -> TreeNode:
    # end is exclusive
    if start == end:
        return None

    mid = (start + end) // 2

    node = TreeNode(arr[mid])
    node.left = arr_to_bst(arr, start, mid)
    node.right = arr_to_bst(arr, mid + 1, end)

    return node

def balanceBST(root: TreeNode) -> TreeNode:
    arr = []
    bst_to_arr(root, arr)
    return arr_to_bst(arr, 0, len(arr))

# NORMAL CASE
TEST_1 = TreeNode(7)
node = TreeNode(6)
TEST_1.add(TEST_1, node)
node = TreeNode(5)
TEST_1.add(TEST_1, node)
node = TreeNode(4)
TEST_1.add(TEST_1, node)
TEST_1 = balanceBST(TEST_1)
BSF(TEST_1)
print()

# NORMAL CASE
TEST_2 = TreeNode(3)
node = TreeNode(2)
TEST_2.add(TEST_2, node)
node = TreeNode(4)  
TEST_2.add(TEST_2, node)
node = TreeNode(1)
TEST_2.add(TEST_2, node)
node = TreeNode(5)
TEST_2.add(TEST_2, node)
TEST_2 = balanceBST(TEST_2)
BSF(TEST_2)
print()

# CHECK ALREADY BALANCED
TEST_3 = TreeNode(3)
node = TreeNode(2)
TEST_3.add(TEST_3, node)
node = TreeNode(5)  
TEST_3.add(TEST_3, node)
node = TreeNode(1)
TEST_3.add(TEST_3, node)
node = TreeNode(4)
TEST_3.add(TEST_3, node)

TEST_3 = balanceBST(TEST_3)
BSF(TEST_3)
print()

# CHECK SIZE 1
TEST_4 = TreeNode(3)

TEST_4 = balanceBST(TEST_4)
BSF(TEST_4)
print()

# CHECK SIZE 0
TEST_5 = None

TEST_5 = balanceBST(TEST_5)
BSF(TEST_5)
print()
