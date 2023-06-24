stack=[]
def push():
    e=int(input("enter :"))
    stack.append(e)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        a=stack.pop()
        print("removed element:",a)
while True:
    print("select option 1.push 2.pop 3.display 4.peek 5.quit")
    c=int(input())
    if c==1:
        push()
    elif c==2:
        pop()
    elif c==3:
        print(stack)
    elif c==4:
        print(stack[len(stack)-1])
    elif c==5:
        break
    else:
        print("enter correct option")
