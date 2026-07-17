class Solution {
public:
    vector<int> relativeSortArray(vector<int>& arr1, vector<int>& arr2) {
        std::vector<int> count(1001,0);
        for (int num : arr1) count[num]++;

        std::vector<int> ans{};
        for (int i = 0; i < arr2.size(); ++i) {
            int curr = arr2[i];
            for (int j = 0; j < count[curr]; ++j) {
                ans.push_back(curr);
            }
            count[curr] = 0;
        }

        for (int i = 0; i < count.size(); ++i) {
            for (int j = 0; j < count[i]; ++j) {
                ans.push_back(i);
            }
        }

        return ans;
    }
};