class MyQueue(object):

    def __init__(self):
        self.size = 10000

        self.S1 = [0] * self.size
        self.top1 = 0

        self.S2 = [0] * self.size
        self.top2 = 0
        

    def push(self, x):
        self.S1[self.top1] = x
        self.top1 = self.top1 + 1
        

    def pop(self):
        if self.top2 == 0:
            while self.top1 > 0:

                self.top1 = self.top1 - 1
                value = self.S1[self.top1]

                self.S2[self.top2] = value
                self.top2 = self.top2 + 1

        self.top2 = self.top2 - 1
        return self.S2[self.top2]

    def peek(self):
        if self.top2 == 0:

            while self.top1 > 0:

                self.top1 = self.top1 - 1
                value = self.S1[self.top1]

                self.S2[self.top2] = value
                self.top2 = self.top2 + 1

        return self.S2[self.top2 - 1]
        

    def empty(self):
        if self.top1 == 0 and self.top2 == 0:
            return True
        else:
            return False
        
        

