class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)

        lis = [0] * n
        sub = []

        for i, num in enumerate(nums):
            pos = bisect_left(sub, num)
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
            lis[i] = pos + 1

        lds = [0] * n
        sub = []
        for i, num in enumerate(reversed(nums)):
            pos = bisect_left(sub, num)
            if pos == len(sub):
                sub.append(num)
            else:
                sub[pos] = num
            lds[n - 1 - i] = pos + 1

        ans = n
        for i in range(1, n-1):
            if lis[i] > 1 and lds[i] > 1:
                ans = min(ans, n - lis[i] - lds[i] + 1)
            
        return ans