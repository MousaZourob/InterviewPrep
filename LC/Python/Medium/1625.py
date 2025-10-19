class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:    
        def add(curr):
            chars = list(curr)
            for i in range(1, len(chars), 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            return ''.join(chars)

        def rotate(curr):
            return curr[b:] + curr[:b]

        q = deque([s])
        ans = s
        visited = set([s])
        while q:
            curr = q.popleft()
            added = add(curr)
            rotated = rotate(curr)

            for guess in (added, rotated):
                if guess not in visited:
                    ans = min(ans, guess)
                    visited.add(guess)
                    q.append(guess)

        return ans