class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def inorder_traverse(self):
        if self.left:
            self.left.inorder_traverse()
        print(self.val, end=" ")
        if self.right:
            self.right.inorder_traverse()

    def preorder_traverse(self):
        print(self.val, end=" ")
        if self.left:
            self.left.preorder_traverse()
        if self.right:
            self.right.preorder_traverse()

    def postorder_traverse(self):
        if self.left:
            self.left.postorder_traverse()
        if self.right:
            self.right.postorder_traverse()
        print(self.val, end=" ")


#       1
#      / \
#     2   3
#    / \
#   4   5

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("inorder Traversal:")
root.inorder_traverse()  

print("\npreorder Traversal:")
root.preorder_traverse()  

print("\npostorder Traversal:")
root.postorder_traverse()  
