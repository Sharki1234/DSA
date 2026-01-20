class Stack:
    def __init__(self,top):
        self.values = []
        self.top = top
    def push(self,value):
        if len(self.values) < self.top:
            self.values.append(value)
        else:
            print("the stack is full")
    def pushout(self):
        if len(self.values)>0:
            self.values.pop()
        else:
            print("stack is empty")
    def display(self):
        print(self.values)
    

open = ["(","[","{"]
closing = [")","]","}"]
def validity(expression):
    new_stack = Stack(len(expression))
    
    for i in expression:
        if i in open:
            new_stack.push(i)
        elif i in closing:
            pos = closing.index(i)
            if len(new_stack.values)>0 and open[pos] == new_stack.values[len(new_stack.values)-1]:
                new_stack.pushout()
            else:
                
                return "imbalanced"
    if len(new_stack.values)==0:
        return "balanced"
    else:
        return "imbalanced"


                


print(validity("(a+b"))