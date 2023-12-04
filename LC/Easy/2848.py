class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        merged = [nums[0]]
        
        for interval in nums:
            if merged[-1][1] >= interval[0]:
                merged[-1][1] = max(merged[-1][1], interval[1])
            else:
                merged.append(interval)
            
        
        ans = 0
        print(merged)
        
        for interval in merged:
            ans += interval[1] - interval[0] + 1
        
        return ans