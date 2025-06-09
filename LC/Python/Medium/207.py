class Solution:
    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        in_degree = [0] * n
        
        for parent, child in prerequisites:
            adj_list[parent].append(child)
            in_degree[child] += 1
            
        sources = [i for i in range(n) if in_degree[i] == 0]
        
        courses = 0
        while sources:
            curr = sources.pop(0)
            courses += 1
            
            for neighbour in adj_list[curr]:
                in_degree[neighbour] -= 1
                if in_degree[neighbour] == 0:
                    sources.append(neighbour)
        print(courses)
        return courses == n