class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        n = 10
        ans = []
        d_low = len("%i" % low)
        d_high = len("%i" % high)
        sample = "123456789"  
        
        for length in range(d_low, d_high + 1):
            for start in range(n - length):
                num = int(sample[start: start + length])
                if num >= low and num <= high:
                    ans.append(num)
        
        return ans