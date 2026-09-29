class Solution {
    int m;
    int n;
    std::vector<std::vector<std::vector<int>>> cache_;
public:
    bool dfs(vector<vector<char>>& grid, int x, int y, int parenCount) {
        if (x >= m || y >= n) {
            return false;
        }

        parenCount += grid[x][y] == '(' ? 1 : -1;


        if (parenCount < 0) return false;
        else if (parenCount == 0 && x == m - 1 && y == n - 1) return true;

        if (cache_[x][y][parenCount] != -1) {
            return cache_[x][y][parenCount];
        }

        return cache_[x][y][parenCount] = dfs(grid, x + 1, y, parenCount) || dfs(grid, x, y + 1, parenCount);
    }

    bool hasValidPath(vector<vector<char>>& grid) {
        m = grid.size();
        n = grid[0].size();

        if ((m + n - 1) % 2 != 0) return false;
        
        cache_.assign(m, std::vector<std::vector<int>>(
            n, std::vector<int>(m + n, -1)
        ));

        return dfs(grid, 0, 0, 0);
    }
};