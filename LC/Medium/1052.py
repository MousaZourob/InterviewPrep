class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        ans = 0
        max_grump = 0
        grump = 0
        
        for i in range(len(customers)):
            if i >= minutes and grumpy[i - minutes] == 1:
                grump -= customers[i-minutes]  
            
            if grumpy[i]:
                grump += customers[i]
            else:
                ans += customers[i]

            max_grump = max(max_grump, grump)
        
        return ans + max_grump