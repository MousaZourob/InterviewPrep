class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        count = [0] * k
        
        for num in arr:
            count[num % k] += 1

        if count[0] % 2 != 0:
            return False
        
        for i in range(1, k // 2 + 1):
            if count[i] != count[k - i]:
                return False
        
        return True