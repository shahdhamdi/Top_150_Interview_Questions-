class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit=0;
        int n=prices.size();
        // Traverse through the prices list
        for(int i=1;i<n;i++)
        {
            int temp=0;
            temp=prices[i]-prices[i-1]; // Calculate the profit from buying and selling on adjacent days
            if(temp>0){
                profit+=temp; // Add the positive profit to the total profit
            }
        }
        return profit;
    }
};