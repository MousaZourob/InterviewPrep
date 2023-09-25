class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        missing = 0
        for c in s:
            missing -= ord(c)
        for c in t:
            missing += ord(c)
        
        return chr(missing)
            