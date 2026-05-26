class RandomizedSet {
    std::vector<int> data_;
    std::unordered_map<int, int> index_;

public:
    RandomizedSet() {}
    
    bool insert(int val) {
        if (index_.contains(val)) return false;

        index_[val] = data_.size();
        data_.push_back(val);

        return true;
    }
    
    bool remove(int val) {
        if (!index_.contains(val)) return false;

        int last = data_.back();
        int index = index_[val];

        data_[index] = last;
        index_[last] = index;

        data_.pop_back();
        index_.erase(val);

        return true;
    }
    
    int getRandom() {
        return data_[rand() % data_.size()];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */