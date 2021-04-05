class BinaryTree():
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

    def set_root_value(self, new_data):
        self.data = new_data

    def get_root_value(self):
        return self.data

    def insert_left(self, data):
        if self.left_child == None:
            self.left_child = BinaryTree(data)
        else:
            temp = BinaryTree(data)
            temp.left_child = self.left_child
            self.left_child = temp

    def get_left(self):
        return self.left_child

    def insert_right(self, data):
        if self.right_child == None:
            self.right_child = BinaryTree(data)
        else:
            temp = BinaryTree(data)
            temp.right_child = self.right_child
            self.right_child = temp
    
    def get_right(self):
        return self.right_child



