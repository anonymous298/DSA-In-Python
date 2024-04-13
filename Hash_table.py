class HashTable:
    def __init__(self):
        self.MAX = 10
        self.Array = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        sum = 0
        for i in key:
            sum += ord(i)

        return sum % self.MAX
    
    def __setitem__(self, key, val):
        h = self.get_hash(key)

        if self.Array[h]:
            for index, element in enumerate(self.Array[h]):
                if element[0] == key and len(element) == 2:
                    self.Array[h][index] = (key, val)
                    break
        else:
            self.Array[h].append((key, val))
            print('inserted')

    def __getitem__(self, key):
        h = self.get_hash(key)

        if self.Array[h] == []:
            return 'Hash position is empty'

        for kv in self.Array[h]:
            if kv[0] == key:
                return kv[1]
            
    def __delitem__(self, key):
        h = self.get_hash(key)

        for index, element in enumerate(self.Array[h]):
            if element[0] == key:
                del self.Array[h][index]

if __name__ == "__main__":
    ht = HashTable()
    ht['talha'] = 16
    ht['talha'] = 46
    print(ht.Array)
    print(ht['talha'])