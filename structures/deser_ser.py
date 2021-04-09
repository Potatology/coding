class Node():
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    if not root:
        return 'x'
    return str(root.val) +',' + serialize(root.left) +',' + serialize(root.right) 

def deserialize(text):
    if text == '':
        return None
    l = text.split(',')
    def dfs(L):        
        if L[0] == 'x':
            L.pop(0)
            return None
        return Node(L.pop(0), dfs(L), dfs(L))
    return dfs(l)

sertree = serialize(Node(4,Node(3, Node(9)),Node(5)))
print(sertree)
desertree = deserialize(sertree)
print(desertree.right)









