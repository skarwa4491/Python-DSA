class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None

class linked_list():
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add_first(self , data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head = node
        self.size+=1
        return self.head

    def add_last(self,data):
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size+=1

    def display(self):
        if self.head is None:
            return 'head is None'
        node = self.head
        while node is not None:
            print(node.data,end='\t')
            node = node.next
        print()
        

    
ll = linked_list()
for i in range(0,5):
    ll.add_last(i)
ll.display()
print(ll.head.data)
print(ll.tail.data)
print(ll.size)