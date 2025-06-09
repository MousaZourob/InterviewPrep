class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        i1 = i2 = 0
        
        while i1 < n1 and i2 < n2:
            if nums1[i1] == nums2[i2]:
                return nums1[i1]
            elif nums1[i1] > nums2[i2]:
                i2 += 1
            else:
                i1 += 1
        
        return -1