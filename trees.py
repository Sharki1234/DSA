class Tree:
    def __init__(self,root):
        self.value = root
        self.left = None
        self.right = None
intraversal = []


def inorder_t(root):#LRooR
    if root.left != None:
        inorder_t(root.left)
    (root.value)
    if root.right != None:
        inorder_t(root.right)

def inorder_successor(root,node):
    successor = None
    if node.right :
        curr = node.right
        while curr.left != None:
            curr = curr.left
        return curr.value
    while root:
        if node.value<root.value:
            successor = root
            root = root.left
        elif node.value>root.value:
            root = root.right
        else:
            break
    return successor.value

def insert(root,num):
    if root == None:
        return Tree(num)
    if root.value>num:
        root.left = insert(root.left,num)
    if root.value<num:
        root.right = insert(root.right,num)
    return root

def search(root,num):
    if root.value == num:
        return root.value
    elif root.value>num and root.left != None:
        return search(root.left,num)
    elif root.value<num and root.right != None:
        return search(root.right,num)
    else:
        return False
def minimum_value(root):
    if root.left != None:
        return minimum_value(root.left)
    return(root.value)
def maximum_value(root):
    if root.right != None:
        return minimum_value(root.right)
    return(root.value)
def leaf_sum(root):
    if root.left == None and root.right == None:
        return(root.value)
    return(leaf_sum(root.left)+leaf_sum(root.right))
def even_numbers(root):
    if root.left != None:
        even_numbers(root.left)
    if root.value%2 == 0:
        print(root.value)
    if root.right != None:
        even_numbers(root.right)
def delete(root,value):
    if root == None:
        print("1" )
        return None
    if root.value>value:
        root.left =  delete(root.left,value)
        print("2")
    elif root.value<value:
        root.right =  delete(root.right,value)
        print("3")
    else:
        # if root.left == None and root.right == None:
        #     root.value = None
        #     print("4")
        if root.left and root.right == None:
            other = root.left
            root = None
            print("5")
            return other
            
        elif root.right and root.left == None:
            other = root.right
            root = None
            print("6")
            return other
        else:
            
            temp = inorder_successor(root)
            print(temp.value,"temp")
            num = root.value
            root.value = temp.value
            temp.value = num
            root.right = delete(root.right,temp.value)
            print("7")
           

    


tree = Tree(17)
tree.left = Tree(14)
tree.right = Tree(19)
tree.left.left = Tree(12)
tree.left.right = Tree(15)
tree.right.right = Tree(20)
tree.right.left = Tree(18)
print(inorder_successor(tree,tree))














