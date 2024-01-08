# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        m, n = binaryMatrix.dimensions()
        ans = inf
        
        for row in range(m):
            l = 0
            r = n - 1
            
            while l <= r and l < ans:
                m = (l + r) // 2
                
                if binaryMatrix.get(row, m) == 0:
                    l = m + 1
                else:
                    r = m - 1
                    ans = min(ans, m)
        
        return ans if ans != inf else -1