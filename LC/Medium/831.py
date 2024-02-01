class Solution:
    def maskEmail(self, s: str) -> str:
        first_part, second_part = s.split('@')
        masked = first_part[0] + '*' * 5 + first_part[-1]
        
        return masked.lower() + '@' + second_part.lower()
    
    def maskPhone(self, s: str) -> str:
        code = ["", "+*-", "+**-", "+***-"]

        s = "".join(i for i in s if i.isdigit())
        return code[(len(s) - 10)] + "***-***-" + s[-4:] 
    
    def maskPII(self, s: str) -> str:
        if '@' in s:
            return self.maskEmail(s)
        else:
            return self.maskPhone(s)
        