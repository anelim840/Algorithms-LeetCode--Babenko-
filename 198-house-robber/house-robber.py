class Solution(object):
    def rob(self, nums):
        a = 0
        b = 0

        for x in nums:
            c = max(a + x, b)
            a = b
            b = c

        return b