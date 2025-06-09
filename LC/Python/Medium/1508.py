class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []

        for i in range(n):
            pre_sum = 0
            for j in range(i, n):
                pre_sum += nums[j]
                sums.append(pre_sum)
        
        sums.sort()
        return sum(sums[left-1:right]) % (10**9 + 7)