class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.seen = {}
        for num in nums:
            self.add(num)
        
    def showFirstUnique(self) -> int:
        while self.q and not self.seen[self.q[0]]:
            self.q.popleft()
        if self.q:
            return self.q[0]
        return -1

    def add(self, value: int) -> None:
        if value not in self.seen:
            self.seen[value] = True
            self.q.append(value)
        else:
            self.seen[value] = False
            


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)