class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1

        n1 = len(nums1)
        n2 = len(nums2)
        total = n1 + n2
        half = total // 2
            
        l, r = 0, n1 - 1
        
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            n1left = nums1[i] if i >= 0 else -inf
            n1right = nums1[i + 1] if i + 1 < n1 else inf
            
            n2left = nums2[j] if j >= 0 else -inf
            n2right = nums2[j + 1] if j + 1 < n2 else inf
            
            if n1left <= n2right and n2left <= n1right:
                if total % 2:
                    return min(n1right, n2right)
                else:
                    return (max(n1left, n2left) + min(n1right, n2right)) / 2
            elif n1left > n2right:
                r = i - 1
            else:
                l = i + 1