class Solution {
public:
    int maxIceCream(vector<int>& costs, int coins) {
        int n = costs.size();
        int m = *std::max_element(costs.begin(), costs.end());
        int ans = 0;

        std::vector<int> freq(m + 1);
        for (auto& cost : costs) {
            freq[cost]++;
        }

        for (int cost = 1; cost <= m; ++cost) {
            if (freq[cost] == 0) continue;
            if (coins < cost) break;

            int count = min(freq[cost], coins / cost);
            coins -= cost * count;
            ans += count;
        }

        return ans;
    }
};