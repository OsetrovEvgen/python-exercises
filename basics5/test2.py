class NewTree:
    def __init__(self, data):
        self.data = data
        self.left_branch = None
        self.right_branch = None

    def bin_tree(self, data):
        if self.data:
            if data < self.data:
                if self.left_branch is None:
                    self.left_branch = NewTree(data)
                    print('Left Branch - ', data)
                else:
                    self.left_branch.bin_tree(data)
            if data > self.data:
                if self.right_branch is None:
                    self.right_branch = NewTree(data)
                    print('Right Branch - ', data)
                else:
                    self.right_branch.bin_tree(data)
        else:
            self.data = data

    def find(self, meaning):
        if meaning < self.data:
            if  self.left_branch is None:
                return str(meaning, ' - Not Found')
            return self.left_branch.find(meaning)
        elif meaning > self.data:
            if self.right_branch is None:
                return str(meaning, ' - Not Found')
            return self.right_branch.find(meaning)
        else:
            print(meaning, ' - is Found')


a = NewTree(10)
a.bin_tree(7)
a.bin_tree(15)
a.bin_tree(17)
a.bin_tree(11)
a.bin_tree(2)
a.bin_tree(9)
a.find(7)
