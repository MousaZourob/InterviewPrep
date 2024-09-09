class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        count = Counter(nums)
        
        for key, v in count.items():
            if k == 0:
                if v > 1:
                    ans += 1
            else:
                if key - k in count:
                    ans += 1
        
        return ans