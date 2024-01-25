class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ans = [0] * k
        user_uam = {}
        
        for id, time in logs:
            if id not in user_uam:
                user_uam[id] = set()
            user_uam[id].add(time)
            
        for value in user_uam.values():
            ans[len(value) - 1] += 1
        
        return ans