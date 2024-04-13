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
    
    def traverse_forward(self):
        if self.head is None:
            print("Doubly LL is empty")

        pointer = self.head
        llstr = ''
        while pointer:
            arrow = ''
            if pointer.next:
                arrow = '-->'
            llstr += str(pointer.data) + arrow
            pointer = pointer.next

        print(llstr)

    def traverse_backward(self):
        if self.head is None:
            print("Doubly LL is empty")

        pointer = self.head
        llstr = ''
        
        while pointer.next:
            pointer = pointer.next

        while pointer:
            arrow = ''
            if pointer.prev:
                arrow = '<--'
            llstr += str(pointer.data) + arrow
            pointer = pointer.prev

        print(llstr)

if __name__ == "__main__":

    dll = DoublyLL()
    dll.insert_at_begining(4)
    dll.insert_at_end(5)
    dll.insert_at_end(6)
    dll.insert_at_end(7)
    dll.insert_at(10,1)
    dll.traverse_forward()
    dll.traverse_backward()