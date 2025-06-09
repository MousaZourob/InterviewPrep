class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        ranges = defaultdict(int)
        
        for i, r in lights:
            ranges[i-r] += 1
            ranges[i+r+1] -= 1
        curr, ans, max_val = 0, -1, -inf
        for i, val in sorted(ranges.items()):
            curr += val
            if curr > max_val:
                ans = i
                max_val = curr
        
        return ans