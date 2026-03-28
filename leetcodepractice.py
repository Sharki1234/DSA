class MinStack(object):

    def __init__(self):
        self.values = []

    def push(self, val):
        self.values.append(val)
        

    def pop(self):
        self.values.pop()
        

    def top(self):
        return self.values[-1]
        

    def getMin(self):
        return(min(self.values))
        



obj = MinStack()
obj.push(5)
obj.push(7)
obj.push(9)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)
print(obj.values)