class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        heapify(heap)
        
        start, end = 0, inf
        curr_max = -inf
        
        for l in nums:
            heappush(heap, (l[0], 0, l))
            curr_max = max(l[0], curr_max)
        
        while len(heap) == len(nums):
            num, i, lst = heappop(heap)
                        
            if end - start > curr_max - num:
                start = num
                end = curr_max
            
            if len(lst) > i + 1:
                heappush(heap, (lst[i + 1], i+1, lst))
                curr_max = max(lst[i + 1], curr_max)
        
        return [start, end]