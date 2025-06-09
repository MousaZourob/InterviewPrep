class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curr_pen = min_pen = customers.count('Y')
        ans = 0
        
        for i, c in enumerate(customers):
            if c == 'Y':
                curr_pen -= 1
            else:
                curr_pen += 1
            
            if min_pen > curr_pen:
                min_pen = curr_pen
                ans = i+1
        
        return ans