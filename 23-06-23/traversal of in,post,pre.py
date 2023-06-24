class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val=key
def printInorder(root):
    if root:
        #first recur on left child
        printInorder(root.left)
        #data of node
        print(root.val,end=" ")
        #recur on right child
        printInorder(root.right)
def printPostorder(root):
    if root:
        #first recur on left child
        printPostorder(root.left)
        #recur on right child
        printPostorder(root.right)
        #data of node
        print(root.val,end=" ")
def printPreorder(root):
    if root:
        #data of node
        print(root.val,end=" ")
        #first recur on left child
        printPreorder(root.left)
        #recur on right child
        printPreorder(root.right)
root=Node(100)
root.left=Node(400)
root.right=Node(500)
root.left.left=Node(700)
root.left.right=Node(600)
root.right.left=Node(800)
root.right.right=Node(200)
root.left.right.left=Node(900)
root.right.right.left=Node(300)
print("inorder:")
printInorder(root)
print()
print("preorder:")
printPreorder(root)
print()
print("postorder:")
printPostorder(root)
print()
