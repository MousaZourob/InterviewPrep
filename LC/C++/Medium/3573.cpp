class Solution {
    vector<vector<vector<long long>>> cache_;
public:
    long long dfs(vector<int>& prices, int i, int k, int state) {
        if (i == prices.size()) {
            return state == 0 ? 0 : LLONG_MIN / 4;
        }
        if (cache_[i][k][state] != LLONG_MIN) {
            return cache_[i][k][state];
        }

        int p = prices[i];
        long long res = dfs(prices, i + 1, k, state);
        if (k > 0 && state == 0) {
            res = max(res, dfs(prices, i + 1, k - 1, 1) - p);
            res = max(res, dfs(prices, i + 1, k - 1, 2) + p);
        } else if (state == 1) {
            res = max(res, dfs(prices, i + 1, k, 0) + p);
        } else {
            res = max(res, dfs(prices, i + 1, k, 0) - p);
        }

        return cache_[i][k][state] = res;
    }

    long long maximumProfit(vector<int>& prices, int k) {
        cache_.assign(
            prices.size(),
            vector<vector<long long>>(
                k + 1,
                {LLONG_MIN, LLONG_MIN, LLONG_MIN}
            )
        );
        return dfs(prices, 0, k, 0);
    }
};