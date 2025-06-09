class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        
        top, bot = 0, len(matrix) - 1
        row = -1
        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                row = mid
                break
                
        if row < 0:
            return False
        
        l, r = 0, len(matrix[row]) - 1
        while l <= r:
            mid = (l+r) // 2
            
            if target > matrix[row][mid]:
                l = mid + 1
            elif target < matrix[row][mid]:
                r = mid - 1
            else:
                return True
        
        return False
    