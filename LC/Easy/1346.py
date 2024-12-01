class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        s = set(arr)
        zero_count = 0
        
        for n in arr:
            if n == 0:
                zero_count += 1
            if zero_count >= 2 or (n != 0 and n * 2 in s):
                return True
        
        return False