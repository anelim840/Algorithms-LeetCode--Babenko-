class MinStack(object):

    def __init__(self):
        self.size = 10000
        self.A = [0] * self.size
        self.M = [0] * self.size
        self.t = 0
        self.mt = 0


    def push(self, x):
        self.A[self.t] = x
        self.t = self.t + 1
        if self.mt == 0:

            self.M[self.mt] = x
            self.mt = self.mt + 1

        else:
            current_min = self.M[self.mt - 1]
            if x <= current_min:
                self.M[self.mt] = x
                self.mt = self.mt + 1


    def pop(self):
        if self.t == 0:
            return

        self.t = self.t - 1
        x = self.A[self.t]
        
        current_min = self.M[self.mt - 1]

        if x == current_min:
            self.mt = self.mt - 1


    def top(self):
        if self.t == 0:
            return None

        return self.A[self.t - 1]


    def getMin(self):
        if self.mt == 0:
            return None

        return self.M[self.mt - 1]