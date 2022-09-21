class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        even_sum = 0
        
        for num in nums:
            even_sum += num if num % 2 == 0 else 0
        
        for val, i in queries: 
            if nums[i] % 2 == 0:
                even_sum -= nums[i]

            nums[i] += val
            
            if nums[i] % 2 == 0:
                even_sum += nums[i]
            
            
            ans.append(even_sum)
                
        return ans