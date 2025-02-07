class LinkedList:
    class Node:
        def __init__(self, value, next = None):
            self.value = value
            self.next = next

    def __init__(self, node: Node):
        self.head = self.tail = node

    def add(self, node: Node):
        self.tail.next = node
        self.tail = node

    # helper function
    def remove_tail(self, prev: Node) -> Node:
        temp = self.tail 

        if self.tail:
            prev.next = None
            self.tail = prev

        return temp

    # helper function
    def remove_head(self) -> Node:
        result = self.head
        
        if not self.head or not self.head.next:
            self.head = None
        else:
            self.head = self.head.next

        return result

    def remove_nth_from_end(self, slow: Node, n: int) -> Node:
        if n <= 0: return None
        
        # keep fast node ahead by n
        fast = slow
        for i in range(n):
            if not fast: return None 
            fast = fast.next

        if not fast:
            return self.remove_head()

        # want to be left of nth node for easy removal
        while fast.next:
            fast = fast.next
            slow = slow.next

        if not slow.next.next:
            return self.remove_tail(slow)
        
        result = slow.next
        slow.next = slow.next.next        
        return result

    def print_list(self):
        output = ""       
        node = self.head

        while node:
            output += str(node.value) + " "
            node = node.next
       
        print(output)

def main():
    ll = LinkedList(LinkedList.Node(7))
    ll.add(LinkedList.Node(4))
    ll.add(LinkedList.Node(1))
    ll.add(LinkedList.Node(3))
    ll.add(LinkedList.Node(0))
    ll.add(LinkedList.Node(-2))
    ll.print_list()

    # remove from invalid n 
    ll.remove_nth_from_end(ll.head, -4)
    ll.remove_nth_from_end(ll.head, 0)
    ll.remove_nth_from_end(ll.head, 9999)
    ll.print_list()

    # remove from end
    ll.remove_nth_from_end(ll.head, 1)
    ll.remove_nth_from_end(ll.head, 1)
    ll.print_list()

    # remove from start
    ll.remove_nth_from_end(ll.head, 4)
    ll.print_list()   

    # remove from middle
    ll.remove_nth_from_end(ll.head, 2)
    ll.print_list()

    # try removing from empty list
    ll.remove_nth_from_end(ll.head, 1)
    ll.remove_nth_from_end(ll.head, 1)
    ll.remove_nth_from_end(ll.head, 1)
    ll.print_list()

if __name__ == "__main__":
    main()
