class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if (nums1.size() > nums2.size()) {
            std::swap(nums1, nums2);
        }

        int m = nums1.size();
        int n = nums2.size();
        int total = m + n;
        int half = total / 2;

        int l = 0;
        int r = m - 1;

        while (true) {
            int i = l + (int)std::floor((r - l) / 2.0);
            int j = half - i - 2; 
        
            int n1left = i >= 0 ? nums1[i] : INT_MIN;
            int n1right = i + 1 < m ? nums1[i + 1] : INT_MAX;

            int n2left = j >= 0 ? nums2[j] : INT_MIN;
            int n2right = j + 1 < n ? nums2[j + 1] : INT_MAX;

            if (n1left <= n2right && n2left <= n1right) {
                if (total % 2 == 1) {
                    return std::min(n1right, n2right);
                } else {
                    return (std::max(n1left, n2left) + std::min(n1right, n2right)) / 2.0;
                }
            } else {
                if (n1left > n2right) {
                    r = i - 1;
                } else {
                    l = i + 1;
                }
            }
        }

        return -1;
    }
};