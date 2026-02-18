class Solution(object):
    def merge(self, nums1, m, nums2, n):
        l1 = m - 1
        l2 = n - 1
        l = m + n - 1

        while l >=0 and l2 >= 0:
            if l1>=0 and nums1[l1]>nums2[l2]:
                nums1[l]=nums1[l1]
                l1-=1
            else:
                nums1[l]=nums2[l2]
                l2-=1
            l-=1
        