class Solution {
public:
    int minMoves2(vector<int>& nums) {
        int ans = 0;

        std::ranges::sort(nums);
        int target = nums[nums.size() / 2];

        for (int num : nums) {
            ans += abs(target - num);
        }
        
        return ans;   
    }
};
