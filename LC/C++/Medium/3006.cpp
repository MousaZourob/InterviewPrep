class Solution {
public:
    vector<int> beautifulIndices(string s, string a, string b, int k) {
        std::vector<int> aPos{};
        size_t pos = s.find(a, 0);
        while (pos != string::npos) {
            aPos.push_back(pos);
            pos = s.find(a, pos + 1);
        }

        std::vector<int> bPos{};
        pos = s.find(b, 0);
        while (pos != string::npos) {
            bPos.push_back(pos);
            pos = s.find(b, pos + 1);
        }

        vector<int> ans{};
        for (int a : aPos) {
            auto it = std::lower_bound(bPos.begin(), bPos.end(), a - k);
            if (it != bPos.end() && *it <= a + k) {
                ans.push_back(a);
            }
        }

        return ans;
    }
};