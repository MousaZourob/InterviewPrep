class Solution {
public:
    bool checkValidString(string s) {
        int minLeft = 0;
        int maxLeft = 0;

        for (auto& c : s) {
            minLeft += c == '(' ? 1 : -1;
            maxLeft += c != ')' ? 1 : -1;

            if (maxLeft < 0) {
                return 0;
            }

            minLeft = std::max(minLeft, 0);
        }

        return minLeft == 0;
    }
};