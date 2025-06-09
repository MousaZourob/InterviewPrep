class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        def dfs(i, ans, transfers): 
            if i == len(requests):
                return ans if all(t == 0 for t in transfers) else 0
            
            exclude = dfs(i+1, ans, transfers)
            
            transfers[requests[i][0]] -= 1
            transfers[requests[i][1]] += 1
            
            include = dfs(i+1, ans+1, transfers)

            transfers[requests[i][0]] += 1
            transfers[requests[i][1]] -= 1
            
            return max(include, exclude)
        
        return dfs(0, 0, [0]*n)