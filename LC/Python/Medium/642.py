class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_num = arrays[0][0]
        max_num = arrays[0][-1]
        ans = 0
        
        for arr in arrays[1:]:
            ans = max(ans, abs(arr[-1] - min_num), abs(max_num - arr[0]))
            max_num = max(max_num, arr[-1])
            min_num = min(min_num, arr[0])
        
        return ans