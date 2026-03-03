class Tree:
    def __init__(self,root):
        self.value = root
        self.left = None
        self.right = None
    

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

tree = Tree(17)
tree.left = Tree(14)
tree.right = Tree(19)
tree.left.left = Tree(12)
tree.left.right = Tree(15)
tree.right.right = Tree(20)
tree.right.left = Tree(18)
insert(tree,7)
inorder_t(tree)
print(search(tree,15))
print(search(tree,23))











