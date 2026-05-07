class Solution {
public:
    vector<int> maxValue(vector<int>& nums) {
        int n = nums.size();

        std::vector<int> suffixMin(n);
        suffixMin[n - 1] = nums[n - 1];

        for (int i = n - 2; i >= 0; i--) {
            suffixMin[i] = min(nums[i], suffixMin[i + 1]);
        }

        std::vector<int> ans(n);

        int start = 0;
        int prefixMax = nums[0];
        int blockMax = nums[0];

        for (int i = 0; i < n; ++i) {
            prefixMax = max(prefixMax, nums[i]);
            blockMax = max(blockMax, nums[i]);

            bool cut = (i == n - 1) || (prefixMax <= suffixMin[i+1]);
            if (cut) {
                for (int j = start; j <= i; j++) {
                    ans[j] = blockMax;
                }

                start = i + 1;
                if (start < n) {
                    blockMax = nums[start];
                }
            }
        }

        return ans;
    }
};