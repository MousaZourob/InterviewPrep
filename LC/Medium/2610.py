class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        count = [0] * (len(nums) + 1)
        ans = []
        
        for n in nums:
            if count[n] >= len(ans):
                ans.append([])
            ans[count[n]].append(n)
            count[n] += 1

        return ans
