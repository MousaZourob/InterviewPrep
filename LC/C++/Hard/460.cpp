class LFUCache {
    struct Node {
        int key;
        int value;
        int freq;
    };

    int capacity_;
    int minFreq_;

    std::unordered_map<int, std::list<Node>::iterator> cache_;
    std::unordered_map<int, std::list<Node>> freqLists_;

    void touch(std::list<Node>::iterator nodeIt) {
        int key = nodeIt->key;
        int value = nodeIt->value;
        int freq = nodeIt->freq;

        freqLists_[freq].erase(nodeIt);
        
        if (freqLists_[freq].empty()) {
            freqLists_.erase(freq);

            if (minFreq_ == freq) {
                minFreq_++;
            }
        }

        freqLists_[freq + 1].push_front(Node{key, value, freq + 1});
        cache_[key] = freqLists_[freq + 1].begin();
    }
public:
    LFUCache(int capacity) 
        : capacity_(capacity), minFreq_(0) {}
    
    int get(int key) {
        auto it = cache_.find(key);
        if (it == cache_.end()) {
            return -1;
        }

        auto nodeIt = it->second;
        int value = nodeIt->value;

        touch(nodeIt);
        return value;
    }
    
    void put(int key, int value) {
        auto it = cache_.find(key);
        if (it != cache_.end()) {
            auto nodeIt = it->second;
            nodeIt->value = value;
            touch(nodeIt);
            return;
        }

        if (cache_.size() == capacity_) {
            auto& list = freqLists_[minFreq_];

            auto evictIt = std::prev(list.end());
            int evictKey = evictIt->key;

            cache_.erase(evictKey);
            list.erase(evictIt);

            if (list.empty()) {
                freqLists_.erase(minFreq_);
            }
        }

        freqLists_[1].push_front(Node{key, value, 1});
        cache_[key] = freqLists_[1].begin();
        minFreq_ = 1;
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */