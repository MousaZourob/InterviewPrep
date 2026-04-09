class Solution {
    using state = std::tuple<int, int, int>;
    int m = 0;
    int n = 0;
    vector<vector<vector<int>>> cache;
public:
    int dfs(vector<vector<int>>& coins, int x, int y, int d) {
        if (x >= m || y >= n) return INT_MIN; 
        if (x == m - 1 && y == n - 1) {
            if (coins[x][y] < 0 && d > 0) return 0;
            return coins[x][y];
        }

        if (cache[x][y][d] != INT_MIN) return cache[x][y][d];

        int notDestroy = max(dfs(coins, x + 1, y, d), 
                            dfs(coins, x, y + 1, d)) + coins[x][y];
        int destroy = INT_MIN;
        if (d > 0 && coins[x][y] < 0) {
            destroy = max(dfs(coins, x + 1, y, d - 1), 
                        dfs(coins, x, y + 1, d - 1)); 
        }

        int res = max(notDestroy, destroy);
        cache[x][y][d] = res;
        return res;
    }

    int maximumAmount(vector<vector<int>>& coins) {
        m = coins.size();
        n = coins[0].size();
        cache.assign(m, vector<vector<int>>(n, vector<int>(3, INT_MIN)));
        return dfs(coins, 0, 0, 2);
    }
};