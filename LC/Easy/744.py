class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if letters[0] > target or letters[-1] <= target:
            return letters[0]
        
        l, r = 0, len(letters) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            
            if ord(letters[mid]) > ord(target):
                r = mid - 1
            elif ord(letters[mid]) <= ord(target):
                l = mid + 1

        return letters[l]