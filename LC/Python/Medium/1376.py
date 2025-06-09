class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj_list = defaultdict(list)
        for i in range(n):
            adj_list[manager[i]].append(i)
        
        ans = 0
        q = [(headID, 0)]
        
        while q:
            i, time = q.pop(0)
            ans = max(ans, time)
            
            for emp in adj_list[i]:
                q.append((emp, time + informTime[i]))
                
        
        return ans