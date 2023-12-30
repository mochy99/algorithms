class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.value)
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        newNode = TreeNode(value)
        if not self.root:
            self.root = newNode
        else:
            if value < self.root:
                self.insert(self.left, newNode)
            else:
                self.insert(self.right, newNode)
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
print(bst.root.left)
