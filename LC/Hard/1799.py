class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        dp = defaultdict(int)
        
        def dfs(mask, op):
            if mask in dp:
                return dp[mask]
            for i in range(len(nums)):
                for j in range(i + 1, len(nums)):
                    if (1 << i) & mask or (1 << j) & mask:
                        continue
                        
                    newMask = mask | (1 << i) | (1 << j)
                    score = op * gcd(nums[i], nums[j])
                    dp[mask] = max(dp[mask], score + dfs(newMask, op + 1))
            return dp[mask]

        return dfs(0, 1)
