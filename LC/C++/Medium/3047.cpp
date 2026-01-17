class Solution {
public:
    long long largestSquareArea(vector<vector<int>>& bottomLeft, vector<vector<int>>& topRight) {
        int n = bottomLeft.size();
        long long maxSide = 0;
 
        for (int i = 0; i < n; ++i) {
            int lx1 = bottomLeft[i][0];
            int ly1 = bottomLeft[i][1];
            int rx1 = topRight[i][0];
            int ry1 = topRight[i][1];

            for (int j = i + 1; j < n; ++j) {
                int lx2 = bottomLeft[j][0];
                int ly2 = bottomLeft[j][1];
                int rx2 = topRight[j][0];
                int ry2 = topRight[j][1];

                long long w = min(rx1, rx2) - max(lx1, lx2);
                long long h = min(ry1, ry2) - max(ly1, ly2);
                if (w > 0 && h > 0) {
                    maxSide = max(maxSide, min(w,h));
                }
            }
        }

        return maxSide * maxSide;
    }
};