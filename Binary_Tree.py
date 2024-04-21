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

    def search(self, data):
        if data == self.data:
            return True
        
        if data < self.data:
            if self.left:
                return self.left.search(data)

            else:
                return False
        
        if data > self.data:
            if self.right:
                return self.right.search(data)
            
            else:
                return False
            
    def delete(self, data):
        if data > self.data:
            if self.right:
                self.right.delete(data)

        if data < self.data:
            if self.left:
                self.left.delete(data)

        else:
            if self.left is None and self.right is None:
                return None
            
            if self.left is None:
                return self.right
            
            if self.right is None:
                return self.left
            
            max_val = self.right.find_max()
            self.data = max_val
            self.right = self.right.delete(max_val)

        return self

    def find_max(self):
        if self.right is None:
            return self.data
        
        return self.right.find_max()
    
    def find_min(self):
        if self.left is None:
            return self.data
        
        return self.left.find_min()


    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)

        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()

        return 
    
    def post_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

    
def build_tree(data_list):
    print(f"Building the tree with {data_list}")
    root = BinaryTree(data_list[0])
    for i in range(1, len(data_list)):
        root.add_child(data_list[i])

    return root


if __name__ == "__main__":
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    root = build_tree(numbers)
    print(root.in_order_traversal())
    root.delete(20)
    # root.delete(20)
    print(root.in_order_traversal())
    pass