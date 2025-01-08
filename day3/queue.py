class Queue:
    def __init__(self):
        self.value = []

    def enqueue(self, x):
        self.value.append(x)

    def dequeue(self):
        if self.value:
            return self.value.pop(0)
        else:
            return ("Queue is empty")
            

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print("after enqueues:", q.value)
print("dequeue:", q.dequeue())
print("after dequeue:", q.value)
