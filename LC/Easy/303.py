class NumArray:

    def __init__(self, nums: List[int]):
        prefix = 0
        self.prefix = []
        
        for num in nums:
            prefix += num
            self.prefix.append(prefix)
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        ans = self.prefix[right]
        
        if left != 0:
            ans -= self.prefix[left - 1]
            
        return ans


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)