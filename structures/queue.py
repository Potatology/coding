class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return self.items==[]


def test():
    q = Queue()
    print('Size: ')
    print(q.size())
    q.enqueue(1)
    q.enqueue('g')
    print('Size step 2: ')
    print(q.size())
    for item in q.items:
        print(str(q.items.index(item)) + ' index of item: ' + str(item))
    q.dequeue()
    print('Is q empty: ')
    print(q.isEmpty())
    q.dequeue()
    print('Is q empty step final: ')
    print(q.isEmpty())

    
