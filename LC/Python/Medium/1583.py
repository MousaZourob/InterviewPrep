class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        dd = {}
        for x, y in pairs:
            dd[x] = set(preferences[x][:preferences[x].index(y)])
            dd[y] = set(preferences[y][:preferences[y].index(x)])
        
        print(dd)
        ans = 0
        for x in dd:
            for y in dd[x]:
                if x in dd[y]:
                    ans += 1
                    break
        
        return ans