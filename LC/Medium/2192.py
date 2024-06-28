class Solution:
    def getAncestors(self, n, edges):
        ans = [set() for _ in range(n)]
        in_degree = [0] * n
        adjacency_list = defaultdict(set)
        for parent, child in edges:
            ans[child].add(parent)
            adjacency_list[parent].add(child)
            in_degree[child] += 1
            
        q = deque([u for u, degree in enumerate(in_degree) if degree == 0])
        while q:
            parent = q.popleft()
            for child in adjacency_list[parent]:
                ans[child].update(ans[parent])
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    q.append(child)

        return [sorted(s) for s in  ans]   