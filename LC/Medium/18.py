class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i + 1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                    
                l, r = j + 1, len(nums) - 1
                
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]

                    if total == target:
                        ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif total > target:
                        r -= 1
                    else: 
                        l += 1

        return ans
                