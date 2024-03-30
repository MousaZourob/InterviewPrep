class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def mostK(K):
            ans = 0
            count = defaultdict(int)
            window_start = 0

            for window_end in range(len(nums)):
                count[nums[window_end]] += 1

                while len(count) > K:
                    count[nums[window_start]] -= 1
                    if count[nums[window_start]] == 0:
                        del count[nums[window_start]]
                    window_start += 1

                ans += window_end - window_start + 1

            return ans
        
        return mostK(k) - mostK(k-1)