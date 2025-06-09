class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        sorted_graph = []
        
        adjacency_list = defaultdict(list)
        in_degrees = {i: 0 for i in range(1, len(nums)+1)}
        
        for s in sequences:
            for i in range(1, len(s)):
                parent, child = s[i - 1], s[i]
                adjacency_list[parent].append(child)
                in_degrees[child] += 1
        
        if len(in_degrees) != len(nums):
            return False
        
        sources = [k for k in in_degrees if in_degrees[k] == 0]
        
        while sources:
            if len(sources) > 1:
                return False
            if sources[0] != nums[len(sorted_graph)]:
                return False
            
            node = sources.pop(0)
            sorted_graph.append(node)
            
            for child in adjacency_list[node]:
                in_degrees[child] -= 1
                
                if in_degrees[child] == 0:
                    sources.append(child)
                    
        return len(sorted_graph) == len(nums)