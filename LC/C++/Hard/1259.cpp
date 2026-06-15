class Solution {
public:
    int numberOfWays(int numPeople) {
        int MOD = 1e9 + 7;
        int handshakes = numPeople / 2;
        std::vector<int> dp(handshakes + 1);
        dp[0] = 1;

        for (size_t m{1}; m <= handshakes; ++m) {
            for (size_t i{}; i < m; ++i) {
                dp[m] = (dp[m] + (long long)dp[i] * dp[m - 1 - i]) % MOD;
            }
        }

        return dp[handshakes]; 
    }
};