class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        int n = s.size();
        queue<int> q;
        q.push(0);

        int farthest = 1;

        while (!q.empty()) {
            int curr = q.front();
            q.pop();

            int start = max(curr + minJump, farthest);
            int end = min(curr + maxJump, n - 1);

            for (int i = start; i <= end; ++i) {
                if (s[i] == '1') continue;
                if (i == n - 1) return true;
                
                q.push(i);
            }

            farthest = max(farthest, end + 1);
        }

        return n == 1;
    }
};