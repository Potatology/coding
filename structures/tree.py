def binary_tree(r):
    return[r,[],[]]

def insert_left(root, new_branch):
    temp = root.pop(1)
    if len(temp)>1:
        root.insert(1, [new_branch, temp, []])
    else: 
        root.insert(1, [new_branch,[],[]])
    return root

def insert_right(root, new_branch):
    temp = root.pop(2)
    if len(temp)>1:
        root.insert(2, [new_branch, [], temp])
    else: 
        root.insert(2, [new_branch,[],[]])
    return root

def get_root_value(root):
    return root[0]

def set_root_value(root, value):
    root[1] = value

def get_left_child(root):
    return(root[1])

def get_right_child(root):
    return(root[2])
    
tree = binary_tree(1)
kazoo = 'kazoo'

for i in range(len(kazoo)):
    insert_left(tree, kazoo[i:])
    insert_right(tree, kazoo[i:])




serialize(tree)
print(tree)