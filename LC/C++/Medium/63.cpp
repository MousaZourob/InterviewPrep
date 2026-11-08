class Solution {
    int m;
    int n;
    std::vector<std::vector<int>> cache;
    int dfs(vector<vector<int>>& grid, int i, int j) {
        if (i >= m || j >= n || grid[i][j] == 1) {
            return 0;
        }
        
        if (i == m - 1 && j == n - 1) {
            return 1;
        }

        if (cache[i][j] != -1) {
            return cache[i][j];
        }

        return cache[i][j] = dfs(grid, i + 1, j) + dfs(grid, i, j+ 1);
    }
public:
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        m = obstacleGrid.size();
        n = obstacleGrid[0].size();
        cache.resize(m, std::vector<int>(n, -1));

        return dfs(obstacleGrid, 0, 0);
    }
};