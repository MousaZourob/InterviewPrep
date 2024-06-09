class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        prefix = 0
        count = [1] + [0] * k
        for num in nums:
            prefix = (prefix + num) % k
            ans += count[prefix]
            count[prefix] += 1
            
        return ans