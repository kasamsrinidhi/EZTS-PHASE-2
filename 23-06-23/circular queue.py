class CircularQueue:
    def __init__(self,size):
        self.size=size
        #can use self.queue=[None]*size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,data):
        #condition if queue is full
        if((self.rear+1)%self.size==self.front):#size 6 index from 0 to 5
            print("Queue is full\n")
        #condtion for empty queue
        elif (self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
            #always add at rear place
        else:
            #next position of rear
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if(self.front==-1):
            #condition for empty space
            print("queue is empty")
            #condition for only one eleement
        elif (self.front==self.rear):
            temp=self.queue[self.front]
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        #condition for empty queue
        if(self.front==-1):
            print("queue is empty")
        elif (self.rear>=self.front):
            print("elements in the circular queue",end="  ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        else:
            print("elements in circular queue are:",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        if ((self.rear+1)%self.size==self.front):
            print("queue is full")
obj=CircularQueue(5)
obj.enqueue(14)
obj.enqueue(22)
obj.enqueue(13)
obj.enqueue(-6)
obj.display()
print("deleted elmt:",obj.dequeue())
print("deleted elmt:",obj.dequeue())
obj.display()
obj.enqueue(10)
obj.enqueue(9)
obj.enqueue(8)
obj.display()
#it want to be inserted becoz queue is full
obj.enqueue(100)
