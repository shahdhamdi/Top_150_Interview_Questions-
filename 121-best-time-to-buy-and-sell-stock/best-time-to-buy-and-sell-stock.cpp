class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n
        =prices.size();
        int ans=0;
        int mn=100000;
        for(int i=0;i<n;i++)
        {
            if(prices[i]<mn)
            {
                mn=prices[i];
            }  
            else
            {
              if(ans<prices[i]-mn)
                ans=prices[i]-mn;
            }

        }
        return ans;
    }
};