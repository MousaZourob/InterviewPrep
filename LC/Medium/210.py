class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sorted_graph = []
        
        adjacency_list = defaultdict(list)
        in_degrees = {i: 0 for i in range(numCourses)}
        
        for course, prerequisite in prerequisites:
            adjacency_list[prerequisite].append(course)
            in_degrees[course] += 1
        
        sources = [k for k in in_degrees if in_degrees[k]==0]
        
        while sources:
            prerequisite = sources.pop(0)
            sorted_graph.append(prerequisite)
            
            for course in adjacency_list[prerequisite]:
                in_degrees[course] -= 1
                if in_degrees[course] == 0:
                    sources.append(course)

        if numCourses == len(sorted_graph):
            return sorted_graph
        else:
            return []