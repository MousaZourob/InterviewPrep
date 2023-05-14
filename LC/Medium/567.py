class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if Counter(s1) == Counter(s2):
            return True
        window_start = 0
        
        for window_end in range(len(s2)):
            if window_end - window_start + 1 == len(s1):
                if Counter(s1) == Counter(s2[window_start:window_end+1]):
                    return True
            
            if window_end - window_start + 2 > len(s1):
                window_start += 1
            
        return False
        