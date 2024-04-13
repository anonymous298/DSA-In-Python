from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def Enqueue(self, data):
        self.container.insert(0, data)

    def Dequeue(self):
        self.container.pop()

    def print(self):
        print(self.container)

    def get_length(self):
        count = 0
        for i in range(len(self.container)):
            count += 1

        return count
    


if __name__ == "__main__":
    q = Queue()
    q.Enqueue(3)
    q.Enqueue(4)
    q.Enqueue(5)
    q.Dequeue()
    q.print()