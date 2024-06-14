class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        max_n = max(nums)
        ans = 0
        
        count = [0]*(n+max_n+1)
        
        for num in nums:
            count[num] += 1
        print(count)
        for i in range(n+max_n+1):
            if count[i] <= 1:
                continue

            ans += count[i] - 1
            count[i+1] += count[i] - 1
            count[i] = 1
            
        return ans