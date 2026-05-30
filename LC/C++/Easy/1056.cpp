class Solution {
public:
    bool confusingNumber(int n) {
        int res = 0;
        int copy = n;
        std::unordered_map<int, int> inversion = {{0, 0}, {1, 1}, {6, 9}, {8, 8}, {9, 6}};

        while (copy > 0) {
            int curr = copy % 10;
            if (!inversion.contains(curr)) {
                return false;
            }

            res = res * 10 + inversion[curr];
            copy /= 10;
        }
        cout << res;
        return res != n;
    }
};