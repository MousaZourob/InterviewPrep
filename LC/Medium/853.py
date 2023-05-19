class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted(zip(position, speed), reverse = True)
        ans = 0
        prev = -inf
        
        for p, s in pairs:
            curr = (target - p)/s
            if curr > prev:
                ans += 1
                prev = curr

        return ans