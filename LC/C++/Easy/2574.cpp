class Solution {
public:
    vector<int> leftRightDifference(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> left(n);
        std::vector<int> right(n);

        for (int i = 1; i < n; ++i) {
            left[i] = nums[i - 1] + left[i - 1];
            right[n - i - 1] = nums[n - i] + right[n - i];
        }

        for (int i = 0; i < n; ++i) {
            left[i] = abs(left[i] - right[i]);
        }

        return left;
    }
};