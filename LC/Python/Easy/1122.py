class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        count = Counter(arr1)
        
        for num in arr2:
            ans += [num] * count[num]
            del count[num]
            
        for k, v in sorted(count.items()):
            ans += [k] * v
        
        return ans