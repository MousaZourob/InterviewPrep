class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();        std::vector<std::pair<int, int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        std::queue<std::pair<int, int>> q;

        int fresh = 0;
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (grid[i][j] == 2) {
                    q.emplace(i, j);
                } else if (grid[i][j] == 1) {
                    fresh++;
                }
            }
        }

        int ans = 0;
        while (!q.empty() && fresh > 0) {
            int qSize = q.size(); 
            while (qSize > 0) {
                auto [r, c] = q.front();
                q.pop();

                for (auto& [x, y] : dirs) {
                    int nr = r + x;
                    int nc = c + y;

                    if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] == 1) {
                        grid[nr][nc] = 0;
                        q.emplace(nr, nc);
                        fresh--;
                    }
                }

                qSize--;
            }
            ans++;
        }

        return fresh == 0 ? ans : -1;
    }
};