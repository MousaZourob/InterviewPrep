class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int maxE = std::numeric_limits<int>::min(), maxI = -1, minE = std::numeric_limits<int>::max(), minI = -1;
        int n = nums.size();

        for (int i = 0; i < n; ++i) {
            if (maxE < nums[i]) {
                maxE = nums[i];
                maxI = i;
            }

            if (minE > nums[i]) {
                minE = nums[i];
                minI = i;
            }
        }

        return min({
            max(minI, maxI) + 1,
            n - min(minI, maxI),
            minI + 1 + n - maxI,
            maxI + 1 + n - minI
        });
    }
};