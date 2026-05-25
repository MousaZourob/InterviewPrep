class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int ans = 0;
        
        int currMin = std::numeric_limits<int>::max();
        for (int price : prices) {
            if (price > currMin) {
                ans += price - currMin;
            }
            currMin = price;
        }

        return ans;
    }
};