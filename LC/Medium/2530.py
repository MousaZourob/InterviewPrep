class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        heap = []
        
        for num in nums:
            heappush(heap, -num)
        
        while k > 0:
            curr = -heappop(heap)
            
            ans += curr
            
            heappush(heap, -ceil(curr / 3))
            k -= 1
            
        return ans