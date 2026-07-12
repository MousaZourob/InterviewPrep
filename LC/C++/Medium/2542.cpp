class Solution {
public:
    long long maxScore(vector<int>& nums1, vector<int>& nums2, int k) {
        long long  ans = 0;
        
        std::vector<std::pair<long long, int>> pairs{};
        for (size_t i{}; i < nums1.size(); ++i) {
            pairs.push_back({nums1[i], nums2[i]});
        }

        std::sort(pairs.begin(), pairs.end(),
            [] (const auto& a, const auto& b) {
                return a.second > b.second;
            });
        

        std::priority_queue<long long, std::vector<long long>, std::greater<long long>> pq;
        long long total = 0;
        for (auto& [a, b] : pairs) {
            pq.push(a);
            total += a;

            if (pq.size() > k) {
                total -= pq.top();
                pq.pop();
            } 
            if (pq.size() == k) {
                ans = max(ans, total * b);
            }
        }

        return ans;
    }
};