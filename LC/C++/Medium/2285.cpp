class Solution {
public:
    long long maximumImportance(int n, vector<vector<int>>& roads) {
        std::vector<int> inDegrees(n, 0);
        for (int i = 0; i < roads.size(); ++i) {
            inDegrees[roads[i][0]]++;
            inDegrees[roads[i][1]]++;
        }
        std::sort(inDegrees.begin(), inDegrees.end());

        long long ans = 0;
        for (int i = 0; i < inDegrees.size(); ++i) {
            ans += inDegrees[i]*(i+1LL);
        }

        return ans;
    }
};