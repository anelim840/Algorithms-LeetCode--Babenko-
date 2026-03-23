class Solution(object):
    def intersection(self, nums1, nums2):
        d = {}
    
        for x in nums1:
            d[x] = 1
        r= []
        
        for x in nums2:
            if x in d:
                r.append(x)
                
                del d[x]
        
        return r
        