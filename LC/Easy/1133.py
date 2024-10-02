class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        ans = -1
        for k, v in count.items():
            if k > ans and v == 1:
                ans = k
        
        return ans