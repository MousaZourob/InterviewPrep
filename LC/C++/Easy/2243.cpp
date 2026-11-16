class Solution {
    std::string numSum(std::string s) {
        int sum = 0;
        for (char c : s) {
            sum += c - '0';
        }

        return std::to_string(sum);
    }

public:
    string digitSum(string s, int k) {
        while (s.size() > k) {
            int i = 0;
            std::string curr = "";
            std::string newS = "";
            while (i < s.size()) {
                curr += s[i++];

                if (i % k == 0 || i >= s.size()) {
                    newS += numSum(curr);
                    curr = "";
                }
            }
            s = newS;
        }

        return s;
    }
};