class Solution:
    def fractionAddition(self, expression: str) -> str:
        expression = expression.replace("+", " +").replace("-", " -").split()
        
        ans_num = 0
        ans_den = 1
        for expression in expression:
            num, den = expression.split('/')
            num = int(num)
            den = int(den)
            
            ans_num = ans_num*den + num*ans_den
            ans_den *= den
        
        ans = [ans_num, ans_den]
        while ans_den: 
            ans_num, ans_den = ans_den, ans_num%ans_den
       
        return str(ans[0] // ans_num) + "/" + str(ans[1] // ans_num)
