class MyTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is not None:
                    self.left.insert(data)
                else:
                    self.left = MyTree(data)
                    print('Left', data)

            if data > self.data:
                if self.right is not None:
                    self.right.insert(data)
                else:
                    self.right = MyTree(data)
                    print('Right', data)
        else:
            self.data = data


    def find(self, val):
        if val < self.data:
            if self.left is None:
                return str(val) + 'Not Found'
            return self.left.find(val)
        elif val > self.data:
            if self.right is None:
                return str(val) + 'Not Found'
            return self.right.find(val)
        else:
            print(str(val) + 'is Found')


    # def PrintTree(self):
    #     if self.left:
    #         self.left.PrintTree()
    #     print( self.data),
    #     if self.right:
    #         self.right.PrintTree()


root = MyTree(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.find(7))
print(root.find(11))
print(root.find(3))

