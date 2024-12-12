class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n=nums.size();
        int i=0;
        int max=0;
        while(i<n)
        {
            if(i>max)return false;
            if(i+nums[i]>max)max=i+nums[i];
            if(max>=n-1)return true;
            i++;
        } 
        return false;

    }
};