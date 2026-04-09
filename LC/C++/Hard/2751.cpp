class Solution {
public:
    vector<int> survivedRobotsHealths(vector<int>& positions, vector<int>& healths, string directions) {
        int n = positions.size();
        vector<int> posToIndex(n);
        for (int i = 0; i < n; ++i) {
            posToIndex[i] = i;
        }
        sort(posToIndex.begin(), posToIndex.end(),
             [&](int lhs, int rhs) { return positions[lhs] < positions[rhs]; });

        std::stack<int> stack;
        for (int& i : posToIndex) {
            if (directions[i] == 'R') {
                stack.push(i);
            } else {
                while (!stack.empty() && directions[stack.top()] == 'R' && healths[i] > 0) {
                    int i2 = stack.top();
                    stack.pop();

                    if (healths[i] > healths[i2]) {
                        healths[i]--;
                        healths[i2] = 0;
                    } else if (healths[i] < healths[i2]) {
                        healths[i] = 0;
                        healths[i2]--;
                        stack.push(i2);
                    } else {
                        healths[i] = 0;
                        healths[i2] = 0;
                    }
                }
            }
        }


        vector<int> ans;
        for (int i = 0; i < healths.size(); ++i) {
            if (healths[i] > 0) ans.push_back(healths[i]);
        }

        return ans;
    }
};