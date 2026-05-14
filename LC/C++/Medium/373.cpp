class Solution {
public:
    vector<vector<int>> kSmallestPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        using T = tuple<int, int, int>;
        int n1 = nums1.size(), n2 = nums2.size();

        std::vector<std::vector<int>> ans;
        ans.reserve(k);

        std::priority_queue<T, std::vector<T>, std::greater<T>> pq;
        for (int i = 0; i < std::min(k, n1); ++i) {
            pq.emplace(nums1[i] + nums2[0], i, 0);
        }
        
        while (k-- > 0 && !pq.empty()) {
            auto [currSum, i, j] = pq.top();
            pq.pop();

            ans.push_back({nums1[i], nums2[j]});

            if (j + 1 < n2) {
                pq.emplace(nums1[i] + nums2[j + 1], i, j + 1);
            } 
        }

        return ans;
    }
};