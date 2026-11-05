class SnapshotArray {
    int n_ = 0;
    std::vector<std::vector<std::pair<int, int>>> array_; 
    int snapId_ = 0;
public:
    SnapshotArray(int length) : n_(length) {
        array_.resize(length);
    }
    
    void set(int index, int val) {
        if (!array_[index].empty() && array_[index].back().first == snapId_) {
            array_[index].back().second = val;
            return;
        }

        array_[index].emplace_back(snapId_, val);
    }
    
    int snap() {
        return snapId_++;
    }
    
    int get(int index, int snap_id) {
        auto& history = array_[index];
        auto it = std::ranges::upper_bound(
            history, snap_id, {}, &std::pair<int, int>::first
        );

        if (it == history.begin()) return 0;
        return std::prev(it)->second;
    }
};

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * SnapshotArray* obj = new SnapshotArray(length);
 * obj->set(index,val);
 * int param_2 = obj->snap();
 * int param_3 = obj->get(index,snap_id);
 */