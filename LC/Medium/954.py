class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        vals = Counter(arr)
        arr = sorted(arr, key = abs)

        for num in arr:
            if vals[num] == 0:
                continue
            
            if vals[num*2] == 0:
                return False
            
            vals[num] -= 1
            vals[num*2] -= 1
            
        return True