class TimeMap {
    std::unordered_map<std::string, std::vector<std::pair< int, std::string>>> data_;
public:
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        data_[key].emplace_back(timestamp, value);
    }
    
    string get(string key, int timestamp) {
        auto it = data_.find(key);
        if (it == data_.end()) return "";

        const auto& vals = it->second;
        auto pos = std::ranges::upper_bound(
            vals, timestamp, std::less{}, &std::pair<int, string>::first
        );

        return pos == vals.begin() ? "" : std::prev(pos)->second;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */