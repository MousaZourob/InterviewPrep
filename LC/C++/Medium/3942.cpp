class Solution {
public:
    int minOperations(vector<int>& nums) {
        int n = nums.size();

        int start = std::ranges::find(nums, 0) - nums.begin();
        bool asc = true;
        bool desc = true;

        for (size_t i = 1; i < n; ++i) {
            int val = nums[(start + i) % n];
            if (val != i) asc = false;
            if (val != n - i) desc = false;

            if (!asc & !desc) return -1;
        }

        if (asc) {
            return std::min(start, n - start + 2);
        }
        return min(n - start, start + 2);
    }
};