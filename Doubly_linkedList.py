class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class DoublyLL:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
        
        else:
            node = Node(data, self.head)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node

        pointer = self.head
        while pointer.next:
            pointer = pointer.next

        pointer.next = Node(data, None, pointer)

    def get_length(self):
        length = 0
        pointer = self.head
        while pointer:
            length += 1
            pointer = pointer.next

        return length

    def insert_at(self, data, index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        count = 0
        pointer = self.head

        while pointer:
            if count == index - 1:
                node = Node(data, pointer.next,pointer)
                pointer.next.prev = node
                pointer.next = node


            count += 1
            pointer = pointer.next
    