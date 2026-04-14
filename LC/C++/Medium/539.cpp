class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<bool> seen(1440, false);
        for (string& time : timePoints) {
            int minutes = stoi(time.substr(0, 2)) * 60 + stoi(time.substr(3, 5));
            if (seen[minutes]) return 0;
            seen[minutes] = true;
        }

        int first = -1, prev = -1, ans = INT_MAX;
        for (int i = 0; i < 24*60; ++i) {
            if (seen[i]) {
                if (first == -1) first = i;
                
                if (prev != -1) ans = min(ans, i - prev);
                prev = i;
            }
        }

        return min(ans, 24*60 - prev + first);
    }
};