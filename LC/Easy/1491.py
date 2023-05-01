class Solution:
    def average(self, salary: List[int]) -> float:
        curr_min = inf
        curr_max = -inf
        total = 0
        
        for num in salary:
            total += num
            curr_min = min(num, curr_min)
            curr_max = max(num, curr_max)
            
        return (total-curr_max-curr_min) / (len(salary)-2)