class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        pairs = [(a,b) for a,b in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])
        
        heap = []
        
        total = 0
        for pair in pairs:
            heappush(heap, pair[0])
            total += pair[0]
            
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                ans = max(ans, total * pair[1])
        
        return ans