class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        std::map<int, vector<int>> indices{};

        for (size_t i{}; i < arr.size(); ++i) {
            indices[arr[i]].push_back(i);
        }

        int rank = 1;
        for (auto& [k, v] : indices) {
            for (size_t i : v) {
                arr[i] = rank;
            }
            rank++;
        }
        return arr;
    }
};