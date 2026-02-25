class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = []

        for i in nums:
            self.add(i)

    def add(self,val):
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
