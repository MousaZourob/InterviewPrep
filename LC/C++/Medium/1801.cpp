class Solution {
public:
    int getNumberOfBacklogOrders(vector<vector<int>>& orders) {
        std::priority_queue<std::pair<int, int>> buys{};
        std::priority_queue<std::pair<int,int>, std::vector<pair<int,int>>, std::greater<std::pair<int,int>>> sells;
        for (auto& order : orders) {
            int price = order[0], amount = order[1], t = order[2];
            if (t == 0) {
                buys.push({price, amount});
            } else {
                sells.push({price, amount});
            } 

            while (!buys.empty() && !sells.empty() && sells.top().first <= buys.top().first) {
                auto [bp, ba] = buys.top();  buys.pop();
                auto [sp, sa] = sells.top(); sells.pop();

                int quantity = min(ba, sa);
                
                ba -= quantity;
                sa -= quantity;
                
                if (ba > 0) buys.push({bp, ba});
                if (sa > 0) sells.push({sp, sa});
            }
        }

        int result = 0;
        const int MOD = 1e9 + 7;
        
        while (!buys.empty()) {
            result = (result + buys.top().second) % MOD;
            buys.pop();
        }
        while (!sells.empty()) {
            result = (result + sells.top().second) % MOD;
            sells.pop();
        }
        return result;
    }
};