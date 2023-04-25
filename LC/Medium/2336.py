class SmallestInfiniteSet:

    def __init__(self):
        self.available = [True]*1001

    def popSmallest(self) -> int:
        for i in range(1000):
            if self.available[i]:
                self.available[i] = False
                return i+1

    def addBack(self, num: int) -> None:
        self.available[num-1] = True


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)