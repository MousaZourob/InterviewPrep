class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        routes = {}
        
        for source, dest in paths:
            routes[source] = dest
            
        source = paths[0][0]
        dest = None
        
        while source in routes:
            dest = routes[source]
            source = dest
        
        return dest