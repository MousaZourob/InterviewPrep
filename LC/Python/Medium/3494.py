class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        dp = [0] * n
        dp[0] = skill[0]
        for i in range(1, n):
            dp[i] = dp[i - 1] + skill[i]
        
        start_time = 0
        for i in range(1, m):
            max_diff = mana[i - 1] * dp[0]
            for j in range(1, n):
                curr_diff = (mana[i-1] * dp[j]) - (mana[i] * dp[j-1]) 
                if curr_diff > max_diff:
                    max_diff = curr_diff

            start_time += max_diff

        return start_time + mana[m-1] * dp[n-1]