"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        visited = {}
        q = [node]
        visited[node] = Node(node.val, [])
        
        while q:
            curr = q.pop(0)
            
            for neighbour in curr.neighbors:
                if neighbour not in visited:
                    visited[neighbour] = Node(neighbour.val, [])
                    q.append(neighbour)
                
                visited[curr].neighbors.append(visited[neighbour])

        return visited[node]