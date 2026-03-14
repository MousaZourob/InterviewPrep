class Solution {
    std::string curr;
    int k;
    std::string result;
    std::vector<char> happy{'a','b','c'};

    void dfs(int n) {
        if (!result.empty()) return;

        if (curr.size() == n) {
            if (--k == 0) {
                result = curr;
            }
            return;
        }

        for (char& c : happy) {
            if (curr.empty() || curr.back() != c) {
                curr.push_back(c);
                dfs(n);
                curr.pop_back();
            }
        }
    }

public:
    string getHappyString(int n, int k) {
        this->k = k;
        dfs(n);
        return result;
    }
};