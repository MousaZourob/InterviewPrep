class Solution {
public:
    int minMoves(vector<int>& nums) {
        int ans = 0;

        int min = std::ranges::min(nums);
        for (auto& num : nums) {
            ans += num - min;
        }

        return ans;
    }
};