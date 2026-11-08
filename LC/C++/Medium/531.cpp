class Solution {
public:
    int findLonelyPixel(vector<vector<char>>& picture) {
        int m = picture.size();
        int n = picture[0].size();

        std::vector<int> rows(m);
        std::vector<int> cols(n);

        for (int i = 0; i < picture.size(); ++i) {
            for (int j = 0; j < picture[i].size(); ++j) {
                if (picture[i][j] == 'B') {
                    rows[i]++;
                    cols[j]++;
                }
            }
        }

        int ans = 0;
        for (int i = 0; i < picture.size(); ++i) {
            for (int j = 0; j < picture[i].size(); ++j) {
                if (picture[i][j] == 'B') {
                    if (rows[i] == 1 && cols[j] == 1) {
                        ans++;
                    }
                }
            }
        }
        

        return ans;
    }
};