class HitCounter {
private:
    std::vector<pair<int, int>> cache;

public:
    HitCounter() {
        cache.resize(300);
        for (size_t i = 0; i < 300; ++i) {
            cache[i] = {i + 1, 0};
        }
    }
    
    void hit(int timestamp) {
        int i = timestamp % 300;
        if (cache[i].first == timestamp) {
            cache[i].second++;
        } else {
            cache[i] = {timestamp, 1};
        }
    }
    
    int getHits(int timestamp) {
        int ans = 0;

        for (auto& [time, hits] : cache) {
            if (hits > 0 && timestamp - time < 300) {
                ans += hits;
            }
        }

        return ans;
    }
};

/**
 * Your HitCounter object will be instantiated and called as such:
 * HitCounter* obj = new HitCounter();
 * obj->hit(timestamp);
 * int param_2 = obj->getHits(timestamp);
 */