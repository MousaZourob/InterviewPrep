class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        vals = defaultdict(list)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                vals[i+j].append(mat[i][j])
                
        ans = []
        for k, v in vals.items():
            if k % 2 == 0:
                ans.extend(v[::-1])
            else:
                ans.extend(v)
                
        return ans