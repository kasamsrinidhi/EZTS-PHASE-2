class Node:
    def __init__(self,data):
        self.data=data
        self.previous=None
        self.next=None
class dll:
    def __init__(self):
        self.head=None
    def delete_pos():
        temp=self.head.next
        previous=self.head
        for i in range(1,pos-1):
            temp=temp.next
            previous=previous.next
        previous.next=temp.next
        temp.next=previous.next
      
    def display(self):
        if self.head is None:
            print("empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
l=dll()
n1=Node(100)
l.head=n1
n2=Node(200)
n2.prev=n1
n1.next=n2
n3=Node(300)
n3.prev=n2
n2.next=n3
n4=Node(900)
n4.prev=n3
n3.next=n4
print("before insertion")
l.display()
print("")
'''print("after insertion at beginning:")
l.delete_first()
l.display()
print("")
print("after insertion at end:")
l.insert_end()
l.display()
print("")'''
print("after insertion at position:")
l.delete_pos(2)
l.display()

