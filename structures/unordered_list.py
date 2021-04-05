import node

class UnorderedList:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        self.temp = node.Node()
        self.temp.data = data
        if self.head:
            self.temp.next = self.head
            self.head = self.temp        
        else:
            self.head = self.temp

    def remove(self, data):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.data == data:
                found = True
                if  previous == None:
                    self.head = current.next           
                else: 
                    previous.next = current.next
            previous = current
            current = current.next

    def remove_book(self, data):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == data:
                found = True
            else: 
                previous = current
                current = current.next
        if previous == None:
            self.head = current.next
        else: 
            previous.setNext(current.next)

    def isEmpty(self):
        return self.head == None

    def length(self):
        len = 0
        current = self.head
        while current != None:
            len += 1 
            current = current.getNext()
        return len 
    
    def search(self, query):
        current = self.head
        found = False
        while current != None:
            if current.data == query:
                found = True
                break
            current = current.getNext()
        return found
            
    def printList(self):
        current = self.head
        while current != None:
            print(current.data)
            current = current.next

def add_test():
    ul = UnorderedList()
    ul.add(2)
    ul.add(4)
    ul.add('Dolina')
    ul.printList()

def search_test():
    ul = UnorderedList()
    ul.add(1)
    ul.add(3)
    print(ul.search(3))

def isEmpty_test():
    ul = UnorderedList()
    #ul.add('kebab')
    return ul.isEmpty()

def length_test():
    ul = UnorderedList()
    ul.add(1)
    ul.add(3)
    ul.add('k3bab')
    print(ul.length())    

def remove_test():
    ul = UnorderedList()
    ul.add(1)
    ul.add(3)
    ul.add('k3bab')
    ul.add('True')
    ul.remove_book('True')
    ul.printList()
