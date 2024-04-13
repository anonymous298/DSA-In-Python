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
        if self.head is None:
            print("Linked list in empty")

        count = 0
        pointer = self.head
        while pointer:
            count += 1
            pointer = pointer.next
        
        return count
    
    def traverse(self):
        if self.head is None:
            print("Linked list in empty")

        pointer = self.head
        llstr = ''

        while pointer:
            arrow = ''
            if pointer.next:
                arrow = '-->'

            llstr += str(pointer.data) + arrow
            pointer = pointer.next

        print(llstr)

    def remove_at(self, index):
        if index < 0 or index > self.get_length():
            print("Linked list in empty")

        if index == 0:
            self.head = self.head.next

        count = 0
        pointer = self.head
        while pointer:
            if count == index - 1:
                pointer.next = pointer.next.next
                break

            pointer = pointer.next
            count += 1



if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_begining(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.remove_at(1)
    ll.traverse()


