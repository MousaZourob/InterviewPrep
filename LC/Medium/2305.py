class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        ans = [inf]
        
        
        def dfs(i, count):
            if i >= n:
                ans[0] = min(ans[0], max(count))
                return
            
            for j in range(k):
                count[j] += cookies[i]
                dfs(i + 1, count)
                count[j] -= cookies[i]
                if count[j] == 0: break
        
        
        dfs(0, [0]*k)
        
        return ans[0]