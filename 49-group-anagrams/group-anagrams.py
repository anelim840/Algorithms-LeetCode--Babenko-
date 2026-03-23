class Solution(object):
    def groupAnagrams(self, strs):
        d = {}
        
        for w in strs:
            key = "".join(sorted(w))
            
            if key not in d:
                d[key] = []
            
            d[key].append(w)
        
        return list(d.values())
        