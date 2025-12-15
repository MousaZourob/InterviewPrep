class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        ans = 0

        count = 0
        prev = inf

        for num in prices:
            if prev - num == 1:
                count += 1
                ans += count
                prev = num
            else:
                count = 1
                ans += count
                prev = num

        return ans
