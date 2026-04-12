class Solution {
public:
    vector<int> killProcess(vector<int>& pid, vector<int>& ppid, int kill) {
        std::unordered_map<int, vector<int>> adjList{};
        for (int i = 0; i < ppid.size(); ++i) {
            adjList[ppid[i]].push_back(pid[i]);
        }
        
        // build tree
        std::queue<int> q{};
        q.emplace(kill);
        vector<int> ans;

        while (!q.empty()) {
            int curr = q.front();
            q.pop();
            ans.push_back(curr);
            
            for (int n : adjList[curr]) {
                q.emplace(n);
            }
        }

        return ans;
    }
};