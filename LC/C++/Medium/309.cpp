class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int sold = std::numeric_limits<int>::min();
        int held = std::numeric_limits<int>::min();
        int reset = 0;

        for (int price : prices) {
            int temp = sold;
            sold = held + price;
            held = max(held, reset - price);
            reset = max(reset, temp);
        }

        return std::max(sold, reset);
    }
};