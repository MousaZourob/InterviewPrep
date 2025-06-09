class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        ans = set([0, firstPerson])
        
        adj_list = defaultdict(list)
        visited = [False] * n
        
        for p1, p2, t in meetings:
            adj_list[p1].append((t, p2))
            adj_list[p2].append((t, p1))
        
        heap = []
        heappush(heap, (0, 0))
        heappush(heap, (0, firstPerson))

        while heap:
            time, person = heappop(heap)

            if visited[person]:
                continue
                
            visited[person] = True
            ans.add(person)
            
            for t, next_person in adj_list[person]:
                if not visited[next_person] and t >= time:
                    heappush(heap, (t, next_person))
            
        return ans