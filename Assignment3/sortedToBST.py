from classes import ListNode
from classes import TreeNode
from classes import LinkedList
from classes import BSF

def get_mid_node(head: ListNode, end: ListNode = None) -> ListNode:
    if not head:
        return None

    # fast = head.next guarentees us middle will be lower if even size
    fast = head.next
    slow = head

    while fast != end and fast.next != end:
        fast = fast.next.next
        slow = slow.next

    return slow

def list_to_bst(start: ListNode, end: ListNode = None) -> TreeNode:
    # end is exclusive
    if start == end:
        return None

    mid = get_mid_node(start, end)

    node = TreeNode(mid.val)
    node.left = list_to_bst(start, mid)
    node.right = list_to_bst(mid.next, end)
    
    return node

# NORMAL
TEST_1 = LinkedList()
TEST_1.add(ListNode(-10))
TEST_1.add(ListNode(-3))
TEST_1.add(ListNode(0))
TEST_1.add(ListNode(5))
TEST_1.add(ListNode(9))
BST = list_to_bst(TEST_1.head)
BSF(BST)
print("")

# NEGATIVE ASCENDING
TEST_2 = LinkedList()
TEST_2.add(ListNode(-100))
TEST_2.add(ListNode(-50))
TEST_2.add(ListNode(-30))
TEST_2.add(ListNode(-15))
TEST_2.add(ListNode(-9))
BST = list_to_bst(TEST_2.head)
BSF(BST)
print("")

# POSITIVE ASCENDING
TEST_3 = LinkedList()
TEST_3.add(ListNode(9))
TEST_3.add(ListNode(20))
TEST_3.add(ListNode(40))
TEST_3.add(ListNode(90))
TEST_3.add(ListNode(100))
BST = list_to_bst(TEST_3.head)
BSF(BST)
print("")

# SIZE 1
TEST_4 = LinkedList()
TEST_4.add(ListNode(0))
BST = list_to_bst(TEST_4.head)
BSF(BST)

# SIZE 0
TEST_5 = LinkedList()
BST = list_to_bst(TEST_5.head)
BSF(BST)
