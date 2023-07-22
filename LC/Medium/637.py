class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = {}
        lis, ans = 0, 0
        
        for i in range(len(nums) - 1, -1, -1):
            max_lis, max_count = 1, 1
            
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length, count = dp[j]
                    if length + 1 > max_lis:
                        max_lis, max_count = length + 1, count
                    elif length + 1 == max_lis:
                        max_count += count
                
            if max_lis > lis:
                lis, ans = max_lis, max_count
            elif max_lis == lis:
                ans += max_count

            dp[i] = [max_lis, max_count]
        
        return ans