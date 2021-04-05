# ((())))

class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items==[]
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self[len(self.items) - 1]
    def size(self):
        return len(self.items)

def checkParents(parString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(parString) and balanced: 
        par = parString[index]
        if par == "(":
            s.push(par)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()

        index += 1
    if balanced and s.isEmpty():
        return True
    else: return False

print(checkParents('((()))()()'))
print(checkParents('((()))()()]'))


