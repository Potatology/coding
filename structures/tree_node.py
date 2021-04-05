class TreeNode():
    def __init__(self, key, val, parent = None, left_child = None, right_child = None):
        self.key = key
        self.val = val
        self.parent = parent
        self.left_child = left_child
        self.right_child = right_child

    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return: not (self.right_child or self.left_child)

    def has_left_child(self):
        return self.left_child
    
    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return: self.parent and self == parent.left_child

    def is_right_child(self):
        return: self.parent and self == parent.right_child

    def has_both_children(self):
        return self.right_child and self.left_child
    
    def has_any_children(self):
        return self.right_child or self.left_child

    def replace_node_data(self, key, value, right_child, left_child):
        self key = key
        self.val = val
        self.left_child = left_child
        self.right_child = right_child
        if self.has_left_child:
            left_child.parent = self
        if self.has_right_child:
            right_child.parent = self

