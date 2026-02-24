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

    

#stack rverse  text homework
text = "PYTHON"
answer = ""
text_stack = Stack(len(text))
for i in text:
    text_stack.push(i)
while len(text_stack.values)>0:
    answer+=text_stack.values[len(text_stack.values)-1]
    text_stack.pushout()
print(answer)
#undo with stacks
stack = Stack(100)
t = ""
def type(t):
    stack.push(t)
def undo():
    stack.pop()
#check for palindrome using stack
user = "raceca"
checker = Stack(len(user))
for i in user:
    checker.push(i)
for j in range(len(user)):
    if user[j] == checker.values[len(checker.values)-1]:
        checker.pushout()
if len(checker.values)==0:
    print("palindrome")
else:
    print("not palindrome")
#decimal to binary convertor
num = 10
s = Stack(100)
while num>0:
    s.push(num%2)
    num//=2
#infix to postfix
equation = "a+b*c"

operations = {
    "/" : 4,
    "*" : 3,
    "+":2,
    "-":1

}
operations_stack = Stack(len(equation))

postfix = []
for i in range(len(equation)):
    if equation[i] in operations:
        if len(operations_stack.values)>0:
            while (len(operations_stack.values) > 0 and operations[equation[i]] <= operations[operations_stack.values[-1]]):
                postfix.append(operations_stack.values[-1])
                operations_stack.pushout()
            operations_stack.push(equation[i])
            
    else:
        postfix.append(equation[i])
    
for i in range(len(operations_stack.values)):
    postfix.append(operations_stack.values[-1])
    operations_stack.pushout()


       



print(postfix)


