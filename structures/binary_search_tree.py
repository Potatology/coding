import tree_node

class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.size = 0
    
    def length(self):
        return self.size
    def __len__(self):
        return self.size
    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)
        else:
            self.root = tree_node.TreeNode(key, val)
        self.size += 1
    
    def _put(self, key, val, currentNode):
        if key < currentNode.key:
            if currentNode.has_left_child():
                self._put(key, val, currentNode.left_child)
            else:
                currentNode.left_child = tree_node.TreeNode(key, val, parent=currentNode)
        else:
            if currentNode.has_right_child():
                self._put(key, val, currentNode.right_child)
            else:
                currentNode.right_child = tree_node.TreeNode(key, val, parent=currentNode)

    def __setitem__(self, k, v):
        self.put(k,v)
    
    def get(self, key):
        if self.root:
            result = _get(key, self.root)
            if result:
                return result.val
            else: 
                return None
        else:
            return None
    
    def _get(self, key, current_node):
        if not current_node:
            return None
        elif key == current_node.key:
            return current_node
        elif key < current_node.key:
                self._get(key, current_node.left_child)
        else:
                self_get(key, current_node.right_child)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False
            
