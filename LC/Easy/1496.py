class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        crossed = set()
        crossed.add((0, 0))
        
        for p in path:
            if p == "E":
                x += 1
            elif p == "W":
                x -= 1
            elif p == "N":
                y += 1
            elif p == "S":
                y -= 1

            if (x, y) in crossed:
                return True
            else:
                crossed.add((x,y))
            
        return False