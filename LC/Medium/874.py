class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        d = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        x, y, di = 0, 0, 0
        ans = 0
        obstacleSet = set(map(tuple, obstacles))
        
        for command in commands:
            if command == -1:
                di = (di + 1) % 4
            elif command == -2:
                di = (di - 1) % 4
            else:
                for i in range(command):
                    if (x + d[di][0], y + d[di][1])  in obstacleSet:
                        break
                        
                    x += d[di][0]
                    y += d[di][1]
                    ans = max(ans, x**2 + y**2)
                        
        return ans