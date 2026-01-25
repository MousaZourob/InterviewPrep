#include <algorithm>
#include <vector>
#include <limits>

class Solution {
public:
    int minimumDifference(std::vector<int>& nums, int k) {
        int ans = std::numeric_limits<int>::max();
        std::sort(nums.begin(), nums.end());

        for (int windowEnd = 0; windowEnd < nums.size() - k + 1; ++windowEnd) {
            ans = std::min(ans, nums[windowEnd + k - 1] - nums[windowEnd]);
        }

        return ans;
    }
};
