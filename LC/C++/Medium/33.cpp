class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();

        auto find = [&](int l, int r) -> int {
            while (l <= r) {
                int m = l + (r - l) / 2;
                if (nums[m] == target) {
                    return m;
                } else if (nums[m] < target) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }

            return -1;
        };

        int l = 0;
        int r = n - 1;

        while (l <= r) {
            int m = l + (r - l) / 2;
            if (nums.back() < nums[m]) {
                l = m + 1;
            } else {
                r = m - 1;
            }
        }

        return max(find(0, l - 1), find(l, n - 1));
    }
};