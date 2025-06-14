#include <vector>

class Solution {
public:
    std::vector<int> lexicalOrder(int n) {
        std::vector<int> ans;
        int curr = 1;

        for (int i = 0; i < n; i++) {
            ans.push_back(curr);
            if (curr * 10 <= n) {
                curr *= 10;
            } else {
                while (curr % 10 == 9 || curr >= n) {
                    curr = curr / 10;
                }
                curr += 1;
            }
        }

        return ans;
    }
};
