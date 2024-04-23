class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]: 
        if n == 0:
            return []
        
        if n == 1:
            return [0]
        
        in_degrees = defaultdict(int)
        adjacency_list = defaultdict(list)
        
        for n1, n2 in edges:
            adjacency_list[n1].append(n2)
            adjacency_list[n2].append(n1)
            in_degrees[n1] += 1
            in_degrees[n2] += 1
        
        leaves = [node for node in in_degrees if in_degrees[node]==1]

        count = n
        while count > 2:
            leaves_size = len(leaves)
            count -= leaves_size
            
            for i in range(leaves_size):
                node = leaves.pop(0)

                for child in adjacency_list[node]:
                    in_degrees[child] -= 1
                    if in_degrees[child] == 1:
                        leaves.append(child)
                    
        return leaves
