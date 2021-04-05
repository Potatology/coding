class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next
    
    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newData):
        self.data = newData

    def setNext(self, newNext):
        self.next = newNext