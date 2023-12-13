class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        row_ones = defaultdict(int)
        col_ones = defaultdict(int)
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    row_ones[i] += 1
                    col_ones[j] += 1
                    
        ans = 0
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and row_ones[i] == 1 and col_ones[j] == 1:
                    ans += 1
                      
        return ans