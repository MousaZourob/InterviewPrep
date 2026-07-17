class Solution {
public:
    int minSizeSubarray(vector<int>& nums, int target) {
        long long sum = 0;
        for (auto num : nums) sum += num;

        long long q = target / sum;
        long long rem = target % sum;

        size_t n = nums.size();
        if (rem == 0) {
            return q * n;
        }

        size_t l = 0;
        long long ans = INT_MAX;
        long long curr = 0;
        for (size_t r{}; r < n * 2; ++r) {
            curr += nums[r % n];
            while (curr > rem) {
                curr -= nums[l % n];
                ++l;
            }
            if (curr == rem) {
                ans = std::min(ans, static_cast<long long>(q * n + r - l + 1));
            }
        }

        return ans != INT_MAX ? ans : -1;
    }
};