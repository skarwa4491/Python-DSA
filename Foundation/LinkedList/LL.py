class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    size = 0

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def addLast(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1
        return self.head

    def addFirst(self, data):
        node = Node(data)
        if self.size == 0:
            self.head = self.tail = node
        elif self.head:
            node.next = self.head
            self.head = node
        self.size += 1
        return self.head

    def display(self):
        head = self.head
        while(head):
            print(head.data, end="\t")
            head = head.next
        print("\n")

    def getSize(self):
        return self.size

    def getFirst(self):
        if self.head:
            return self.head
        else:
            print('List is empty')
            return None

    def getLast(self):
        if self.tail:
            return self.tail
        else:
            print('List is empty')
            return None

    def getAtIndex(self, index):
        if self.size == 0:
            print('List is empty')
            return Node(-1)
        if index > self.size:
            print('request index is out of range')
            return Node(-1)
        node = self.head
        i = 0
        while i < index:
            node = node.next
            i += 1
        return node

    def removeLast(self):
        if self.size == 0:
            print('List is empty')
            return

        if self.size == 1:
            self.head = self.tail = None
            self.size = 0
            return

        node = self.head
        while(node):
            if node.next == self.tail:
                node.next = None
                self.tail = node
                self.size -= 1
                return self.head
            node = node.next

    def removeFirst(self):
        if self.size == 0:
            print('List is empty')
            return None
        if self.size == 1:
            removed = self.head
            self.head = self.tail = None
            self.size = 0
            return removed
        removed = self.head
        self.head = self.head.next
        self.size -= 1
        return removed

    def removeAtIndex(self, index):
        if self.size == 0 or index > self.size:
            print('Invalid Arguments')
            return None
        if index == 0:
            self.removeFirst()
            self.size -= 1
            return
        if index == self.size-1:
            self.removeLast()
            self.size -= 1
            return self.head
        i = 0
        node = self.head
        while i < index-1:
            node = node.next
            i += 1
        remove = node.next
        node.next = node.next.next
        remove.next = None
        self.size -= 1
        return self.head
