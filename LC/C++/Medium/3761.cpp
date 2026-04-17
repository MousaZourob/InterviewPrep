class Solution {
public:
    int reverse(int x) {
        int res = 0;
        while (x) {
            res = res * 10 + x % 10;
            x /= 10;
        }

        return res;
    }
    int minMirrorPairDistance(vector<int>& nums) {
        std::unordered_map<int, int> seen;

        int ans = INT_MAX;
        for (int i = 0; i < nums.size(); ++i) {
            if (seen.count(nums[i])) {
                ans = min(ans, i - seen[nums[i]]);
            }

            int complement = reverse(nums[i]);
            seen[complement] = i;
        }
    
        return ans != INT_MAX ? ans : -1;
    }
};