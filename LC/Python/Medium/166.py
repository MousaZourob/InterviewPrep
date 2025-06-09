class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        
        ans = []
        if (numerator < 0) != (denominator < 0):
            ans.append("-")
            
        dividend = abs(numerator)
        divisor = abs(denominator)
        
        ans.append(str(dividend // divisor))
        remainder = dividend % divisor
        if remainder == 0:
            return ''.join(ans)
        
        ans.append('.')
        lookup = {}
        while remainder != 0:
            if remainder in lookup:
                ans.insert(lookup[remainder], "(")
                ans.append(")")
                break
            lookup[remainder] = len(ans)
            remainder *= 10
            ans.append(str(remainder // divisor))
            remainder %= divisor
        
        return ''.join(ans)