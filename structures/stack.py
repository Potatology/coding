class Stack:
    def __init__(self):
        self.items = []
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def peek(self):
        return self.items[len(self.items)-1]
    
    def push(self, item):
        self.items.append(item)
    
    def size(self):
        return len(self.items)

# objectStack = Stack()
# objectStack.push(420)
# objectStack.push('Varghul')
# objectStack.push(True)
# for obj in objectStack.items:
#     print(obj) 
# print(':Pass 1') 
# objectStack.pop()
# type(objectStack.peek())
# objectStack.push(objectStack.peek() + ' Boomaye ' + str(objectStack.size()))
# for obj in objectStack.items:
#     print(obj)
# print(':Pass 2')


