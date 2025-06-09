class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False] * len(rooms)
        visited[0] = True
        queue = [rooms[0]]
        
        while queue:
            keys = queue.pop(0)
            for key in keys:
                if not visited[key]:
                    visited[key] = True
                    queue.append(rooms[key])

        return all(visited)