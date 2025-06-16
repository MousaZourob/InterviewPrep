class Solution {
public:
    int maximumDifference(vector<int>& nums) {
        int curr_low = INT_MAX;
        int ans = 0;

        for (int num : nums) {
            curr_low = min(curr_low, num);
            ans = max(ans, num - curr_low);
        }

        return ans != 0 ? ans : -1;
    }
};