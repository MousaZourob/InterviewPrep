class Solution:
    def countPairs(self, nums1, nums2):
        n = len(nums1)

        difference = [nums1[i] - nums2[i] for i in range(n)]
        difference.sort()

        ans = 0
        l, r = 0, n - 1
                
        while l < r:
            if difference[l] + difference[r] > 0:
                ans += r - l
                r -= 1
            else:
                l += 1
        return ans