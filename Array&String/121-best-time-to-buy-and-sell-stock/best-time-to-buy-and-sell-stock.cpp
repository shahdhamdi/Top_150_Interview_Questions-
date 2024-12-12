class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        int ans = 0;
        int mn = 100000;  // Initialize to a large value
        for(int i = 0; i < n; i++) {
            if(prices[i] < mn) {
                mn = prices[i];  // Update minimum price
            }  
            else {
                ans = max(ans, prices[i] - mn);  // Update maximum profit
            }
        }
        return ans;
    }
};
