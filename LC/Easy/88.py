class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m + n - 1
        
        while m > 0 and n > 0:
            curr = max(nums1[m-1], nums2[n-1])
            if nums1[m-1] >= nums2[n-1]:
                m -= 1
            else:
                n -= 1
            
            nums1[i] = curr
            i -= 1
        
        for j in range(n-1,-1,-1):
            nums1[i] = nums2[j]
            i -= 1
        
        return nums1