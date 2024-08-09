class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        ans = []
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        
        step = 1
        direction = 0
        while len(ans) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    if 0 <= rStart < rows and 0 <= cStart < cols:
                        ans.append([rStart, cStart])
                    rStart += dirs[direction][0]
                    cStart += dirs[direction][1]

                direction = (direction + 1) % 4
            step += 1
        return ans