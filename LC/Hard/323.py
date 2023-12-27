class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj_list = defaultdict(list)
        
        for source, dest in tickets:
            adj_list[source].append(dest)
        
        ans=[]
        
        def dfs(source):
            while adj_list[source]:
                dfs(adj_list[source].pop(0))

            ans.append(source)
            
        dfs("JFK")
        return reversed(ans)
    