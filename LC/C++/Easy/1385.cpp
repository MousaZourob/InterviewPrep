class Solution {
public:
    int findTheDistanceValue(vector<int>& arr1, vector<int>& arr2, int d) {
        std::ranges::sort(arr2);
        int ans = 0;
    
        for (auto& num : arr1) {
            auto it = std::lower_bound(arr2.begin(), arr2.end(), num - d);
            if (it == arr2.end() || *it > num + d) ans++;
        }

        return ans;
    }
};