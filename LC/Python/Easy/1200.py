class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        min_element = min(arr)
        max_element = max(arr)
        shift = -min_element
        sort = [0] * (max_element - min_element + 1)
        
        for num in arr:
            sort[num + shift] = 1
            
        min_diff = max_element - min_element
        prev = 0
        ans = []
        
        for i in range(1, max_element + shift + 1):
            if sort[i] == 0:
                continue
            
            diff = i - prev
            
            if diff < min_diff:
                min_diff = diff
                ans = []
            
            if diff == min_diff:
                ans.append([prev - shift, i - shift])
            prev = i
        
        return ans