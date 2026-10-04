/**
 * // This is the HtmlParser's API interface.
 * // You should not implement it, or speculate about its implementation
 * class HtmlParser {
 *   public:
 *     vector<string> getUrls(string url);
 * };
 */

class Solution {
    std::unordered_set<std::string> seen_{};
    std::string hostname_{};

    std::string getHostname(const string& url) {
        size_t start = url.find("://") + 3;
        size_t end = url.find('/', start);

        return url.substr(start, end - start);
    }

    void dfs(string currUrl, HtmlParser htmlParser) {
        seen_.insert(currUrl);
        for (auto& nextUrl : htmlParser.getUrls(currUrl)) {
            if (getHostname(nextUrl) == hostname_ && !seen_.contains(nextUrl)) {
                dfs(nextUrl, htmlParser);
            }
        }
    }

public:
    vector<string> crawl(string startUrl, HtmlParser htmlParser) {
        hostname_ = getHostname(startUrl);
        dfs(startUrl, htmlParser);
        
        std::vector<std::string> ans{};
        for (auto& c : seen_) {
            ans.push_back(c);
        }
        
        return ans;
    }
};