class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
    
        for i in range(n):
            if arr[i] == arr[i + n // 4]:
                return arr[i]
        
        return -1