class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        vector<int> dp(k * 2, INT_MIN);

        for (int price : prices) {
            dp[0] = max(dp[0], - price);

            for (int i = 1; i < k * 2; ++i) {
                if (i % 2 == 0) {
                    dp[i] = max(dp[i], dp[i - 1] - price);
                } else {
                    dp[i] = max(dp[i], dp[i - 1] + price);
                }
            }
        }
        
        return max(0, dp.back());
    }
};