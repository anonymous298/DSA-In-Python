class Array:
    def __init__(self):
        self.array = []

    def append(self, data):
        self.array.append(data)

    def pop(self):
        if self.array is None:
            print("Array is empty")

        self.array.pop()

    def insert(self, index, data):
        if self.array is None:
            print("Array is empty")

        self.array.insert(index, data)

    @property
    def length(self):
        count = 0
        for i in range(len(self.array)):
            count += 1

        return count
    
    def print(self):
        print(self.array)



if __name__ == "__main__":
    array = Array()
    array.append(5)
    array.append(6)
    # array.pop()
    print(array.length)
    array.print()