class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root):
    #set current to root of binary tree
    current=root
    stack=[]
    done=0
    while True:
        #reach the left most node of the current
        if current is not None:
        #place pointer to a tree node on the stack
        #before travsersing the nodes left subtree
            stack.append(current)
            current=current.left
#backtrack from empty subtree and visit node
#at the  top of the stack however the stack is empty u are done
        elif(stack):
            current=stack.pop()
            print(current.data,end="  ")
#we have visited the node and  its left
#subtree,now its right subtrees turn
            current=current.right
        else:
            break
    print()
#input
root=Node(100)
root.left=Node(400)
root.right=Node(500)
root.left.left=Node(700)
root.left.right=Node(600)
root.right.left=Node(800)
root.right.right=Node(200)
root.left.right.left=Node(900)
root.right.right.left=Node(300)
inorder(root)

