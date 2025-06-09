class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 == 1:
            return []
        
        ans = []
        count = Counter(changed)
        changed.sort()
        
        for num in changed:
            if num == 0 and count[num] >= 2:
                count[num] -= 2
                ans.append(num)
            elif num > 0 and count[num] and count[num*2]:
                count[num] -= 1
                count[num*2] -= 1
                ans.append(num)
            
        return ans if len(ans) == len(changed) // 2 else []