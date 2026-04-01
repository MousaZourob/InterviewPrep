class MRUQueue {
    int totalElements_;
    const int BUCKET_SIZE_;
    std::vector<std::vector<int>> queue_;
    std::vector<int> index_;
public:
    MRUQueue(int n) : totalElements_(n), BUCKET_SIZE_(sqrt(n)) {
        queue_.reserve(n);
        for (int i = 1; i <= n; ++i) {
            int bucketIndex = (i - 1) / BUCKET_SIZE_;
            if (bucketIndex == queue_.size()) {
                queue_.push_back({});
                index_.push_back(i);
            }
            queue_.back().push_back(i);
        }
    }
    
    int fetch(int k) {
        int bucketI = upper_bound(index_.begin(), index_.end(), k) - index_.begin() - 1;
        int element = queue_[bucketI][k - index_[bucketI]];
        queue_[bucketI].erase(queue_[bucketI].begin() + (k - index_[bucketI]));
        for (int i = bucketI + 1; i < index_.size(); ++i) {
            --index_[i];
        }

        if (queue_.back().size() >= BUCKET_SIZE_) {
            queue_.push_back({});
            index_.push_back(totalElements_);
        }
        queue_.back().push_back(element);

        if (queue_[bucketI].empty()) {
            queue_.erase(queue_.begin() + bucketI);
            index_.erase(index_.begin() + bucketI);
        }

        return element;
    }
};

/**
 * Your MRUQueue object will be instantiated and called as such:
 * MRUQueue* obj = new MRUQueue(n);
 * int param_1 = obj->fetch(k);
 */