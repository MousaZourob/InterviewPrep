class LRUCache {
public:
    LRUCache(int capacity) : capacity_(capacity) {}

    int get(int key) {
        auto it = cache_.find(key);
        if (it == cache_.end()) return -1;

        nodes_.splice(nodes_.begin(), nodes_, it->second);
        return it->second->second;
    }

    void put(int key, int value) {
        auto it = cache_.find(key);

        if (it != cache_.end()) {
            it->second->second = value;
            nodes_.splice(nodes_.begin(), nodes_, it->second);
        } else {
            if (nodes_.size() == capacity_) {
                int oldKey = nodes_.back().first;
                cache_.erase(oldKey);
                nodes_.pop_back();
            }
            nodes_.emplace_front(key, value);
            cache_[key] = nodes_.begin();
        }
    }

private:
    int capacity_;
    std::list<std::pair<int,int>> nodes_;
    std::unordered_map<int, std::list<std::pair<int,int>>::iterator> cache_;
};
