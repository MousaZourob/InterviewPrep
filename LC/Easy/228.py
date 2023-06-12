class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        ranges = []
        i = 0
        
        while i < len(nums):
            start = nums[i]
            while i + 1 < len(nums) and nums[i+1] == nums[i] + 1:
                i += 1
                
            if nums[i] == start:
                ranges.append(f'{start}')
            else:
                ranges.append(f'{start}->{nums[i]}')
            
            i += 1
        
        return ranges