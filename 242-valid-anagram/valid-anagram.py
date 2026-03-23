class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        map = {}
        
        for i in range(len(s)):
            x = s[i]
            
            if x in map:
                map[x] += 1
            else:
                map[x] = 1
        
        for i in range(len(t)):
            x = t[i]
            
            if x not in map:
                return False
            
            map[x] -= 1
            
            if map[x] < 0:
                return False
        
        return True