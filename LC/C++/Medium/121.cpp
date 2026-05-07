class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        int minPrice = prices[0];

        for (int n : prices) {
            minPrice = min(minPrice, n);
            ans = max(ans, n - minPrice);
        }

        return ans;
    }
};