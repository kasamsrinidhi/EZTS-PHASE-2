class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class singlelinkedlist:
    def __init__(slef):
        slef.head=None
    def insert_position(self,pos,data):
        np=Node(data)
        temp=self.head
        for i in range(pos-1):#1 iteration 1 happen
            temp=temp.next
        np.next=temp.next
        temp.next=np
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                 if temp.next!=None:
                    print(temp.data,end="--> ")
                 else:
                    print(temp.data,end=" ")
                 temp=temp.next
                
obj=singlelinkedlist()
#Node creation-initialising
n=Node(10)# so n.data in Node class will be 10
obj.head=n#assigning first node as head
n1=Node(20)
obj.head.next=n1#next node value
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
obj.display()
print('')
obj.insert_position(5,100)
obj.display()

