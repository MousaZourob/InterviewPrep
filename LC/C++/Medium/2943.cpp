class Solution {
public:
    int maximizeSquareHoleArea(int n, int m, vector<int>& hBars, vector<int>& vBars) {
        std::sort(hBars.begin(), hBars.end());
        std::sort(vBars.begin(), vBars.end());
        int hCurr = 1;
        int hMax = 1;
        int vCurr = 1;
        int vMax = 1;

        for (int i = 1; i < hBars.size(); i++) {
            if (hBars[i] - 1 == hBars[i-1]) {
                hCurr += 1;
            } else {
                hCurr = 1;
            }
            hMax = max(hMax, hCurr);
        }

        for (int i = 1; i < vBars.size(); i++) {
            if (vBars[i] - 1 == vBars[i-1]) {
                vCurr += 1;
            } else {
                vCurr = 1;
            }
            vMax = max(vMax, vCurr);
        }
        int side = min(vMax, hMax) + 1;

        return side * side;
    }
};
