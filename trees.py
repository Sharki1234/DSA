class Tree:
    def __init__(self,root):
        self.value = root
        self.left = None
        self.right = None
intraversal = []


def inorder_t(root):#LRooR
    if root.left != None:
        inorder_t(root.left)
    print(root.value)
    if root.right != None:
        inorder_t(root.right)



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
            
def delete_leaf(root,value):
    if root.value == value and root.left == None and root.right == None:
        root.value = None
        return True
    elif value<root.value:
        return delete_leaf(root.left,value)
    elif value>root.value:
        return delete_leaf(root.right,value)
    return None
def delete_1c(root,value):
    if root.value == value:
        if root.left == None and root.right != None:
            root.value = root.right.value
            root.right.value = None
            return True
        elif root.right == None and root.left != None:
            root.value = root.left.value
            root.left.value = None
            return True
        else:
            return("has more or less than one child")
    elif root.value<value:
        return delete_1c(root.right,value)
    elif root.value>value:
        return delete_1c(root.left,value)
    else:
        return False
    

def replace_2(root):
    if root.left == None and root.right == None:
        root.value = None
        return
    else:
        if root.right!= None and root.left == None:
            other= root.right.value
            root.value = other
            replace_2(root.right)
        elif root.right== None and root.left != None:
            other= root.left.value
            root.value = other
            replace_2(root.left)
        else:
            inorder_s = inorder_successor(root.right)
            other = inorder_s.value
            root.value = other
            replace_2(inorder_s)
            
   
def inorder_successor(root):
    current = root
    while current.left!= None:
        current= current.left
    return current

def delete(root,value):
    if root is None:
       return None
    if root.value>value:
       root.left = delete(root.left,value)
    elif root.value<value:
        root.right = delete(root.right,value)
    else:
        if root.left == None and root.right == None:
            return None
        elif root.left is None:
            root.value = root.right.value
            return root.right
        elif root.right is None:
           root.value = root.left.value
           return root.left
        else:
            inorder_s = inorder_successor(root.right)
            root.value = inorder_s.value
            delete(root.right,inorder_s.value)
    return root
           
            
        

tree = Tree(17)
tree.left = Tree(14)
tree.right = Tree(19)
tree.left.left = Tree(12)
tree.left.right = Tree(15)
tree.right.right = Tree(20)
tree.right.left = Tree(18)
delete(tree,17)
inorder_t(tree)
#(inorder_successor(tree.left).value)
#print(inorder_successor(tree.right).value)













