class Solution {
public:
    bool uniformArray(vector<int>& nums1) {
        int minNum = nums1[0];
        bool hasOdd = minNum & 1;
        for (auto num : nums1) {
            minNum = std::min(minNum, num);
            hasOdd |= num & 1;
        }

        return (minNum & 1) || !hasOdd;
    }
};