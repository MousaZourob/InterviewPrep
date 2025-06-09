class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        count = defaultdict(int)
        max_count = 0
        ans = 0
        
        for num in nums:
            count[num] += 1
            freq = count[num]
            
            if freq > max_count:
                max_count = freq
                ans = freq
            elif freq == max_count:
                ans += freq
        
        return ans