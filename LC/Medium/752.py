class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:
            return -1
        
        ans = 0
        
        q = ['0000']
        visited.add('0000')
        
        while q:
            for _ in range(len(q)):
                curr = q.pop(0)

                if curr == target:
                    return ans

                for i in range(4):
                    for op in [-1, 1]:
                        neighbour = curr[:i] + str((int(curr[i]) + op) % 10) + curr[i+1:]
                        if neighbour not in visited:
                            visited.add(neighbour)
                            q.append(neighbour)
            ans += 1
        
        return -1