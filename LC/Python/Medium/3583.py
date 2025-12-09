class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        freqPrev = Counter()
        freqNext = Counter(nums)
        count = 0
        
        for num in nums:
            freqNext[num] -= 1
            count += freqPrev[num*2] * freqNext[num*2]
            freqPrev[num] += 1

        return count % 10**7