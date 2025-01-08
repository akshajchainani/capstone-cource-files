class Stack:
    def __init__(self):
        self.value = []

    def push(self, x):
        self.value = [x] + self.value

    def pop(self):
        if not self.is_empty():
            return self.value.pop(0)
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.value) == 0

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.push(40)
print("after pushes:", s.value)
print("pop:", s.pop())
print("after pop:", s.value)
s.push(50)
print("after pushes:", s.value)
print("pop:", s.pop())
print("after pop:", s.value)
