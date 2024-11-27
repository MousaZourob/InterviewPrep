class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        ans = []
        d = [i for i in range(1, n)]
        curr = n - 1

        for i, j in queries:
            while d[i] < j:
                d[i], i = j, d[i]
                curr -= 1
                
            ans.append(curr)
            
        return ans