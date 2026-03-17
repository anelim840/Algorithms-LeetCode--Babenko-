class MyCircularQueue(object):

    def __init__(self, k):
        self.size = k
        self.Q = [0] * k

        self.head = 0
        self.tail = 0

        self.count = 0

    def enQueue(self, value):
        if self.count == self.size:
            return False

        self.Q[self.tail] = value
        self.tail = (self.tail + 1) % self.size
        self.count = self.count + 1

        return True
        

    def deQueue(self):
        if self.count == 0:
            return False

        self.head = (self.head + 1) % self.size
        self.count = self.count - 1

        return True

    def Front(self):
        if self.count == 0:
            return -1

        return self.Q[self.head]
        

    def Rear(self):
        if self.count == 0:
            return -1

        return self.Q[(self.tail - 1) % self.size]

    def isEmpty(self):
        if self.count == 0:
            return True
        else:
            return False

    def isFull(self):
        if self.count == self.size:
            return True
        else:
            return False
        


