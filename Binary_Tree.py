class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if self.data == data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)

            else:
                self.left = BinaryTree(data)

        if data > self.data:
            if self.right:
                self.right.add_child(data)

            else:
                self.right = BinaryTree(data)