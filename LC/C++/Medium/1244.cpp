class Leaderboard {
    std::unordered_map<int, int> players_;
    std::map<int, int, std::greater<int>> scores_;
public:
    Leaderboard() {}
    
    void addScore(int playerId, int score) {
        int oldScore = players_[playerId];

        if (oldScore > 0) {
            scores_[oldScore]--;
            if (scores_[oldScore] == 0) scores_.erase(oldScore);
        }

        int newScore = oldScore + score;
        players_[playerId] = newScore;
        scores_[newScore]++;
    }
    
    int top(int K) {
        int res = 0;

        for (auto& [score, count] : scores_) {
            int take = min(K, count);
            res += score * take;
            K -= take;

            if (K == 0) break;
        }

        return res;
    }
    
    void reset(int playerId) {
        int oldScore = players_[playerId];

        scores_[oldScore]--;
        if (scores_[oldScore] == 0) scores_.erase(oldScore);

        players_.erase(playerId);
    }
};

/**
 * Your Leaderboard object will be instantiated and called as such:
 * Leaderboard* obj = new Leaderboard();
 * obj->addScore(playerId,score);
 * int param_2 = obj->top(K);
 * obj->reset(playerId);
 */