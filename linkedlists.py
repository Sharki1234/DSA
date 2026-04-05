class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

node1 = Node(1)
node2 = Node(1)
node3 = Node(2)
# node4 = Node(2)
# node5 = Node(3)
# node6 = Node(3)

node1.next = node2
node2.next = node3
# node3.next = node4
# node4.next = node5
# node5.next = node6

def traversal(node):
    print(node.value)
    if node.next:
        return traversal(node.next)
    return
    #O(n)

def lowest_value(node,value):
    if node.value<value:
            value = node.value
    if node.next:
            return lowest_value(node.next,value)
        
    print(value)#O(n)
    return
def delete(node,value):
    if node.next:
        if node.next.value == value:
            node.next = node.next.next
        else:
            delete(node.next,value)
    return False #O(n)

def insert(before,value):
    new = Node(value)
    new.next = before.next
    before.next = new#O(n)

def delete_repeat(node):
    dummy = node
    while node.next:
        if node.value == node.next.value:
            node.next = node.next.next
        else:
            node = node.next
    return traversal(dummy)
        
        
         

print(delete_repeat(node1))
traversal(node1)

