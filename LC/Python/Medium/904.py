class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        window_start = 0
        max_sum = 0
        curr_fruits = {}
        
        for window_end in range(len(fruits)):
            curr_fruits[fruits[window_end]] = curr_fruits.get(fruits[window_end], 0) + 1
            
            while len(curr_fruits) > 2:
                curr_fruits[fruits[window_start]] -= 1
                if curr_fruits[fruits[window_start]] == 0:
                    del curr_fruits[fruits[window_start]]
                window_start += 1
            
            max_sum = max(max_sum, window_end - window_start + 1)
    
        return max_sum