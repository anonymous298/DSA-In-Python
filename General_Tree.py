class GeneralTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):

        spaces = " " * self.get_level() * 3
        prefix = spaces + '|__' if self.parent else ''
        
        print(prefix + self.data)
    
        for child in self.children:
            child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        
        return level



if __name__ == "__main__":
    electronics = GeneralTree('Electronics')

    laptop = GeneralTree('Laptop')
    laptop.add_child(GeneralTree('Lenovo'))
    laptop.add_child(GeneralTree('ThinkPad'))
    laptop.add_child(GeneralTree('Apple'))

    electronics.add_child(laptop)

    electronics.print_tree()

