class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        std::sort(nums.begin(), nums.end());
        std::vector<vector<int>> ans;

        for (int i = 0; i < n - 2; ++i) {
            if (i > 0 && nums[i] == nums[i-1]) continue;

            int l = i + 1;
            int r = n - 1;
            
            while (l < r) {
                int curr = nums[i] + nums[l] + nums[r];

                if (curr == 0) {
                    ans.push_back({nums[i], nums[l], nums[r]});
                    ++l;
                    while (l < r && nums[l] == nums[l - 1]) {
                        ++l;
                    }
                } else if (curr > 0) {
                    --r;
                } else {
                    ++l;
                }
            }
        }

        return ans;
    }
};