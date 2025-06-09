class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_valid(guess):
            count = 0
            for r in ranks:
                count += int(sqrt(guess/r))
                if count >= cars:
                    break
            return count >= cars

        l = 1
        r = max(ranks)*cars*cars
        ans = r
        while l <= r:
            m = (r - l) // 2 + l
            if is_valid(m):
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans
