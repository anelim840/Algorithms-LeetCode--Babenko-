class Solution(object):
    def canPartition(self, nums):
        s = sum(nums)  # сумма всех чисел

        if s % 2 != 0:
            return False  # если нечётная, то нет

        t = s // 2  

        dp = [False] * (t + 1)
        dp[0] = True  # всегда true при 0

        for x in nums:  # проходим по числам
            for i in range(t, x - 1, -1):
                if dp[i - x]:
                    dp[i] = True

        return dp[t]