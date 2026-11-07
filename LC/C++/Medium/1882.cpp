class Solution {
    using Server = std::tuple<int, int>;
    using Busy = std::tuple<long long, int, int>;
public:
    vector<int> assignTasks(vector<int>& servers, vector<int>& tasks) {
        std::priority_queue<
            Server,
            std::vector<Server>,
            std::greater<>
        > available;

        std::priority_queue<
            Busy,
            std::vector<Busy>,
            std::greater<>
        > busy;

        for (size_t i{}; i < servers.size(); ++i) {
            available.push({servers[i], i});
        }

        std::vector<int> ans{};
        long long currTime = 0;
        for (size_t i{}; i < tasks.size(); ++i) {
            currTime = std::max(currTime, (long long)i);
            // move task from busy to available
            while (!busy.empty()) {
                auto [finishTime, priority, id] = busy.top();
                if (currTime >= finishTime) {
                    available.emplace(priority, id);
                    busy.pop();
                } else {
                    break;
                }
            }

            // assign server and put in busy
            if (!available.empty()) {
                auto [priority, id] = available.top();
                available.pop();

                busy.emplace(currTime + tasks[i], priority, id);
                
                ans.push_back(id);
            } else {
                currTime = busy.empty() ? currTime + 1 : std::get<0>(busy.top());
                --i;
            }
        }

        return ans;
    }
};