class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nset = set(nums)
        ans = 0
        
        for num in nums:
            if num - 1 not in nset:
                curr_ans = 1
                
                while num + curr_ans in nset:
                    curr_ans += 1
                
                ans = max(ans, curr_ans)  
                
        return ans