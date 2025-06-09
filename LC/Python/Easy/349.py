class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:  
        ans = []
        seen1 = Counter(nums1)
        
        for n in nums2:
            if n in seen1:
                ans.append(n)
                del seen1[n]
                
        return ans