class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        ans = [0] * n
        
        window_start = 1
        window_end = k
        
        if k < 0:
            window_start = n + k
            window_end = n - 1
            
        window_sum = 0
        for i in range(window_start, window_end + 1):
            window_sum += code[i]
            
        for i in range(n):
            ans[i] = window_sum
            window_sum -= code[window_start % n]
            window_sum += code[(window_end + 1) % n]
            
            window_start += 1
            window_end += 1
            
        return ans