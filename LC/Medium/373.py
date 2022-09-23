class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        
        n = min(k, len(nums1))
        m = min(k, len(nums2))
        
        for i in range(n):
            for j in range(m):
                if len(heap) < k:
                    heappush(heap, (-(nums1[i] + nums2[j]), [nums1[i], nums2[j]]))
                else:
                    if nums1[i] + nums2[j] > -heap[0][0]:
                        break
                    heappushpop(heap, (-(nums1[i] + nums2[j]), [nums1[i], nums2[j]]))
            
        
        return [[arr[0], arr[1]] for (_, arr) in heap]