from collections import defaultdict, deque

class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        online = set()
        components = {}
        component_heaps = defaultdict(list)

        def dfs(station, group_id):
            if station in online:
                return
            online.add(station)
            components[station] = group_id
            heappush(component_heaps[group_id], station)

            for curr in graph[station]:
                dfs(curr, group_id)

        for curr in range(1, c + 1):
            dfs(curr, curr)

        ans = []
        for q, node in queries:
            if q == 1:
                if node in online:
                    ans.append(node)
                    continue
                group_id = components[node]
                component_heap = component_heaps[group_id]
                while component_heap and component_heap[0] not in online:
                    heappop(component_heap)
                
                if component_heap:
                    ans.append(component_heap[0])
                else:
                    ans.append(-1)
            else:
                online.discard(node)

        return ans
