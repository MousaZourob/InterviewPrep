class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        ans = []

        for k, v in count.items():
            if v > 1:
                ans.append(k)
            if len(ans) > 1:
                return ans

        return ans