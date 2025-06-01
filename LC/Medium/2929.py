class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        
        for c in range(max(0, n - 2 * limit), min(n, limit) + 1):
            candies_left = n - c
            min_first_child = max(0, candies_left - limit)
            max_first_child = min(candies_left, limit)
            ans += max_first_child - min_first_child + 1
        return ans