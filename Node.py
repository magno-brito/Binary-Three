class Node:
    def __init__(self,data,turtle):
        self.data = data
        self.left = None
        self.right = None
        self.turtle = turtle

    def insert(self, value):
        if self.data is None:
            self.data = value
        else:
            if value < self.data:
                if self.left is None:
                    self.left = Node(value,self.turtle)
                else:
                    self.left.insert(value)
            elif value > self.data:
                if self.right is None:
                    self.right = Node(value,self.turtle)
                else:
                    self.right.insert(value)

    def inOrderPrint(self):
        if self.data is None:
            return
        else:
            self.inOrderPrint(self.left)
            print(root.data)
            self.inOrderPrint(self.right)
    
    def drawTree(self,length, node):
            if(length<10):
                return
            else:
                if node.data:
                    self.turtle.forward(length)
                    self.turtle.color("red")
                    self.turtle.write(node.data, font=("arial",14,"bold"))
                    self.turtle.color("black")
                    self.turtle.left(30)
                    if node.right:
                        self.drawTree(3*length/4,node.right)
                    self.turtle.right(45)
                    if node.left:
                        self.drawTree(3*length/4,node.left)
                    self.turtle.left(15)
                    self.turtle.backward(length)
                else:
                    return 

            


            

