class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        curr = []
        def dfs(first):
            if len(curr) == k:
                ans.append(curr[:])
                return
                
            need = k - len(curr)
            remain = n - first + 1
            available = remain - need
            
            
            for i in range(first, first + available + 1):
                curr.append(i)
                dfs(i + 1)
                curr.pop()
            
        ans = []
        dfs(1)
        return ans