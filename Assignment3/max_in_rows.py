from classes import TreeNode
from collections import deque

def add_child_nodes(row: deque, node: TreeNode) -> None:
    if node.left: 
        row.append(node.left)
    if node.right: 
        row.append(node.right)

def max_in_row(root: TreeNode) -> list[int]:
    if not root: return []      
    result = []
    row = deque([root])
    
    while len(row):
        row_max = row[0].val
        init_row_size = len(row)

        for _ in range(init_row_size):
            row_max = max(row_max, row[0].val)
            add_child_nodes(row, row[0])
            row.popleft()

        result.append(row_max)
    
    return result

# NORMAL
TEST_1 = TreeNode(4)
node = TreeNode(2)
TEST_1.add(TEST_1, node)
node = TreeNode(-2)
TEST_1.add(TEST_1, node)
node = TreeNode(0)
TEST_1.add(TEST_1, node)
node = TreeNode(-7)
TEST_1.add(TEST_1, node)
node = TreeNode(7)
TEST_1.add(TEST_1, node)
node = TreeNode(3)
TEST_1.add(TEST_1, node)
print(max_in_row(TEST_1))
print()

# ALL NEGATIVE
TEST_2 = TreeNode(0)
node = TreeNode(-3)
TEST_2.add(TEST_2, node)
node = TreeNode(-2)
TEST_2.add(TEST_2, node)
node = TreeNode(-5)
TEST_2.add(TEST_2, node)
node = TreeNode(-4)
TEST_2.add(TEST_2, node)
node = TreeNode(-1)
TEST_2.add(TEST_2, node)
node = TreeNode(-6)
TEST_2.add(TEST_2, node)
print()
print(max_in_row(TEST_2))

# NORMAL
TEST_3 = TreeNode(3)
node = TreeNode(1)
TEST_3.add(TEST_3, node)
node = TreeNode(2)
TEST_3.add(TEST_3, node)
print()
print(max_in_row(TEST_3))

# SIZE 0
TEST_4 = None
print()
print(max_in_row(TEST_4))


# SIZE 1
TEST_5 = TreeNode(3)
print()
print(max_in_row(TEST_5))