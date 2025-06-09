class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        count = [defaultdict(int) for _ in range(n)]
        
        
        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                res = 0
                
                if diff in count[j]:
                    res = count[j][diff]
                
                count[i][diff] += res + 1
                ans += res
        
        return ans