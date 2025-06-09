class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        directions = [
            [1, 3],
            [0, 2, 4],
            [1, 5],
            [0, 4],
            [3, 5, 1],
            [4, 2],
        ]
        
        def swap(s, i, j):
            s = list(s)
            s[i], s[j] = s[j], s[i]
            return "".join(s)

        start_state = "".join(str(num) for row in board for num in row)
        target = "123450"
        
        visited = set()
        q = deque([start_state])
        visited.add(start_state)
        
        ans = 0
        while q:
            for _ in range(len(q)):
                state = q.popleft()
                
                if state == target:
                    return ans

                zero_index = state.index("0")
                for new_index in directions[zero_index]:
                    new_state = swap(state, zero_index, new_index)
                    
                    if new_state in visited:
                        continue
                    
                    q.append(new_state)
                    visited.add(new_state)
                
            ans += 1
                
        return -1