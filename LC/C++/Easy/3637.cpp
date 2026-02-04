class Solution {
public:
    bool isTrionic(vector<int>& nums) {
        int n = nums.size();

        int i = 0;
        while (i < n - 1) {
            if (nums[i] < nums[i + 1]) {
                ++i;
            } else {
                break;
            }
        }
        int p = i;

        while (i < n - 1) {
            if (nums[i] > nums[i + 1]) {
                ++i;
            } else {
                break;
            }
        }
        int q = i;

        while (i < n - 1) {
            if (nums[i] < nums[i + 1]) {
                ++i;
            } else {
                break;
            }
        }

        return (p < q) && (q < i) && (i == n - 1) && p != 0;
    }
};