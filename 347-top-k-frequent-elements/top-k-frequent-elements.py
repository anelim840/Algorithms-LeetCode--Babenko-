class Solution(object):
    def topKFrequent(self, nums, k):
        d = {}
        
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        heap = []
        for key in d:
            heapq.heappush(heap, (d[key], key))
            if len(heap) > k:
                heapq.heappop(heap)
        
        return [i[1] for i in heap]