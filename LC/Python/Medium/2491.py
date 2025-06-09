class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        if n == 2:
            return skill[0] * skill[1]
        
        total_skill = sum(skill)
        
        if total_skill % (n//2):
            return -1
        target = total_skill // (n//2)
        
        diff_count = Counter(skill)
        
        ans = 0
        for num in skill:
            diff = target - num
            if diff_count[diff] <= 0:
                return -1
            
            ans += num * diff
            diff_count[diff] -= 1
            
        return ans // 2