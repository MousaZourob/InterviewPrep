class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            
            l, r = i + 1, len(nums)-1
            
            while l < r:
                total = num + nums[l] + nums[r]
                if total == 0:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        
        return ans