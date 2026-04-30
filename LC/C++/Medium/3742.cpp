class Solution {
public:
    int maxPathScore(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();

        vector dp(m, vector(n, vector<int>(k + 1, INT_MIN)));

        dp[0][0][min(grid[0][0], 1)] = grid[0][0];

        for (int x = 0; x < m; x++) {
            for (int y = 0; y < n; y++) {
                for (int c = 0; c <= k; c++) {
                    if (dp[x][y][c] == INT_MIN) continue;
                    
                    int currCost = min(grid[x][y], 1);

                    if (x + 1 < m) {
                        int nc = c + min(grid[x + 1][y], 1);
                        if (nc <= k) {
                            dp[x + 1][y][nc] = max(
                                dp[x + 1][y][nc], 
                                dp[x][y][c] + grid[x + 1][y]
                            );
                        }
                    }

                    if (y + 1 < n) {
                        int nc = c + min(grid[x][y + 1], 1);
                        if (nc <= k) {
                            dp[x][y + 1][nc] = max(
                                dp[x][y + 1][nc],
                                dp[x][y][c] + grid[x][y + 1]
                            );
                        }
                    }
                }
            }
        }

        int ans = INT_MIN;
        for (int c = 0; c <= k; c++) {
            ans = max(ans, dp[m-1][n-1][c]);
        }

        return ans == INT_MIN ? -1 : ans;
    }
};