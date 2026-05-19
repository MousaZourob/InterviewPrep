class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        std::vector<int> ans(n, 0);
        std::stack<std::pair<int, int>> stack;
        for (auto& log : logs) {
            std:stringstream ss(log);
            string stId, status, stTime;

            getline(ss, stId, ':');
            getline(ss, status, ':');
            getline(ss, stTime, ':');
        
            int id = stoi(stId);
            int time = stoi(stTime);

            if (status == "start") {
                stack.push({id, time});
            } else {
                int timeTaken = time - stack.top().second + 1;
                ans[id] += timeTaken;
                stack.pop();

                if (!stack.empty()) {
                    ans[stack.top().first] -= timeTaken;
                }
            }
        }
        return ans;
    }
};