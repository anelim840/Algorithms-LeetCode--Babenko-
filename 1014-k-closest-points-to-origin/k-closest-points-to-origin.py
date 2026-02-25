class Solution(object):
    def kClosest(self, points, k):
        heap = []
        for x, y in points:
            d = x*x + y*y
            heapq.heappush(heap, (-d, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for d, x, y in heap]