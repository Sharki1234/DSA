import random
class Queue:
    def __init__(self,size):
        self.queue = [None]*size
        self.front = 0
        self.rear = 0
        self.size = size 
    def enqueue(self,value):
        if self.rear < self.size:
            self.queue[self.rear] = value
            self.rear+=1
        else:
            print("queue overflow")
    def dequeue(self):
        if self.front<=self.rear:
            self.queue[self.front] = None
            self.front+=1
        else:
            print("queue underflow")

docs = Queue(3)
for i in range(3):
    doc = input("jkajks")
    docs.enqueue(doc)
for j in range(3):
    print(docs.queue[j],"is printing")
    docs.dequeue()


