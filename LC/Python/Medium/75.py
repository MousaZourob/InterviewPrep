class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3

        for num in nums:
            count[num] += 1
        
        i_nums = 0

        for i in range(3):
            while count[i] > 0:
                count[i] -= 1
                nums[i_nums] = i
                i_nums += 1    
        