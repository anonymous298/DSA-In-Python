class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLL:
    def __init__(self):
        self.head = None

    def add_at_begining(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
        
        else:
            node = Node(data, self.head)
            self.head.prev = node
            self.head = node

    def add_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node

        pointer = self.head
        while pointer.next:
            pointer = pointer.next

        pointer.next = Node(data, None, pointer)
    