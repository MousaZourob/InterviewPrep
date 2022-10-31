class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(cols):
            curr = matrix[rows-1][i]
            j = 0
            
            while rows-1-j >= 0 and i-j >= 0:
                if curr != matrix[rows-1-j][i-j]:
                    return False
                j += 1
        
        for i in range(rows):
            curr = matrix[i][cols-1]
            j = 0
            
            while cols-1-j >=0 and i-j >= 0:
                if curr != matrix[i-j][cols-1-j]:
                    return False
                j+=1
        
        
        return True