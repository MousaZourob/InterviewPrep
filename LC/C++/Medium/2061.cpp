class Solution {
    std::vector<std::vector<int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
public:
    int numberOfCleanRooms(vector<vector<int>>& room) {
        int m = room.size(), n = room[0].size();
        int dirr = 0; 
        int r = 0;
        int c = 0;
        vector<vector<vector<bool>>> visited(
            m, vector<vector<bool>>(n, vector<bool>(4, false))
        );
        room[r][c] = -1;
        int ans = 1;
        while (!visited[r][c][dirr]) {
            visited[r][c][dirr] = true;
            int nr = r + dirs[dirr][0];
            int nc = c + dirs[dirr][1];
            
            if (0 <= nr && nr < m && 0 <= nc && nc < n && room[nr][nc] != 1) {
                r = nr;
                c = nc;
                if (room[r][c] == 0) {
                    room[r][c] = -1;
                    ans++;
                }
            } else {
                dirr = (dirr + 1) % 4;
            }
        }

        return ans;
    }
};