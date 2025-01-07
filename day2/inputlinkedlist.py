class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def create(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end="  ")
            current = current.next
        print("None")


ll = LinkedList()

n = int(input("add at the end: "))
for _ in range(n):
    data = int(input("Enter data: "))
    ll.create(data)

print("adding nodes at the end:")
ll.display()

data = int(input("insert at the beginning: "))
ll.insert_at_beginning(data)

print("inserting at the beginning:")
ll.display()
