class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        l, r = 0, len(num) - 1
        rotated = {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}
        
        while l <= r:
            if num[l] not in rotated or rotated[num[l]] != num[r]:
                return False
            l += 1 
            r -= 1
        
        return True