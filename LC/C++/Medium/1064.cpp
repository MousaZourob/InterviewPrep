class Solution {
public:
    int fixedPoint(vector<int>& arr) {
        int ans = INT_MAX;

        for (size_t i = 0; i < arr.size(); ++i) {
            if (arr[i] == i) {
                ans = min(ans, arr[i]);
            }
        }

        return ans != INT_MAX ? ans : -1;
    }
};