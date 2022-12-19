class Solution:
    def checkValidString(self, s: str) -> bool:
        min_left = 0
        max_left = 0
        for c in s:
            min_left += 1 if c == '(' else -1
            max_left += 1 if c != ')' else -1
            
            if max_left < 0: 
                break
            
            min_left = max(min_left, 0)

        return min_left == 0