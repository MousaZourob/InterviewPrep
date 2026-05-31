class Solution {
public:
    bool asteroidsDestroyed(int mass, vector<int>& asteroids) {
        std::sort(asteroids.begin(), asteroids.end());
        long long m = mass;
        for (long long ast : asteroids) {
            if (ast > m) {
                return false;
            }
            m += ast;
        }

        return true;
    }
};