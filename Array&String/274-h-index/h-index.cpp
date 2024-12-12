class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        sort(citations.begin(), citations.end(), greater<>());
        for (int i = 0; i < n; i++) {
            if (i >= citations[i]) {
                return i;
            }
        }
        return n;
    }
};