class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = Counter(target)
        
        for num in arr:
            if num not in count:
                return False
            else:
                count[num] -= 1
                if count[num] == 0:
                    del count[num]
        
        return True