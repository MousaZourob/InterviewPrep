class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        px, py = point
        
        for x,y in self.points.keys():
            if abs(py - y) != abs(px - x) or x == px or y == py:
                continue
            if (px, y) in self.points and (x, py) in self.points:
                ans += self.points[(px, y)] * self.points[(x, py)] * self.points[(x, y)]

        return ans

# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)