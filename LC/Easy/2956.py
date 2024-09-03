class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [0, 0]
        count = Counter(nums1)
        
        for num in nums2:
            if num in count:
                ans[0] += count[num]
                ans[1] += 1
                count[num] = 0
        
        return ans