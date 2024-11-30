class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        adj_list = defaultdict(deque)
        in_degree = defaultdict(int)
        out_degree = defaultdict(int)
        
        for x, y in pairs:
            adj_list[x].append(y)
            out_degree[x] += 1
            in_degree[y] += 1
                
        stat_node = pairs[0][0]
        for node in out_degree:
            if out_degree[node] == in_degree[node] + 1:
                stat_node = node
                break
        
        order = []
        stack = [stat_node]
        
        while stack:
            curr = stack[-1]
            if adj_list[curr]:
                next_node = adj_list[curr].popleft()
                stack.append(next_node)
            else:
                order.append(curr)
                stack.pop()
            
        order.reverse()
        
        ans = []
        for i in range(1, len(order)):
            ans.append([order[i - 1], order[i]])
        
        return ans
