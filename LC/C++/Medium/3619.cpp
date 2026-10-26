class Solution {
    int m_;
    int n_;
    std::vector<std::pair<int, int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};

    long long dfs(int r, int c, vector<vector<int>>& grid) {
        long long res = grid[r][c];

        grid[r][c] = -1;
        for (auto& [x, y] : dirs) {
            int nr = r + x;
            int nc = c + y;

            if (nr < 0 || nr >= m_ || nc < 0 || nc >= n_ || grid[nr][nc] <= 0) {
                continue;
            }

            res += dfs(nr, nc, grid);
        }
        
        return res;
    }
public:
    int countIslands(vector<vector<int>>& grid, int k) {
        int ans = 0;
        m_ = grid.size();
        n_ = grid[0].size();

        for (int i = 0; i < m_; ++i) {
            for (int j = 0; j < n_; ++j) {
                if (grid[i][j] > 0 && dfs(i, j, grid) % k == 0) {
                    ans += 1;
                }
            }
        }

        return ans;
    }
};