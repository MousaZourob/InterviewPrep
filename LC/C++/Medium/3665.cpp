class Solution {
    static constexpr int MOD = 1e9 + 7;
    int m_ = 0;
    int n_ = 0;
    std::vector<std::vector<std::array<int, 2>>> cache_;

    int dfs(vector<vector<int>>& grid, int r, int c, int dir) {
        if (r >= m_ || c >= n_) return 0;
        if (r == m_ - 1 && c == n_ - 1) return 1;

        int& res = cache_[r][c][dir];
        if (res != -1) return res;

        if (grid[r][c] == 1) {
            int nextDir = 1 - dir;
            return res = nextDir == 0 
                ? dfs(grid, r, c + 1, nextDir)
                : dfs(grid, r + 1, c, nextDir);
        }
        
        long long right = dfs(grid, r, c + 1, 0);
        long long down = dfs(grid, r + 1, c, 1);

        return res = (right + down) % MOD;
    }

public:
    int uniquePaths(vector<vector<int>>& grid) {
        m_ = grid.size();
        n_ = grid[0].size();

        cache_.assign(m_, std::vector<std::array<int, 2>>(n_, {-1, -1}));

        return dfs(grid, 0, 0, 0);
    }
};