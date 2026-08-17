class Solution {
    int n;
    std::vector<std::vector<int>> cache;

    int dfs(vector<int>& sv, int l, int r) {
        if (cache[l][r] != -1) return cache[l][r];
        if (l >= r) return 0;

        int ans = 0;
        int total = 0;
        for (int i = l; i <= r; ++i) {
            total += sv[i];
        }
        int lTotal = 0;

        for (int i = l; i < r; ++i) {
            lTotal += sv[i];
            int rTotal = total - lTotal;

            if (lTotal < rTotal) {
                ans = std::max(ans, dfs(sv, l, i) + lTotal);
            } else if (lTotal > rTotal) {
                ans = std::max(ans, dfs(sv, i+1, r) + rTotal);
            } else {
                ans = std::max({ans, dfs(sv, l, i) + lTotal, dfs(sv, i+1, r) + rTotal});
            }
        }

        return cache[l][r] = ans;
    }

public:
    int stoneGameV(vector<int>& stoneValue) {
        n = stoneValue.size();
        cache.resize(n, std::vector<int>(n, -1));

        return dfs(stoneValue, 0, n - 1);
    }
};