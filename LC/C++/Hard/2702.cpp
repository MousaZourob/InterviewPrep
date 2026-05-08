class Solution {
public:
    int minOperations(vector<int>& nums, int x, int y) {
        auto tryOperations = [&](long long k) {
            long long operationsNeeded = 0;
            long long extra = x - y;

            for (int num : nums) {
                long long remaining = num - k * y;

                if (remaining > 0) {
                    operationsNeeded += (remaining + extra - 1) / extra;
                }

                if (operationsNeeded > k) return false;
            }


            return operationsNeeded <= k;
        };
        
        long long l = 0;
        long long r = *std::max_element(nums.begin(), nums.end());

        while (l < r) {
            long long operations = l + (r - l) / 2;

            if (tryOperations(operations)) { 
                r = operations;
            } else {
                l = operations + 1;
            }
        }

        return l;
    }
};