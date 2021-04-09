class Node(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(data):
    if data == []:
        return
    val = data.pop(0)
    root = Node(val)
    root.left = buildTree(data)
    root.right = buildTree(data)
    return root

def getNodeVals(root):
    if not root:
        return ''
    return str(root.val) + getNodeVals(root.left) + getNodeVals(root.right)


tree = buildTree([1,2,-1,3,4])
print(tree.val)
print(tree.left.val)
print(tree.left.left.val)

tree2 = buildTree(list(getNodeVals(tree)))