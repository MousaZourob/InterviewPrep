class Solution {
public:
    int maxArea(vector<int>& height) {
        int n = height.size();
        int l = 0;
        int r = n - 1;
        int ans = 0;

        while (l < r) {
            int curr_h = min(height[l], height[r]);
            int curr_w = r - l;
            ans = max(ans, curr_h * curr_w);

            if (height[l] < height[r]) {
                l += 1;
            } else {
                r -= 1;
            }

        }

        return ans;
    }
};