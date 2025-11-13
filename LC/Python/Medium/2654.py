class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ones = nums.count(1)
        if ones:
            return n - ones

        ans = inf

        for i in range(n):
            curr = nums[i]
            for j in range(i + 1, n):
                curr = gcd(curr, nums[j])

                if curr == 1:
                    ans = min(ans, j - i)
        
        if ans == inf:
            return -1

        return ans + n - 1
