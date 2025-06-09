class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        max_i = -1
        swap_i = -1
        swap_j = -1
        
        for i in range(len(num) - 1, -1, -1):
            if max_i == -1 or num[max_i] < num[i]:
                max_i = i
            elif num[max_i] > num[i]:
                swap_i = i
                swap_j = max_i

        if swap_i != -1:
            num[swap_i], num[swap_j] = num[swap_j], num[swap_i]
        
        return int(''.join(num))
