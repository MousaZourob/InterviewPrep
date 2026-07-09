class Solution {
    static constexpr long long MOD = 1e9 + 7;

public:
    vector<int> sumAndMultiply(string s, vector<vector<int>>& queries) {
        int n = s.size();
        std::vector<int> pow10(n + 1, 1);
        for (size_t i{1}; i < n + 1; ++i) {
            pow10[i] = (1LL * pow10[i - 1] * 10) % MOD;
        }
        std::vector<int> sum(n + 1);
        std::vector<int> x(n + 1);
        std::vector<int> count(n + 1);

        for (size_t i{}; i < n; ++i) {
            int digit = s[i] - '0';
            sum[i + 1] = sum[i] + digit;
            x[i + 1] = digit > 0 ? (1LL * x[i] * 10 + digit) % MOD : x[i];
            count[i + 1] = count[i] + (digit > 0); 
        }
        
        int m = queries.size();
        std::vector<int> ans(m);
        for (size_t i{}; i < m; ++i) {
            int l = queries[i][0];
            int r = queries[i][1] + 1;

            int length = count[r] - count[l];
            long long val = (x[r] - 1LL * x[l] * pow10[length] % MOD + MOD) % MOD;
            ans[i] = val * (sum[r] - sum[l]) % MOD;
        }

        return ans;
    }
};