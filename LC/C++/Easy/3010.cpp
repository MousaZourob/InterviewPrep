class Solution {
public:
    int minimumCost(vector<int>& nums) {
        int firstMin = std::numeric_limits<int>::max();
        int secondMin = std::numeric_limits<int>::max();

        for (size_t i = 1; i < nums.size(); ++i) {
            if (nums[i] < firstMin) {
                secondMin = firstMin;
                firstMin = nums[i];
            } else if (nums[i] < secondMin) {
                secondMin = nums[i];
            }
        }

        return nums[0] + firstMin + secondMin;
    }
};