class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.vec = vec
        self.r = 0
        self.c = 0

    def get_next(self):
        while self.r < len(self.vec) and self.c == len(self.vec[self.r]):
            self.r += 1
            self.c = 0

    def next(self) -> int:
        self.get_next()
        res = self.vec[self.r][self.c]
        self.c += 1
        return res

    def hasNext(self) -> bool:
        self.get_next()
        return self.r < len(self.vec)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()