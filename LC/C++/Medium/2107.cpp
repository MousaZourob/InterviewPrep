class Solution {
public:
    int shareCandies(vector<int>& candies, int k) {
        int ans{0};
        std::unordered_map<int, int> window{};
        for (auto x : candies) window[x]++;

        for (int i = 0; i < candies.size(); ++i) {
            if (--window[candies[i]] == 0) {
                window.erase(candies[i]);
            }

            if (i >= k) {
                window[candies[i - k]]++;
            }

            if (i >= k - 1) {
                ans = std::max(ans, (int)window.size());
            }
        }

        return ans;
    }
};