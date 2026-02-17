class Solution(object):
    def nextGreatestLetter(self, letters, target):
        first = 0
        last = len(letters) - 1
        
        while first <= last:
            mid = (first+last)//2
            if letters[mid] <= target:
                first = mid +1
            else:
                last = mid -1

        if first == len(letters):
            return letters[0]

        return letters[first]

