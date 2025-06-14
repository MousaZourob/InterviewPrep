class Solution {
public:
    bool count_pairs(const vector<int>& nums, int p, int guess) {
        int i = 0;
        int c = 0; 
        int n = nums.size();

        while (i < n - 1) {
            if (nums[i + 1] - nums[i] <= guess) {
                i += 2;
                c += 1;
            } else {
                i += 1;
            }
            if (c >= p) {
                return true;
            }
        }
        return false;
    }

    int minimizeMax(vector<int>& nums, int p) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int ans = 0;

        int l = 0;
        int r = nums[n - 1] - nums[0];

        while (l <= r) {
            int m = l + (r - l) / 2;
            if (count_pairs(nums, p, m)) {
                ans = m;
                r = m - 1;
            } else {
                l = m + 1;
            }
        }

        return ans;
    }
};