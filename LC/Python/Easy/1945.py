class Solution:
    def getLucky(self, s: str, k: int) -> int:
        def sum_digits(n):
            res = 0
            while n:
                res += n % 10 
                n //= 10
            
            return res

        ans = 0
        
        for c in s:
            digit = ord(c) - ord('a') + 1
            ans = ans * (10 ** (int(math.log10(digit))+1))
            ans += digit
        
        prev = ans
        for _ in range(k):
            ans = sum_digits(ans)
            if ans == prev:
                break
            prev = ans
        
        return ans