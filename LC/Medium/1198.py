class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        count = [0]*10001
        for row in mat:
            for c in row:
                count[c] += 1
        
        m = len(mat)

        for i, num in enumerate(count):
            if num == m:
                return i
            
        return -1