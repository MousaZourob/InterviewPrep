class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        dp = {}
        n = len(locations)
        
        def opt(curr_city, curr_fuel):
            if curr_fuel < 0:
                return 0

            if (curr_city, curr_fuel) in dp:
                return dp[(curr_city, curr_fuel)]

            ans = 0
            if curr_city == finish:
                ans = 1
            
            for next_city in range(n):
                if next_city != curr_city:
                    ans = (ans + opt(next_city, curr_fuel - abs(locations[curr_city] - locations[next_city]))) % (10**9+7)
            
            dp[(curr_city, curr_fuel)] = ans
            return ans
        
        return opt(start, fuel)