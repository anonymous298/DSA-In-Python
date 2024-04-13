class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node

        pointer = self.head
        while pointer.next:
            pointer = pointer.next

        pointer.next = Node(data, None)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid index')

        if index == 0:
            node = Node(data, self.head)
            self.head = node

        count = 0
        pointer = self.head

        while pointer:
            if count == index - 1:
                node = Node(data, pointer.next)
                pointer = node
                break

            count += 1
            pointer = pointer.next

    def get_length(self):
        count = 0
        pointer = self.head
        while pointer:
            count += 1
            poninter = pointer.next
        
        return count
    
    

