class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        ans = [0] * (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                digit = int(num1[i]) * int(num2[j])
                ans[i+j] += digit
                ans[i+j+1] += (ans[i+j] // 10)
                ans[i+j] = ans[i+j] % 10

        while ans[-1] == 0:
            ans.pop()
        
        return ''.join(str(digit) for digit in ans[::-1])