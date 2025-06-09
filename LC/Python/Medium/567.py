class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        window_start = 0
        
        curr = defaultdict(int)
        for window_end in range(len(s2)):
            curr[s2[window_end]] += 1
            if curr == count:
                return True
            
            while window_end - window_start + 2 > len(s1):
                curr[s2[window_start]] -= 1
                if curr[s2[window_start]] == 0:
                    del curr[s2[window_start]]
                window_start += 1
        
        return False