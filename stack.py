class Stack:
    def __init__(self,top):
        self.values = []
        self.top = top
    def push(self,value):
        if len(self.values) < self.top:
            self.values.append(value)
        else:
            return False
    def pushout(self):
        if len(self.values)>0:
            self.values.pop()
        else:
            print("stack is empty")
    def display(self):
        print(self.values)
    def length(self):
        len(self.values)

              

stack1 = [None]*2
stack2 = [None]*3
rear = 0
front = 0
size = 5
def push(value):
    global rear
    if rear>len(stack1)-1 :
        if rear<size:
            stack2[rear-len(stack1)] = value
            rear+=1
    else:
        stack1[rear] = value
        rear+=1
def pushout():
    global front,rear
    if front<=rear:
        if front>len(stack1)-1 :
            if front<size:
                stack2[front-len(stack1)-1] = None
                front+=1
        else:
            stack1[front] = None
            front+=1
for i in range(5):
    push(5)

pushout()
print(stack1)
print(stack2)
