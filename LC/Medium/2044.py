class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = defaultdict(int)
        dp[0] = 1
        max_or = 0
        
        for n in nums:
            new_dp = deepcopy(dp)
            for cur_or, count in dp.items():
                new_or = n | cur_or
                new_dp[new_or] += count
            
            dp = new_dp
            max_or |= n
        
        return dp[max_or]