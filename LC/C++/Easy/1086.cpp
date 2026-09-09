class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        std::map<int, priority_queue<int, vector<int>, greater<int>>> studentScores{};

        for (auto& i : items) {
            auto& pq = studentScores[i[0]];
            pq.push(i[1]);
            if (pq.size() > 5) pq.pop();
        }

        std::vector<std::vector<int>> ans{};
        for (auto& [id, pq] : studentScores) {
            int res = 0;
            while (!pq.empty()) {
                res += pq.top();
                pq.pop();
            }

            ans.push_back({id, res / 5});
        }

        return ans;
    }
};