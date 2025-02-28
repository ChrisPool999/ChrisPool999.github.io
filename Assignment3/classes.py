from __future__ import annotations
from collections import deque

class ListNode:
    next = None
    val = None

    def __init__(self, val):
        self.val = val

class LinkedList:
    head = None
    tail = None

    def add(self, node):
        if not self.head:
            self.head = self.tail = node
            return
        
        self.tail.next = node
        self.tail = node

class TreeNode:
    left = None
    right = None
    val = None

    def __init__(self, val):
        self.val = val

    def add(self, root: TreeNode, new_node: TreeNode):
        while True:
            goleft = new_node.val < root.val

            if goleft and not root.left:
                root.left = new_node
                return
            elif not goleft and not root.right:
                root.right = new_node
                return            

            if (goleft):
                root = root.left
            else:
                root = root.right
            
# for checking output
def DSF(root: ListNode) -> None:
    if not root:
        return
    
    left = DSF(root.left)
    print(root.val)
    right = DSF(root.right)

# for checking output
def BSF(root: ListNode) -> None:
    nodes = deque([root])
    
    while len(nodes):
        node = nodes[0]

        if not node:
            print("Null")
        else:
            nodes.append(node.left)
            nodes.append(node.right)
            print(node.val)

        nodes.popleft()