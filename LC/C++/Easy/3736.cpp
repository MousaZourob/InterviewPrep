class Solution {
public:
    int minMoves(vector<int>& nums) {
        int ans = 0;
        int max = std::ranges::max(nums);

        for (auto& num : nums) {
            ans += max - num;
        }

        return ans;
    }
};