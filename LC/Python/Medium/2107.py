class Solution:
    def shareCandies(self, candies: List[int], k: int) -> int:
        ans = 0
        seen = Counter(candies)
        for window_end in range(len(candies)):
            seen[candies[window_end]] -= 1 
            
            if seen[candies[window_end]] == 0: 
                del seen[candies[window_end]]
            
            if window_end >= k: 
                seen[candies[window_end - k]] += 1 
            
            if window_end >= k - 1: 
                ans = max(ans, len(seen))

        return ans 