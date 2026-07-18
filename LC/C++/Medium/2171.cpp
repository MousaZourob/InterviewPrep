class Solution {
public:
    long long minimumRemoval(vector<int>& beans) {
        std::sort(beans.begin(), beans.end());
        long long  sum = 0;
        for (int bean : beans) sum += bean;

        long long  removed = 0;
        for (int i = 0; i < beans.size(); ++i) {
            removed = std::max(removed, (long long)(beans[i] * (beans.size() - i)));
        }

        return sum - removed;
    }
};