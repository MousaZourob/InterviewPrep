class RandomizedCollection {
    std::vector<int> data_;
    std::unordered_map<
        int,
        std::unordered_set<int>
    > indices_;
public:
    RandomizedCollection() {}
    
    bool insert(int val) {
        indices_[val].insert(data_.size());
        data_.push_back(val);

        return indices_[val].size() == 1;
    }
    
    bool remove(int val) {
        if (indices_[val].empty()) return false;

        int index = *indices_[val].begin();
        indices_[val].erase(index);

        int lastIndex = data_.size() - 1;
        int lastElement = data_[lastIndex];

        if (index != lastIndex) {
            data_[index] = lastElement;
            
            indices_[lastElement].erase(lastIndex);
            indices_[lastElement].insert(index);
        }

        data_.pop_back();

        return true;
    }
    
    int getRandom() {
        return data_[rand() % data_.size()];
    }
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection* obj = new RandomizedCollection();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */