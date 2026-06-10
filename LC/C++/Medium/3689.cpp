class Solution {
public:
    long long maxTotalValue(vector<int>& nums, int k) {
        int min = INT_MAX;
        int max = INT_MIN;
        for (int x : nums) {
            min = std::min(min, x);
            max = std::max(max, x);
        }

        return 1LL * (max - min) * k;
    }
};