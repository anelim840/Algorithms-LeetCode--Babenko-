class KthLargest(object):

    def __init__(self, k, nums):
        self.k = k
        self.heap = []

        for i in nums:
            self.add(i)

    def add(self, new):
        heapq.heappush(self.heap, new)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]
