stack_1=[]
stack_2=[]
def push():
    for i in range(5):
        e=int(input("enter element:"))
        if(e%2==0):
            stack_1.append(e)
        else:
            stack_2.append(e)
def pop():
    pop_what=input("even 0r odd")
    if pop_what=='1':
        if not stack_1:
            print("stack is empty")
        else:
            a=stack_1.pop()
            print("removed element:",a)
            print(stack_1)
def show():
    what=input("1 or 2")
    if what=="1":
        print(stack_1)
    else:
        print(stack_2)
while True:
    print("1.push 2.pop 3.show 4.quit")
    c=int(input())
    if c==1:
        push()
    elif c==2:
        pop()
    elif c==3:
        show()
    elif c==4:
        break
    else:
        print("crct option")
