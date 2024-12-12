class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int count=1;
     for(int i=1;i<nums.size();i++)
     {
        if(count==1||nums[i]!=nums[count-2])
        {
            nums[count]=nums[i];
            count++;
        }
     }
     return count;    
    }
};