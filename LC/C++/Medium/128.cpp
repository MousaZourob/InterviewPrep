class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        int ans = 0;
        std::unordered_set<int> seen(nums.begin(), nums.end());

        for (auto num : seen) {
            if (!seen.contains(num - 1)) {
                int curr = 1;
                while (seen.contains(num + curr)) {
                    curr++;
                }
                ans = max(ans, curr);
            }
        }

        return ans;
    }
};