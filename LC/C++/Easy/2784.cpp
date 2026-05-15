class Solution {
public:
    bool isGood(vector<int>& nums) {
        int n = nums.size();
        std::vector<int> count(n, 0);
        for (auto num : nums) {
            if (num >= n) {
                return false;
            } else if (num < n-1 && count[num-1] == 1) {
                return false;
            } else if (num == n-1 && count[num-1] == 2) {
                return false;
            }
            count[num-1]++;
        }

        return true;
    }
};