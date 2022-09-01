class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        ans = []
        min_diff = float("inf")
        
        for i in range(len(arr) - 1):
            diff = arr[i+1] - arr[i]
            
            if diff < min_diff:
                min_diff = diff
                ans = []
                
            if diff == min_diff:
                ans.append([arr[i], arr[i+1]])
        
        return ans