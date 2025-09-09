class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        left, right = 0, 0
        rounds = 0

        while n > 0:
            temp = n%10
            n = n//10

            if temp <= 1 and n > 0:
                temp += 10
                n -= 1

            remain = temp%2
            left += (temp//2)*10**rounds
            right += (temp//2+remain)*10**rounds
            rounds += 1
        
        return [left, right]
