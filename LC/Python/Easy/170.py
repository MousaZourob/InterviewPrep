class TwoSum:

    def __init__(self):
        self.nums = defaultdict(int)

    def add(self, number: int) -> None:
        self.nums[number] += 1

    def find(self, value: int) -> bool:
        for k, v in self.nums.items():
            diff = value - k
            if diff == k:
                if v > 1:
                    return True
            elif diff in self.nums:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)