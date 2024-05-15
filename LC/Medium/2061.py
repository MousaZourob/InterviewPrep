class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        rows = len(room)
        cols = len(room[0])
        curr_dir = 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        r = 0
        c = 0
        visited = set()
        room[r][c] = -1
        ans = 1
        
        while (r, c, curr_dir) not in visited:
            visited.add((r, c, curr_dir))
            n_r = r + dirs[curr_dir][0]
            n_c = c + dirs[curr_dir][1]
            
            if 0 <= n_r < rows and 0 <= n_c < cols and room[n_r][n_c] != 1:
                r, c = n_r, n_c
                if room[r][c] == 0:
                    ans += 1
                    room[r][c] = -1
            else:
                curr_dir = (curr_dir + 1) % 4
        return ans