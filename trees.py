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

def inorder_successor(root):
    if root.right == None and root.left == None:
        return root
    elif root.right != None:
        return inorder_successor(root.left)
    return(root.left)

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
        
        return None
    if root.value>value:
        root.left =  delete(root.left,value)
        
    elif root.value<value:
        root.right =  delete(root.right,value)
        
    else:
        if root.left == None and root.right == None:
             root.value = None
             
        if root.left == None :
            other = root.left
            root = None
            
            return other
            
        elif root.right and root.left == None:
            other = root.right
            root = None
           
            return other
        else:
            
            temp = inorder_successor(root.right)
            num = root.value
            root.value = temp.value
            temp.value = num
            root.right = delete(root.right,temp.value)
            
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
    
def replace(root):
    successor = inorder_successor(root.right)
    root.value = successor.value
    return root
def delete_try(root,value):
    if root.value == value:
        if root.left == None and root.right == None:
            root.value = None
            return
        elif root.left == None and root.right != None:
            root.value = root.right.value
            root.right.value = None
            return 
        elif root.right == None and root.left != None:
            root.value = root.left.value
            root.left.value = None
            return 
        else:
            replace(root)
    else:
        if root.value>value:
           return delete_try(root.left,value)
        elif root.value<value:
            return delete_try(root.right,value)
    return False
        

tree = Tree(17)
tree.left = Tree(14)
tree.right = Tree(19)
tree.left.left = Tree(12)
tree.left.right = Tree(15)
tree.right.right = Tree(20)
tree.right.left = Tree(18)
print(inorder_successor(tree.right).value)













