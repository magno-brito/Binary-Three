class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, value):
        if self.data is None:
            self.data = data
        else:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value)
                else:
                    self.right.insert(value)

        


        

