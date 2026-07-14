class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;

        int l = 0;
        int r = height.size() - 1;

        int maxLeft = height[l];
        int maxRight = height[r];

        while (l < r) {
            if (height[l] <= height[r]) {
                l++;
                maxLeft = std::max(maxLeft, height[l]);
                ans += maxLeft - height[l];
            } else {
                r--;
                maxRight = std::max(maxRight, height[r]);
                ans += maxRight - height[r];
            }
        }


        return ans;
    }
};