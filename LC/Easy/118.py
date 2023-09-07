class Solution:
    def generate(self, n: int) -> List[List[int]]:
        ans = [[1]]
        
        for i in range(1, n):
            row = [1]
            for j in range(1, i):
                row.append(ans[i-1][j-1] + ans[i-1][j])
            row.append(1)
            ans.append(row)
        
        return ans