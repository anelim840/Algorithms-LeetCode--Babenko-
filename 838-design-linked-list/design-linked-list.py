class Node(object):

    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        current = self.head

        for i in range(index):
            current = current.next

        return current.val 
        

    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node

        self.size = self.size + 1
        

    def addAtTail(self, val):
        node = Node(val)

        if self.head is None:
            self.head = node
        else:
            current = self.head

            while current.next is not None:
                current = current.next

            current.next = node

        self.size = self.size + 1
        

    def addAtIndex(self, index, val):
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        node = Node(val)

        current = self.head

        for i in range(index - 1):
            current = current.next

        node.next = current.next
        current.next = node

        self.size = self.size + 1



    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head

            for i in range(index - 1):
                current = current.next

            current.next = current.next.next

        self.size = self.size - 1








        