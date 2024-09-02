class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        k = k % sum(chalk)
        index = 0
        
        while k > 0:
            if k < chalk[index]:
                break
            k -= chalk[index]
            index = (index + 1) % n
            
        return index