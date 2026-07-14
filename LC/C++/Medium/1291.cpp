class Solution {
public:
    vector<int> sequentialDigits(int low, int high) {
        std::string sample = "123456789";
        int n = 10;
        std::vector<int> ans{};
        for (size_t length = to_string(low).size(); length < to_string(high).size() + 1; ++length) {
            for (size_t i = 0; i < n - length; ++i) {
                int num = stoi(sample.substr(i, length));
                if (num >= low && num <= high) {
                    ans.push_back(num);
                }
            }
        }

        return ans;
    }
};