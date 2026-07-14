class Solution {
public:
    long long numOfSubsequences(string s) {
        using ll = long long;
        ll countL{};
        ll countLC{};
        ll countLCT{};

        for (auto& c : s) {
            if (c == 'L') countL++;
            if (c == 'C') countLC += countL;
            if (c == 'T') countLCT += countLC;
        }
        
        ll gainL{countLCT};
        ll countC{};
        for (auto& c : s) {
            if (c == 'C') countC++;
            if (c == 'T') gainL += countC;
        }

        ll countT{};
        for (auto& c : s) {
            if (c == 'T') countT++;
        }

        countL = 0;
        for (auto& c : s) {
            if (c == 'L') countL++;
            if (c == 'T') countT--;
            best = std::max(best, countL * countT);
        }
        ll gainC = countLCT + best;

        long long gainT(countLCT + countLC);

        return std::max({gainL, gainC, gainT});
    }
};