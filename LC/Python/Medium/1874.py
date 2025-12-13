class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse = True)
        n = len(nums1)
        ans = 0

        for i in range(n):
            ans += nums1[i] * nums2[i]

        return ans
