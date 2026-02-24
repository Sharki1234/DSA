class Tree:
    def __init__(self,root):
        self.value = root
        self.left = None
        self.right = None

def inorder_t(root):
    if root.left != None:
        inorder_t(root.left)
    print(root.value)
    if root.right != None:
        inorder_t(root.right)

tree = Tree(68)
tree.left = Tree(34)
tree.left.left = Tree(17)
tree.left.right = Tree(37)
tree.right = Tree(89)
tree.right.left = Tree(72)
tree.right.right = Tree(90)

inorder_t(tree)



