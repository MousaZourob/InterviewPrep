class Solution {
    std::vector<std::pair<int, int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
public:
    int getFood(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        std::queue<std::tuple<int, int, int>> q{};
        std::vector<std::vector<bool>> visited(m, std::vector<bool>(n, false));
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == '*') {
                    q.emplace(0, i, j);
                    visited[i][j] = true;
                }
            }
        }

        while (!q.empty()) {
            auto [dist, r, c] = q.front();
            q.pop();

            if (grid[r][c] == '#') return dist;

            for (auto& [x, y] : dirs) {
                int nr = r + x;
                int nc = c + y;

                if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] == 'X' || visited[nr][nc]) continue;

                q.emplace(dist + 1, nr, nc);
                visited[nr][nc] = true;
            }
        }
        return -1;
    }
};