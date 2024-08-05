class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)
        
        for s in arr:
            if count[s] == 1:
                k -= 1
            
            if k == 0:
                return s
        
        return ""
