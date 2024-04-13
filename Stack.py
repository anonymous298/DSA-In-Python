from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, data):
        self.container.append(data)

    def pop(self):
        self.container.pop()

    def print(self):
        print(self.container)

    def get_length(self):
        count = 0
        for i in range(len(self.container)):
            count += 1

        return count

    

if __name__ == "__main__":
    s = Stack()
    s.push(4)
    s.push(5)
    s.push(6)
    s.pop()
    s.print()
    print(s.get_length())