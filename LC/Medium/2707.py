class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dictionary = set(dictionary)
        dp = {}
        
        def dfs(start):
            if start == n:
                return 0
            if start in dp:
                return dp[start]
            
            ans = dfs(start + 1) + 1
            for end in range(start, n):
                curr = s[start: end + 1]
                if curr in dictionary:
                    ans = min(ans, dfs(end + 1))
            dp[start] = ans
            return ans
            
        return dfs(0)