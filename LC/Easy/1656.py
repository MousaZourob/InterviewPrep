class OrderedStream:

    def __init__(self, n: int):
        self.list = [None] * n
        self.index = 0
        self.n = n

    def insert(self, idKey: int, value: str) -> List[str]:
        self.list[idKey - 1] = value
        
        if idKey - 1 > self.index:
            return []
        
        while self.index < self.n and self.list[self.index]:
            self.index += 1

        return self.list[idKey-1: self.index]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)