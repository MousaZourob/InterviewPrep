class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int ans = 0;
        int l = 0;
        bool seen = false;
        
        for (int r = 0; r < nums.size(); ++r) {
            while (nums[r] == 0 && seen) {
                seen = nums[l];
                l++;
            }

            if (nums[r] == 0) seen = true;

            ans = std::max(ans, r - l + 1);
        }

        return ans;
    }
};