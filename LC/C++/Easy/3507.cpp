class Solution {
public:
    int minimumPairRemoval(std::vector<int>& nums) {
        int ans = 0;

        while (nums.size() > 1) {
            bool ascending = true;
            int index = 0;
            int minSum = std::numeric_limits<int>::max();

            for (int i = 0; i < nums.size() - 1; ++i) {
                int sum = nums[i] + nums[i + 1];

                if (nums[i] > nums[i + 1]) {
                    ascending = false;
                }

                if (sum < minSum) {
                    minSum = sum;
                    index = i;
                }
            }

            if (ascending) {
                break;
            }

            ans++;
            nums[index] = minSum;
            nums.erase(nums.begin() + index + 1);
        }

        return ans;
    }
};